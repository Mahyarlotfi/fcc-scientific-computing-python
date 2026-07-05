def add_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings.update({key:value})
    return f"Setting '{key}' added with value '{value}' successfully!"