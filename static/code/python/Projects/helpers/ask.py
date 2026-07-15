import sys
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Literal,
    Optional,
    Tuple,
    TypeVar,
    Union,
    overload,
)

T = TypeVar("T", str, int, float)

# Define _getch conditionally based on the OS at module level.
if sys.platform == "win32":
    import msvcrt

    def _getch() -> str:
        return msvcrt.getch().decode("utf-8", errors="ignore")
else:
    import termios
    import tty

    def _getch() -> str:
        """Reads a single character from standard input without waiting for Enter (Unix)."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear() -> None:
    """Clears the terminal screen cleanly across platforms."""
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()


def header(title: str) -> None:
    """Prints a consistent UI header block."""
    print("=" * 40)
    print(f" {title.upper()} ".center(40, "="))
    print("=" * 40 + "\n")


# 1. OVERLOAD: Boolean flag inputs (return_index explicitly False)
@overload
def ask(
    question: str,
    response_type: type[bool],
    options: Optional[Union[Iterable[str], Dict[bool, str]]] = None,
    validator: Optional[Callable[[bool], Union[str, bool, None]]] = None,
    menu_msg: str = "Enter a number",
    allow_empty: bool = True,
    press_any_key: bool = False,
    return_index: Literal[False] = False,
    final_options: Optional[
        Union[str, Iterable[Union[str, Tuple[Any, str]]], Dict[Any, str]]
    ] = None,
) -> bool: ...


# 2. OVERLOAD: Standard type conversion fallback (return_index explicitly False or omitted)
@overload
def ask(
    question: str,
    response_type: type[T] = str,
    options: Optional[Union[Iterable[str], Dict[T, str]]] = None,
    validator: Optional[Callable[[T], Union[str, bool, None]]] = None,
    menu_msg: str = "Enter a number",
    allow_empty: bool = True,
    press_any_key: bool = False,
    return_index: Literal[False] = False,
    final_options: Optional[
        Union[str, Iterable[Union[str, Tuple[Any, str]]], Dict[Any, str]]
    ] = None,
) -> T: ...


# 3. OVERLOAD: Forcing to return index integer space (Requires explicit return_index=True)
@overload
def ask(
    question: str,
    response_type: type = str,
    options: Optional[Union[Iterable[str], Dict[Any, str]]] = None,
    validator: Optional[Callable[[int], Union[str, bool, None]]] = None,
    menu_msg: str = "Enter a number",
    allow_empty: bool = True,
    press_any_key: bool = False,
    *,
    return_index: Literal[True],
    final_options: Optional[
        Union[str, Iterable[Union[str, Tuple[Any, str]]], Dict[Any, str]]
    ] = None,
) -> int: ...


def ask(
    question: str,
    response_type: type = str,
    options: Optional[Union[Iterable[str], Dict[Any, str]]] = None,
    validator: Optional[Callable[..., Any]] = None,
    menu_msg: str = "Enter a number",
    allow_empty: bool = True,
    press_any_key: bool = False,
    return_index: bool = False,
    final_options: Optional[
        Union[str, Iterable[Union[str, Tuple[Any, str]]], Dict[Any, str]]
    ] = None,
) -> Any:
    """Prompts a user for input via the command line with options, validation, and layout management.

    Args:
        question: The prompt or question string displayed to the user.
        response_type: The expected type conversion class for the return value (e.g., str, int, bool).
        options: A collection of choices. Can be a list/iterable of values, a dictionary mapping keys to labels,
            or a generator.
        validator: A callback function evaluating the parsed input. Should return a string error message
            to display a custom error, False to signal a generic validation error, or None/True if valid.
        menu_msg: The instruction text printed alongside the selection bounds when options are present.
        allow_empty: If False, prevents the user from skipping the prompt with an empty string when no options are given.
        press_any_key: If True, halts execution until a single key is pressed, short-circuiting standard prompt workflows.
        return_index: If True, forces the function to return the selected option's index (base options return 1-based,
            final options return auto-assigned negative integers starting from -1).
        final_options: System options (like 'Go Back') appended at the bottom of the list separated by a newline.
            Can be passed as a single string, an iterable, a list of tuples, or a dictionary.

    Returns:
        The validated and converted answer conforming to the active overload structure.

    Raises:
        ValueError: If `question` is an empty string, or when option indexes/boolean selections are invalid.
    """
    if not question:
        raise ValueError("question can't be empty!")

    if press_any_key:
        print(question, end="", flush=True)
        _getch()
        print()
        return response_type("") if response_type is not bool else True

    opt_list: List[Tuple[Any, str]] = []
    has_base_options = False

    # 1. Parse base options generator-safely into concrete list
    if options is not None:
        if isinstance(options, dict):
            opt_list = list(options.items())
        else:
            opt_list = [(opt, opt) for opt in options]
        if opt_list:
            has_base_options = True

    base_options_count = len(opt_list)

    # 2. Parse final options safely supporting Single Strings, Iterables, Lists, and Dicts
    final_opt_list: List[Tuple[Any, str]] = []
    if final_options is not None:
        if isinstance(final_options, dict):
            final_opt_list = list(final_options.items())
        else:
            # Safe normalization if a plain string was provided instead of an iterable collection
            normalized_final = (
                [final_options] if isinstance(final_options, str) else final_options
            )

            # If tracking pure indices or integers, auto-assign sequential negative keys: -1, -2, -3...
            if return_index or response_type is int:
                for idx, f_opt in enumerate(normalized_final, start=1):
                    display = f_opt[1] if isinstance(f_opt, tuple) else f_opt
                    final_opt_list.append((-idx, display))
            else:
                for f_opt in normalized_final:
                    if isinstance(f_opt, tuple):
                        final_opt_list.append(f_opt)
                    else:
                        final_opt_list.append((f_opt, f_opt))

    # Join the final option lists to core options array
    opt_list.extend(final_opt_list)

    while True:
        print(f"{question}\n")

        if opt_list:
            for num, (_, display_text) in enumerate(opt_list, start=1):
                # Insert visual layout spacing newline when hitting final options space
                if has_base_options and num == base_options_count + 1:
                    print()
                print(f"{num}. {display_text}")

        try:
            prompt = ">> "
            if opt_list:
                prompt = f"\n{menu_msg} (1-{len(opt_list)}) >> "
            elif response_type is bool:
                prompt = "[y/n] >> "

            answer = input(prompt).strip()

            if not opt_list and not allow_empty and not answer:
                raise ValueError("Input cannot be empty.")

            if opt_list:
                if not answer.isdigit() or not (1 <= int(answer) <= len(opt_list)):
                    raise ValueError(
                        f"Selection must be a number between 1 and {len(opt_list)}."
                    )

                chosen_num = int(answer)
                selected_key = opt_list[chosen_num - 1][0]

                # If return_index is requested, map selections appropriately
                if return_index:
                    if chosen_num > base_options_count:
                        # Keep the negative indicator key for the final option
                        converted_answer = selected_key
                    else:
                        # Return the regular 1-based option choice index
                        converted_answer = chosen_num
                # If explicit int response is requested
                elif response_type is int:
                    if chosen_num > base_options_count and isinstance(
                        selected_key, int
                    ):
                        converted_answer = selected_key
                    else:
                        try:
                            converted_answer = int(selected_key)
                        except ValueError, TypeError:
                            converted_answer = chosen_num
                else:
                    # Resolve using base dictionary mapping contexts or primitive conversions
                    if (
                        options is not None
                        and isinstance(options, dict)
                        and (chosen_num <= base_options_count)
                    ):
                        converted_answer = selected_key
                    else:
                        converted_answer = response_type(selected_key)

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

