import os
from datetime import datetime

from flask import Flask, jsonify, redirect, request

from .about import app_version, licenses
from .helpers import format_size, get_file_icon, read_config, render_html

app = Flask(__name__)

# Define constants
APP_VERSION = app_version
CONFIG = read_config()

# Serve files from "static" directory
static_directory = os.path.join(os.path.dirname(__file__), "static")

# Create root_directory if it doesn't exist
root_directory_name = CONFIG["root_directory"]
root_directory_path = os.path.join(static_directory, root_directory_name)
if not os.path.exists(root_directory_path):
    os.makedirs(root_directory_path)


# ---Web-UI Routes---


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def files_route(path):
    config = CONFIG
    version = APP_VERSION
    directory = static_directory
    return render_html(path, config, directory, version)


@app.route("/root/")
@app.route("/root")
def redirect_to_main_page():
    return redirect("/", code=302)


# ---API Routes---


@app.route('/api/version', methods=['GET'])
def get_version():
    return {'version': APP_VERSION}


@app.route('/api/licenses', methods=['GET'])
def get_info():
    return licenses


@app.route("/api/list/<path:path>", methods=['GET'])
def list_files_json(path):
    full_path = os.path.join(static_directory, path)
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

            link_path = os.path.join(path, file).replace(os.path.sep, '/')

            file_data.append({
                "name": file,
                "location": link_path,
                "size": size_str,
                "modified": modified_datetime,
                "icon": icon
            })
        return {"files": file_data}
    else:
        return "Not Found", 404


@app.route('/api/upload/<path:directory>/', methods=['POST'])
@app.route('/api/upload/<path:directory>/<path:subdirectory>/', methods=['POST'])
def upload_file(directory='', subdirectory=''):
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if subdirectory:
            target_directory = os.path.join(
                static_directory, directory, subdirectory)
        else:
            target_directory = os.path.join(static_directory, directory)

        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        file_path = os.path.join(target_directory, uploaded_file.filename)

        # Get the 'overwrite' parameter from the request
        overwrite = request.args.get('overwrite', '').lower() == 'true'

        if os.path.exists(file_path) and not overwrite:
            return jsonify({'error': 'File already exists. To overwrite, include "overwrite=true" in the request parameters.'}), 409

        uploaded_file.save(file_path)

        if os.path.exists(file_path) and overwrite:
            return jsonify({'message': 'File overwritten successfully'}), 200
        else:
            return jsonify({'message': 'File uploaded successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
