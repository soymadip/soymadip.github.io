from typing import Annotated

import db_models
from database import Base, engine, get_db
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from models import PostCreate, PostResponse, UserCreate, UserResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static-files")
app.mount("/media", StaticFiles(directory="media"))


@app.post(
    "/api/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(db_models.User).where(db_models.User.username == user.username)
    )

    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )

    result = db.execute(
        select(db_models.User).where(db_models.User.email == user.email)
    )

    existing_email = result.scalars().first()

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    new_user = db_models.User(username=user.username, email=user.email)

    db.add(new_user)  # Stages a new user
    db.commit()  # commits the staged user

    db.refresh(new_user)  # reloads the user from the database

    return new_user


@app.get("/api/users", response_model=list[UserResponse])
def get_users(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(db_models.User))

    users = result.scalars().all()

    if len(users) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No users found"
        )

    return users


@app.get("/api/users/{username}", response_model=UserResponse)
def get_user(username: str, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(db_models.User).where(db_models.User.username == username)
    )

    user = result.scalars().first()

    if user:
        return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@app.get("/api/users/{username}/posts", response_model=list[PostResponse])
def get_user_posts(username: str, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(db_models.User).where(db_models.User.username == username)
    )
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    result = db.execute(select(db_models.Post).where(db_models.Post.user_id == user.id))
    posts = result.scalars().all()

    if len(posts) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No posts found",
        )

    return posts
