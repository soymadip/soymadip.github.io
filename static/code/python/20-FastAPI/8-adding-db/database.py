from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///./blog.db"

# Create the engine
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False  # Only needed for sqlite
    },
)


# Make a sessionmaker for the engine
SessionLocal = sessionmaker(
    bind=engine,  # the engine to use
    #
    # Turn off autocommit and autoflush
    # This is important for transaction management in FastAPI
    autocommit=False,
    autoflush=False,
)


# provides session to our FastAPI routes
def get_db():
    with SessionLocal() as db:
        yield db


# Create a base class for declarative models
class Base(DeclarativeBase):
    pass
