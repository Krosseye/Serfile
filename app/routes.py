"""This module contains all the routes for the application."""

import os
from datetime import datetime
from typing import Dict

import psutil
from app import APP_VERSION, CONFIG, LICENSES, app, helpers, static_directory
from flask import (
    Response,
    abort,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
)
from werkzeug.utils import secure_filename


# ! Files Route
@app.route("/file/<path:path>", defaults={"path": ""})
@app.route("/file/<path:path>")
def files_route(path: str) -> Response:
    """
    Returns a file from a specified directory and path.
    """
    directory: str = static_directory
    full_path: str = os.path.join(directory, path)
    directory, filename = os.path.split(full_path)
    return send_from_directory(directory, filename)


# ! Error Handling Routes
@app.errorhandler(404)
def page_not_found(error: str):
    """
    Renders an error page with a 404 error code and a custom error
    message.
    """
    config: Dict[str, str] = CONFIG
    return (
        render_template(
            "error.html",
            error_code=404,
            error_message=error,
            config=config,
        ),
        404,
    )


@app.errorhandler(500)
def internal_server_error(error: str):
    """
    Renders an error page with a 500 error code and a custom error
    message.
    """
    config: Dict[str, str] = CONFIG
    return (
        render_template(
            "error.html",
            error_code=500,
            error_message=error,
            config=config,
        ),
        500,
    )


# ! Web-UI Routes
@app.route("/browser/", defaults={"path": ""})
@app.route("/browser/<path:path>")
def browser_route(path: str) -> str:
    """
    Takes a path as input and returns a rendered browser page.
    """
    config: Dict[str, str] = CONFIG
    version: str = APP_VERSION
    directory = static_directory
    return helpers.render_browser(path, config, directory, version)


@app.route("/")
@app.route("/browser/home/")
def redirect_to_browser():
    """
    Redirects the user to a browser page.
    """
    return redirect("/browser", code=302)


@app.route("/editor/<path:path>")
def editor_route(path: str) -> str:
    """
    Reads the contents of a file and renders an Ace editor template.
    """
    config: Dict[str, str] = CONFIG
    is_prod: bool | None = helpers.get_environment(config)
    file_path: str = os.path.normpath(os.path.join(static_directory, path))

    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        abort(404)

    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()

    # Render Ace editor template
    return render_template(
        "editor.html",
        file_contents=file_contents,
        config=config,
        file_path=path,
        is_prod=is_prod,
    )


# ! API Routes
@app.route("/api/version", methods=["GET"])
def get_version():
    return {"version": APP_VERSION}


@app.route("/api", methods=["GET"])
def get_greeting():
    return {"helloWorld": "Serfile is running"}


@app.route("/api/licenses", methods=["GET"])
def get_info():
    return LICENSES


@app.route("/api/motd", methods=["GET"])
def get_motd() -> Dict[str, str]:
    motd: Dict[str, str] = helpers.read_json_file(
        os.path.join(static_directory, "motd.json")
    )
    motd_status: bool = bool(motd["enabled"])

    if motd_status:
        return motd
    else:
        return {
            "status": "disabled",
            "message": "MOTD is currently disabled. Check back later for updates.",
        }


@app.route("/api/storage", methods=["GET"])
def get_space_usage() -> Response:
    current_drive: str = psutil.disk_partitions()[0].device

    used_storage_bytes: int = psutil.disk_usage(current_drive).used
    total_storage_bytes: int = psutil.disk_usage(current_drive).total

    result = {
        "spaceUsed": helpers.format_size(used_storage_bytes),
        "spaceTotal": helpers.format_size(total_storage_bytes),
    }
    return jsonify(result)


@app.route("/api/list/<path:path>", methods=["GET"])
def list_files_json(path: str):
    full_path = os.path.join(static_directory, path)
    if os.path.isdir(full_path):
        files = os.listdir(full_path)
        file_data = []
        for file in files:
            file_path = os.path.join(full_path, file)
            is_folder = os.path.isdir(file_path)
            size = os.path.getsize(file_path)
            size_str = helpers.format_size(size)
            if is_folder:
                size_str = "—"
            modified_time = os.path.getmtime(file_path)
            modified_datetime = datetime.fromtimestamp(modified_time)
            icon = helpers.get_file_icon(file, is_folder)

            link_path = os.path.join(path, file).replace(os.path.sep, "/")

            file_data.append(
                {
                    "name": file,
                    "location": link_path,
                    "size": size_str,
                    "modified": modified_datetime,
                    "icon": icon,
                }
            )
        return {"files": file_data}
    else:
        abort(404)


@app.route("/api/update/<path:path>", methods=["POST"])
def update_file(path: str) -> Response:
    data = request.files.get("file")

    if data is None:
        abort(400, "No file uploaded")

    file_path: str = os.path.normpath(os.path.join(static_directory, path))

    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        abort(404)

    data.save(file_path)

    return jsonify({"message": "File updated successfully"})


@app.route("/api/upload/<path:directory>", methods=["POST"])
@app.route("/api/upload/<path:directory>/<path:subdirectory>", methods=["POST"])
def upload_file(directory="", subdirectory=""):
    file_path: str = ""
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        uploaded_file = request.files["file"]

        if uploaded_file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        if subdirectory:
            target_directory = os.path.join(static_directory, directory, subdirectory)
        else:
            target_directory = os.path.join(static_directory, directory)

        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        if uploaded_file.filename:
            # Use secure_filename to ensure the filename is safe
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(target_directory, filename)

        # Get 'overwrite' parameter from request
        overwrite = request.args.get("overwrite", "").lower() == "true"

        if os.path.exists(file_path) and not overwrite:
            return (
                jsonify(
                    {
                        "error": "File already exists. ",
                        "tip": "Include ?overwrite=true in the request.",
                    }
                ),
                409,
            )

        uploaded_file.save(file_path)

        if os.path.exists(file_path) and overwrite:
            return jsonify({"message": "File overwritten successfully"}), 200
        else:
            return jsonify({"message": "File uploaded successfully"}), 201

    except FileNotFoundError:
        return jsonify({"error": "Target directory not found"}), 500

    except PermissionError:
        return jsonify({"error": "Permission denied"}), 500

    except Exception as error:
        return jsonify({"error": str(error)}), 500
