import json
import os
from datetime import datetime

from file_icons import ICON_MAP
from flask import Flask, render_template, send_from_directory
from version import version
from waitress import serve

app = Flask(__name__)

# Get the directory path of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the config file
config_file_path = os.path.join(script_directory, "config.json")

# Read configuration from config.json
with open(config_file_path, "r") as config_file:
    config = json.load(config_file)

# Define the app version
APP_VERSION = version

# Serve files from the "static" directory
static_directory = os.path.join(os.path.dirname(__file__), "static")


# Function to get the appropriate icon for a file or folder
def get_file_icon(filename, is_folder=False):
    if is_folder:
        return "📁"

    extension = os.path.splitext(filename)[1].lower()
    return ICON_MAP.get(extension, "📄")


# Function to format file size in a human-readable way
def format_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_files(path):
    if not path:
        path = config["root_directory"]

    full_path = os.path.join(static_directory, path)

    if os.path.isdir(full_path):
        files = os.listdir(full_path)
        file_data = []
        for file in files:
            file_path = os.path.join(full_path, file)
            is_folder = os.path.isdir(file_path)
            size = os.path.getsize(file_path)
            size_str = format_size(size)
            modified_time = os.path.getmtime(file_path)
            modified_datetime = datetime.fromtimestamp(modified_time)
            icon = get_file_icon(file, is_folder)
            file_data.append({
                "name": file,
                "link": os.path.join(path, file),
                "size": size_str,
                "modified": modified_datetime,
                "icon": icon
            })

        return render_template("index.html", files=file_data, path=path, config=config, version=version)
    elif os.path.isfile(full_path):
        directory, filename = os.path.split(full_path)
        return send_from_directory(directory, filename)
    else:
        return "Not Found", 404


@app.route('/version', methods=['GET'])
def get_version():
    return {'version': APP_VERSION}


if __name__ == "__main__":
    print(f"Serving on http://{config['host']}:{config['port']}")
    serve(app, host=config["host"], port=config["port"])
