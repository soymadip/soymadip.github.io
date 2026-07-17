import sys
import time
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

if sys.platform == "win32":
    import msvcrt

    def _getch() -> str:
        return msvcrt.getch().decode("utf-8", errors="ignore")
else:
    import termios
    import tty

    def _getch() -> str:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def _normalize_options(opts: Any) -> List[Tuple[Any, str]]:
    """Helper to convert lists, lists of tuples, and dicts into a standard List[Tuple] format."""
    if not opts:
        return []
    if isinstance(opts, dict):
        return list(opts.items())
    if isinstance(opts, str):
        return [(opts, opts)]

    normalized = []
    for item in opts:
        if isinstance(item, tuple) and len(item) == 2:
            normalized.append(item)
        else:
            normalized.append((item, str(item)))
    return normalized


@overload
def ask(
    question: str,
    response_type: type[bool],
    options: Optional[
        Union[Iterable[Union[str, Tuple[bool, str]]], Dict[bool, str]]
    ] = None,
    validator: Optional[Callable[[bool], Union[str, bool, None]]] = None,
    menu_msg: str = "Enter a number",
    allow_empty: bool = False,
    press_any_key: bool = False,
    return_index: Literal[False] = False,
    final_options: Optional[
        Union[str, Iterable[Union[str, Tuple[Any, str]]], Dict[Any, str]]
    ] = None,
) -> bool: ...


@overload
def ask(
    question: str,
    response_type: type[T] = str,
    options: Optional[Union[Iterable[Union[T, Tuple[T, str]]], Dict[T, str]]] = None,
    validator: Optional[Callable[[T], Union[str, bool, None]]] = None,
    menu_msg: str = "Enter a number",
    allow_empty: bool = False,
    press_any_key: bool = False,
    return_index: Literal[False] = False,
    final_options: Optional[
        Union[str, Iterable[Union[str, Tuple[Any, str]]], Dict[Any, str]]
    ] = None,
) -> T: ...


@overload
def ask(
    question: str,
    response_type: type = str,
    options: Optional[
        Union[Iterable[Union[Any, Tuple[Any, str]]], Dict[Any, str]]
    ] = None,
    validator: Optional[Callable[[int], Union[str, bool, None]]] = None,
    menu_msg: str = "Enter a number",
    allow_empty: bool = False,
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
    options: Optional[Union[Iterable[Any], Dict[Any, str]]] = None,
    validator: Optional[Callable[..., Any]] = None,
    menu_msg: str = "Enter a number",
    allow_empty: bool = False,
    press_any_key: bool = False,
    return_index: bool = False,
    final_options: Optional[
        Union[str, Iterable[Union[str, Tuple[Any, str]]], Dict[Any, str]]
    ] = None,
) -> Any:
    if not question:
        raise ValueError("question can't be empty!")

    if press_any_key:
        print(question, end="", flush=True)
        _getch()
        print()
        return response_type("") if response_type is not bool else True

    # Normalize both options and final_options into a standard List[Tuple[key, display_text]]
    opt_list = _normalize_options(options)
    has_base_options = bool(opt_list)
    base_options_count = len(opt_list)

    final_opt_list = _normalize_options(final_options)

    # Process final options indexing logic
    if return_index or response_type is int:
        final_opt_list = [
            (-idx, display) for idx, (_, display) in enumerate(final_opt_list, start=1)
        ]

    opt_list.extend(final_opt_list)

    while True:
        print(f"{question}\n")

        if opt_list:
            for num, (_, display_text) in enumerate(opt_list, start=1):
                if has_base_options and num == base_options_count + 1:
                    print()
                print(f"{num}. {display_text}")

        while True:
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

                    if return_index:
                        if chosen_num > base_options_count:
                            converted_answer = selected_key
                        else:
                            converted_answer = chosen_num
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
                        if isinstance(selected_key, response_type):
                            converted_answer = selected_key
                        else:
                            try:
                                converted_answer = response_type(selected_key)
                            except ValueError, TypeError:
                                converted_answer = selected_key

                elif response_type is bool:
                    cleaned_ans = answer.lower()
                    if cleaned_ans in ("y", "yes", "true", "1"):
                        converted_answer = True
                    elif cleaned_ans in ("n", "no", "false", "0"):
                        converted_answer = False
                    else:
                        raise ValueError(
                            "Expected a confirmation response (yes/no or y/n)"
                        )

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
                if "invalid literal for int()" in str(e) or "could not convert" in str(
                    e
                ):
                    err_msg = f"Error: Expected a valid {response_type.__name__}."
                else:
                    err_msg = f"Error: {e}"

                sys.stdout.write(f"\033[F\033[K\r\033[1;31m{err_msg}\033[0m  ")
                sys.stdout.flush()

                time.sleep(2.5)

                sys.stdout.write("\r\033[K")
                if opt_list:
                    sys.stdout.write("\033[F\033[K")
                sys.stdout.flush()
