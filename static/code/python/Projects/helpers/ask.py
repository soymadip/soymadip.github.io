from typing import Callable, TypeVar

T = TypeVar("T", str, int, float)


def ask(
    question: str,
    response_type: type[T] = str,
    options: list[str | int | float] | None = None,
    case_sensitive: bool = False,
    validator: Callable[[T], str | bool | None] | None = None,
) -> T:
    if not question:
        raise ValueError("question can't be empty!")

    while True:
        print(f'{question}?')

        if options:
            for num, option in enumerate(options, start=1):
                print(f"  {num}. {option}")

        try:
            answer = input(">> ").strip()
            converted_answer = response_type(answer)

            if options:
                answer_check = answer if case_sensitive else answer.lower()
                options_check = [
                    str(item) if case_sensitive else str(item).lower()
                    for item in options
                ]
                if answer_check not in options_check:
                    raise ValueError("Answer must be within given options")

            if validator:
                validation_result = validator(converted_answer)
                
                if isinstance(validation_result, str):
                    raise ValueError(validation_result)
                elif validation_result is False:
                    raise ValueError("Invalid input.")

            return converted_answer

        except ValueError as e:
            print()
            if "invalid literal for int()" in str(e) or "could not convert" in str(e):
                print(f"Error: Expected a valid {response_type.__name__}.\n")
            else:
                print(f"Error: {e}\n")
