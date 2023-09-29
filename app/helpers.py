"""This module contains helper functions used throughout the application."""

import json
import os
from datetime import datetime
from typing import Dict

from app.file_icons import ICON_MAP
from cssmin import cssmin
from flask import abort, render_template
from jsmin import jsmin


def get_file_icon(filename: str, is_dir: bool = False) -> str:
    """
    Returns an icon based on the file extension or folder name.
    """
    if is_dir:
        if filename == "Public":
            return "🌐"
        if filename == "Private":
            return "🔒"
        return "📁"

    extension: str = os.path.splitext(filename)[1].lower()
    return ICON_MAP.get(extension, "📄")


def format_size(size: int) -> str:
    """
    Takes a file size in bytes and returns a human-readable string
    in the appropriate unit (Bytes, KB, MB, GB, or TB).
    """
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    unit_index = 0
    size_float: float = float(size)
    while size_float >= 1024 and unit_index < len(units) - 1:
        size_float /= 1024
        unit_index += 1
    return f"{size_float:.2f} {units[unit_index]}"


def read_json_file(file_path: str) -> Dict[str, str]:
    """
    Reads the JSON file and returns its contents as a dictionary.
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def minify_and_bundle_files(
    directory_path: str, bundle_name: str, file_extension: str
) -> None:
    """
    Minifies and bundles CSS and JS files in a directory into a single file.
    """
    css_code = ""
    js_code = ""

    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension) and not filename.endswith(
            f".min{file_extension}"
        ):
            with open(
                os.path.join(directory_path, filename), "r", encoding="utf-8"
            ) as file:
                file_content = file.read()

                if file_extension == ".css":
                    css_code += file_content
                elif file_extension == ".js":
                    js_code += file_content

    if css_code:
        minified_css_code = cssmin(css_code)
        bundle_css_filename = f"{bundle_name}.min{file_extension}"
        with open(
            os.path.join(directory_path, bundle_css_filename), "w", encoding="utf-8"
        ) as css_file:
            css_file.write(minified_css_code)
        print(f"* Bundled and minified CSS files into {bundle_css_filename}")

    if js_code:
        minified_js_code = jsmin(js_code)
        bundle_js_filename = f"{bundle_name}.min{file_extension}"
        with open(
            os.path.join(directory_path, bundle_js_filename), "w", encoding="utf-8"
        ) as js_file:
            js_file.write(minified_js_code)
        print(f"* Bundled and minified JS files into {bundle_js_filename}")


def get_environment(config: Dict[str, str]) -> bool:
    """
    Takes a dictionary `config` as input and returns a boolean value
    indicating whether the environment is production or not.
    """
    environment: str = config["environment"]
    is_prod: bool = False

    if environment in ("development", "dev"):
        is_prod = False
        return is_prod
    if environment in ("production", "prod"):
        is_prod = True
        return is_prod
    else:
        is_prod = True
        return is_prod


def render_browser(
    path: str, config: Dict[str, str], directory: str, version: str
) -> str:
    """
    Renders a web page that displays the contents of a directory.
    """
    if not path:
        path = config["rootName"]

    full_path: str = os.path.join(directory, path)

    is_prod: bool = get_environment(config)

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
            file_data.append(
                {
                    "name": file,
                    "link": os.path.join(path, file),
                    "size": size,
                    "size_str": size_str,
                    "modified": modified_datetime,
                    "icon": icon,
                    "is_dir": is_dir,
                }
            )

        return render_template(
            "index.html",
            files=file_data,
            path=path,
            config=config,
            version=version,
            is_prod=is_prod,
        )
    else:
        abort(404)
