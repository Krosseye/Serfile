"""This is the initialization module for the application."""

import os
from typing import Dict, List

from app import about, helpers
from flask import Flask

app = Flask(__name__)

# Get directory of current script
script_directory: str = os.path.dirname(os.path.abspath(__file__))
# Navigate up one directory
parent_directory: str = os.path.dirname(script_directory)
# Construct full path to config
config_file_path: str = os.path.join(parent_directory, "config.json")
# Serve files from "static" directory
static_directory: str = os.path.join(os.path.dirname(__file__), "static")

# Define constants
SETUP_FINISHED: bool = False
APP_VERSION: str = about.APP_VERSION
LICENSES: Dict[str, List[about.Asset]] = about.licenses
CONFIG: Dict[str, str] = helpers.read_json_file(config_file_path)

if CONFIG is not None:
    # Create root_directory if it doesn't exist
    root_directory_name: str = CONFIG["rootName"]
    root_directory_path: str = os.path.join(static_directory, root_directory_name)
    if not os.path.exists(root_directory_path):
        os.makedirs(root_directory_path)

    # Minify and bundle JS and CSS files
    if CONFIG["environment"] in ("prod", "production"):
        assets_directory: str = os.path.join(app.root_path, "static", "assets")

        helpers.minify_and_bundle_files(
            os.path.join(assets_directory, "js"), "scripts", ".js"
        )
        helpers.minify_and_bundle_files(
            os.path.join(assets_directory, "css"), "styles", ".css"
        )

SETUP_FINISHED = True

if SETUP_FINISHED is True:
    from app import routes
