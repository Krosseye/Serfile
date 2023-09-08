import json
import os
from datetime import datetime

from cssmin import cssmin
from flask import render_template, send_from_directory
from jsmin import jsmin

from .file_icons import ICON_MAP


def get_file_icon(filename, is_dir=False):   # Get icon for a file or folder
    if is_dir:
        return "📁"

    extension = os.path.splitext(filename)[1].lower()
    return ICON_MAP.get(extension, "📄")


def format_size(size):  # Format file size in a human-readable way
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


def read_json_file(file_path):  # Read the configuration file
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {file_path}: {e}")
        return None


def minify_files(directory_path, file_extension):
    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension) and not filename.endswith(f".min{file_extension}"):
            file_folder = os.path.join(directory_path)
            minified_path = os.path.join(file_folder, filename.replace(
                file_extension, f".min{file_extension}"))

            print(f" * Minifying {filename}")
            with open(os.path.join(file_folder, filename), 'r') as file:
                if file_extension == ".css":
                    minified_code = cssmin(file.read())
                elif file_extension == ".js":
                    minified_code = jsmin(file.read())

            with open(minified_path, 'w') as minified_file:
                minified_file.write(minified_code)


def get_environment(config):
    environment = config['environment']
    
    if environment == 'production' or environment == 'prod':
        is_prod = True
        return is_prod
    elif environment == 'development' or environment == 'dev':
        is_prod = False
        return is_prod
        
def render_html(path, config, directory, version):
    if not path:
        path = config["root_directory"]

    full_path = os.path.join(directory, path)
    
    is_prod = get_environment(config)

    if os.path.isdir(full_path):
        files = os.listdir(full_path)
        file_data = []
        for file in files:
            file_path = os.path.join(full_path, file)
            is_dir = os.path.isdir(file_path)
            size = os.path.getsize(file_path)
            size_str = format_size(size)
            if is_dir:
                size_str = "—"
            modified_time = os.path.getmtime(file_path)
            modified_datetime = datetime.fromtimestamp(modified_time)
            icon = get_file_icon(file, is_dir)
            file_data.append({
                "name": file,
                "link": os.path.join(path, file),
                "size": size,
                "size_str": size_str,
                "modified": modified_datetime,
                "icon": icon,
                "is_dir": is_dir
            })

        return render_template("index.html",
                               files=file_data,
                               path=path,
                               config=config,
                               version=version,
                               is_prod=is_prod)
    elif os.path.isfile(full_path):
        directory, filename = os.path.split(full_path)
        return send_from_directory(directory, filename)
    else:
        return "Not Found", 404
