"""
Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import json
from pathlib import Path
from time import sleep
from typing import Literal

from helpers import ask, clear, header


def main() -> None:
    db_file = Path(".cache/ss.json")

    db_file.parent.mkdir(parents=True, exist_ok=True)

    movies = []

    def save_movies():
        try:
            with open(db_file, "w", encoding="utf-8") as file:
                json.dump(movies, file, indent=2)
        except Exception as e:
            print(f"Error: {e}")

    def list_movies(
        query: str | None = None, search_basis: Literal["name", "genre"] = "name"
    ):
        # Remove the return "No Movie in Database!" string!
        if not movies:
            return

        for movie in movies:
            if query:
                clean_query = query.strip().lower()
                if search_basis == "name":
                    if clean_query not in movie["name"].lower():
                        continue
                else:
                    if clean_query not in [g.lower() for g in movie["genre"]]:
                        continue

            yield f"{movie['name']} [{movie['progress']}]"

    if not db_file.exists() or db_file.stat().st_size == 0:
        save_movies()

    try:
        with open(db_file, "r", encoding="utf-8") as file:
            movies = json.load(file)
    except Exception as e:
        print(f"Error: {e}")

    while True:
        clear()
        header("Movie Tracker")

        action = ask(
            "Select An Optoin",
            options={
                "view": "View All Movies",
                "search": "Search Movies",
                "add": "Add a Movie",
                "update": "Update Movie Data",
                "delete": "Delete Movies",
            },
            final_options={"exit": "Exit App"},
        )

        clear()
        match action:
            case "view":
                if not movies:
                    header("All Tracked Movies")
                    print("\nNo movies in database yet! Go add some first.")
                    ask("", press_any_key=True)
                    continue

                while True:
                    header("All Tracked Movies")

                    selected = (
                        ask(
                            "",
                            options=list_movies(),
                            final_options={"return": "Return to Main Menu"},
                            return_index=True,
                            menu_msg="Enter a Movie Number to know More / Return to Main Menu",
                        )
                        - 1
                    )

                    if selected < 0:
                        break

                    selected_movie = movies[selected]

                    clear()
                    header(f"{selected_movie['name']}", bar_len=70)

                    print(
                        "> Genre:",
                        ", ".join(genre for genre in selected_movie["genre"]),
                    )
                    print("> Rating:", str(selected_movie["rating"]) + "/10")
                    print("> Progress:", selected_movie["progress"])

                    ask(
                        "\n\nEnter any key to return to movies list..",
                        press_any_key=True,
                    )
                    clear()

            case "add":
                header("Add A Movie")

                name = ask(
                    "Enter Movie Name",
                    response_type=str,
                    validator=lambda x: (
                        "Movie already Exists"
                        if any(
                            x.strip().lower() == movie["name"].lower()
                            for movie in movies
                        )
                        else True
                    ),
                ).strip()

                genre = ask("\nEnter Comma Separated Movie's Genre(s)")
                progress = ask(
                    "\nSelect Movie's Progress",
                    options=[
                        "planning",
                        "completed",
                        "in-progress",
                        "dropped",
                        "custom",
                    ],
                )
                rating = round(
                    ask(
                        "\nGive this Moview a rating (out of 10)",
                        response_type=float,
                        validator=lambda x: (
                            "Enter between 1-10" if x < 1.0 or x > 10.0 else True
                        ),
                    ),
                    2,
                )

                if progress == "custom":
                    progress = str(
                        ask(
                            "\nEnter custom Progress (in precentage)",
                            response_type=int,
                            validator=lambda x: (
                                "Enter a valid progress" if x > 100 or x < 0 else True
                            ),
                        )
                    )

                    if progress == "100":
                        progress = "completed"
                    else:
                        progress += "%"

                movies.append(
                    {
                        "name": name,
                        "genre": [x.strip() for x in genre.split(",")],
                        "progress": progress,
                        "rating": rating,
                    }
                )

                save_movies()

                print("\n[Success] Movie Added Successfully!")
                sleep(1.2)

            case "search":
                header("Search a Movie")

                search_basis = ask(
                    "What do you wanna search with",
                    options=["name", "genre"],
                )

                query = ask(f"\nEnter {search_basis} to search")

                clear()
                header("Search Results")
                selected = (
                    ask(
                        "",
                        options=list_movies(query, search_basis),  # pyright: ignore[reportArgumentType]
                        menu_msg="Enter a Number for More Info / Return",
                        final_options={"return": "Return to Main Menu"},
                    )
                    .split("[", 1)[0]
                    .strip()
                )

                if selected == "return":
                    continue

                ask("\nPress any key to return to main menu..", press_any_key=True)

            case "update":
                if not movies:
                    header("Update a Movie")
                    print("\nNo movies to update yet!")
                    ask("", press_any_key=True)
                    continue

                while True:
                    header("Update a Movie")
                    selected = (
                        ask(
                            "",
                            options=list_movies(),
                            response_type=int,
                            return_index=True,
                            menu_msg="Enter a No. to Update / Return",
                            final_options="Return To Main Menu",
                        )
                        - 1
                    )

                    if selected < 0:
                        break

                    selected_movie = movies[selected]

                    def heading():
                        return header(f"Updating: {selected_movie['name']}", bar_len=60)  # pyright: ignore[reportIndexIssue]

                    clear()
                    heading()
                    to_update = ask(
                        "What do You wanna Update?",
                        options={field: field.title() for field in selected_movie},
                        final_options={"return": "Return to Previous Menu"},
                    )

                    if to_update == "return":
                        clear()
                        continue

                    clear()
                    heading()

                    match to_update:
                        case "name":
                            selected_movie["name"] = ask(
                                "Enter New Name",
                                validator=lambda x: (
                                    "Movie Name Already Exists"
                                    if any(
                                        x.lower() == movie["name"].lower()
                                        for movie in movies
                                    )
                                    else True
                                ),
                            )

                        case "genre":
                            selected_movie["genre"] = [
                                genre.strip()
                                for genre in ask("Enter Comma Separated Genres").split(
                                    ","
                                )
                            ]

                        case "progress":
                            selected_state = ask(
                                "Select Movie Progress",
                                options=[
                                    "Planning",
                                    "Completed",
                                    "In-Progress",
                                    "Dropped",
                                    "Custom",
                                ],
                            ).lower()

                            if selected_state == "custom":
                                clear()
                                heading()
                                progress = str(
                                    ask(
                                        "Enter custom Progess (in percnetage)",
                                        response_type=int,
                                        validator=lambda x: (
                                            "Enter between 0-100"
                                            if x < 0 or x > 100
                                            else True
                                        ),
                                    )
                                )
                                if progress == "100":
                                    progress = "completed"
                                else:
                                    progress = progress + "%"

                            else:
                                progress = selected_state

                            selected_movie["progress"] = progress

                        case "rating":
                            selected_movie["rating"] = round(
                                ask(
                                    "Enter a rating (out of 10)",
                                    response_type=float,
                                    validator=lambda x: (
                                        "Enter between 1-10"
                                        if (x < 1.0 or x > 10.0)
                                        else True
                                    ),
                                ),
                                2,
                            )

                    save_movies()
                    clear()

            case "delete":
                while True:
                    header("Delete a Movie")

                    selected_movie = (
                        ask(
                            "Tracked Movies:",
                            options=list_movies(),
                            final_options="Return to Main Menu",
                            menu_msg="Enter a Movie Number to Delete / Return",
                            return_index=True,
                        )
                        - 1
                    )

                    if selected_movie < 0:
                        break

                    selected_movie = movies[selected_movie]

                    movies.remove(selected_movie)
                    save_movies()

                    print("Removed", selected_movie)
                    sleep(1)
                    clear()

            case "exit":
                clear()
                print("ok, See ya untill next time")
                break


#
# Execute only if file executed directly
if __name__ == "__main__":
    main()
