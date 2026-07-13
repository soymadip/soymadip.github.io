from typing import Callable, Iterable, Optional, TypeVar, Union, overload

T = TypeVar("T", str, int, float)


@overload
def ask(
    question: str,
    response_type: type[bool],
    options: Optional[Iterable[str]] = None,
    validator: Optional[Callable[[bool], Union[str, bool, None]]] = None,
    menu_msg: str = "Enter a number",
) -> bool: ...


@overload
def ask(
    question: str,
    response_type: type[T] = str,
    options: Optional[Iterable[str]] = None,
    validator: Optional[Callable[[T], Union[str, bool, None]]] = None,
    menu_msg: str = "Enter a number",
) -> T: ...


def ask(
    question: str,
    response_type: type = str,
    options: Optional[Iterable[str]] = None,
    validator: Optional[Callable] = None,
    menu_msg: str = "Enter a number",
):
    if not question:
        raise ValueError("question can't be empty!")

    if options is not None:
        options = list(options)

    while True:
        print(f"{question}\n")

        if options:
            for num, option in enumerate(options, start=1):
                print(f"{num}. {option}")

        try:
            prompt = ">> "
            if options:
                prompt = f"\n{menu_msg} (1-{len(options)}) >> "
            elif response_type is bool:
                prompt = "[y/n] >> "

            answer = input(prompt).strip()

            if options:
                # Ensure they typed an integer within the range
                if not answer.isdigit() or not (1 <= int(answer) <= len(options)):
                    raise ValueError(
                        f"Selection must be a number between 1 and {len(options)}."
                    )

                # If they passed response_type=int, give them the index.
                # Otherwise, default to returning the string text of the selected option.
                if response_type is int:
                    converted_answer = int(answer)
                else:
                    converted_answer = response_type(options[int(answer) - 1])

            elif response_type is bool:
                cleaned_ans = answer.lower()
                if cleaned_ans in ("y", "yes", "true", "1"):
                    converted_answer = True
                elif cleaned_ans in ("n", "no", "false", "0"):
                    converted_answer = False
                else:
                    raise ValueError("Expected a confirmation response (yes/no or y/n)")

            else:
                converted_answer = response_type(answer)

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
