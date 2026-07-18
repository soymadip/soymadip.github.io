def flatten_json(data: dict | list, separator: str = ".") -> dict | list:

    if not data:
        return data

    def _flatten(current_data, target_dict, parent_key=""):
        if isinstance(current_data, dict):
            if not current_data:
                target_dict[""] = None
            else:
                for key, val in current_data.items():
                    new_key = (
                        f"{parent_key}{separator if parent_key != '' else ''}{key}"
                    )
                    _flatten(val, target_dict, new_key)
        elif isinstance(current_data, list):
            if not current_data:
                target_dict[""] = None
            else:
                for i, val in enumerate(current_data):
                    new_key = f"{parent_key}{separator if parent_key != '' else ''}{i}"
                    _flatten(val, target_dict, new_key)
        else:
            target_dict[parent_key] = current_data

    if isinstance(data, dict):
        flattened_dict = {}
        _flatten(data, flattened_dict)
        return flattened_dict
    else:
        flattened_list = []
        for dict_element in data:
            row_dict = {}
            _flatten(dict_element, row_dict)
            flattened_list.append(row_dict)
        return flattened_list
