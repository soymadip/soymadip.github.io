def format_size(size_bytes: float) -> tuple[int | float, str]:

    if not isinstance(size_bytes, (int, float)):
        raise TypeError("Input must be of type float/int")

    if size_bytes < 0:
        raise ValueError("Input Must be positive number")

    units: list[str] = ["b", "kb", "mb", "gb", "tb", "pb"]

    size = float(size_bytes)
    step: int = 1024

    for unit in units:
        unit = unit.upper()

        if size < 1024:
            return (round(size, 2) if unit != "B" else int(size), unit)
        size = size / step

    return round(size, 2), units[-1].upper()
