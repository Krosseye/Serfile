import json
import os
from datetime import datetime

from flask import render_template, send_from_directory

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

# Read the configuration file
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


def render_html(path, config, directory, version):
    if not path:
        path = config["root_directory"]

    full_path = os.path.join(directory, path)

    if os.path.isdir(full_path):
        files = os.listdir(full_path)
        file_data = []
        for file in files:
            file_path = os.path.join(full_path, file)
            is_folder = os.path.isdir(file_path)
            size = os.path.getsize(file_path)
            size_str = format_size(size)
            if is_folder:
                size_str = "—"
            modified_time = os.path.getmtime(file_path)
            modified_datetime = datetime.fromtimestamp(modified_time)
            icon = get_file_icon(file, is_folder)
            file_data.append({
                "name": file,
                "link": os.path.join(path, file),
                "size_value": size,
                "size": size_str,
                "modified": modified_datetime,
                "icon": icon
            })

        return render_template("index.html",
                               files=file_data,
                               path=path,
                               config=config,
                               version=version)
    elif os.path.isfile(full_path):
        directory, filename = os.path.split(full_path)
        return send_from_directory(directory, filename)
    else:
        return "Not Found", 404
