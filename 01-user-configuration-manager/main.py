def add_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings.update({key:value})
    return f"Setting '{key}' added with value '{value}' successfully!"
    
def update_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
        
def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
        
def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key, value in settings.items():
            key = key.capitalize()
            result += f"{key}: {value}\n"
        return result
        
test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}