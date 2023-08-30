import json
import os

from .file_icons import ICON_MAP


# Get icon for a file or folder
def get_file_icon(filename, is_folder=False):
    if is_folder:
        return "📁"

    extension = os.path.splitext(filename)[1].lower()
    return ICON_MAP.get(extension, "📄")


# Format file size in a human-readable way
def format_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


def read_config():
    # Get directory of current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Navigate up one directory to reach config.json
    parent_directory = os.path.dirname(script_directory)

    # Construct full path to config
    config_file_path = os.path.join(parent_directory, "config.json")

    # Read config
    with open(config_file_path, "r") as config_file:
        config = json.load(config_file)
        return config
