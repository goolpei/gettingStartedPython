def add_setting(dict_of_settings, tuple_):
    key = tuple_[0]
    value = tuple_[1]
    key, value = key.lower(), value.lower()
    if key in dict_of_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dict_of_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dict_of_settings, tuple_):
    key = tuple_[0]
    value = tuple_[1]
    key, value = key.lower(), value.lower()
    if key in dict_of_settings:
        dict_of_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict_of_settings, key):
    key = key.lower()
    if key in dict_of_settings:
        dict_of_settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(dict_of_settings):
    if not dict_of_settings: return "No settings available."
    output = "Current User Settings:\n"
    for key, value in dict_of_settings.items():
        output += f"{key.capitalize()}: {value}\n"
    
    return output

test_settings = {
    'Hello': 'World'
}