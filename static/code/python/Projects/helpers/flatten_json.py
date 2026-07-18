def flatten_json(raw_data: dict, separator: str = "_") -> dict:
    flat_dict = {}

    def flatten(data, parent_key: str = ""):

        if isinstance(data, dict):
            for ky, val in data.items():
                new_key: str = f"{parent_key}{separator if parent_key else ''}{ky}"

                flatten(val, new_key)

        elif isinstance(data, list):
            for i, val in enumerate(data):
                new_key = f"{parent_key}{separator if parent_key else ''}{i}"

                flatten(val, new_key)

        else:
            flat_dict[parent_key] = data

    flatten(raw_data)
    return flat_dict
