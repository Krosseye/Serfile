import json
import os
from datetime import datetime

from app.file_icons import ICON_MAP
from cssmin import cssmin
from flask import abort, render_template
from jsmin import jsmin


def get_file_icon(filename, is_dir=False):   # Get icon for a file or folder
    def is_public_dir():
        if filename == 'Public':
            return True

    def is_private_dir():
        if filename == 'Private':
            return True

    if is_dir:
        if is_public_dir():
            return "🌐"
        elif is_private_dir():
            return "🔒"
        else:
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


def get_folder_size(folder_path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            total_size += os.path.getsize(filepath)

    return total_size


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


def minify_and_bundle_files(directory_path, bundle_name, file_extension):
    css_code = ""
    js_code = ""

    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension) and not filename.endswith(f".min{file_extension}"):
            with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
                file_content = file.read()

                if file_extension == ".css":
                    css_code += file_content
                elif file_extension == ".js":
                    js_code += file_content

    if css_code:
        minified_css_code = cssmin(css_code)
        bundle_css_filename = f"{bundle_name}.min{file_extension}"
        with open(os.path.join(directory_path, bundle_css_filename), 'w', encoding='utf-8') as css_file:
            css_file.write(minified_css_code)
        print(f"* Bundled and minified CSS files into {bundle_css_filename}")

    if js_code:
        minified_js_code = jsmin(js_code)
        bundle_js_filename = f"{bundle_name}.min{file_extension}"
        with open(os.path.join(directory_path, bundle_js_filename), 'w', encoding='utf-8') as js_file:
            js_file.write(minified_js_code)
        print(f"* Bundled and minified JS files into {bundle_js_filename}")


def get_environment(config):
    environment = config['environment']

    if environment == 'production' or environment == 'prod':
        is_prod = True
        return is_prod
    elif environment == 'development' or environment == 'dev':
        is_prod = False
        return is_prod


def render_browser(path, config, directory, version):
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
    else:
        abort(404)
