def header(heading: str = "", bar_symbol: str = "-", bar_len: int = 30) -> None:
    if len(heading) > bar_len:
        bar_len = len(heading) + 6

    if heading:
        heading = f" {heading} "

    print(heading.center(bar_len, bar_symbol))
