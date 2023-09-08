import os

from app import about, helpers
from flask import Flask

app = Flask(__name__)

# Get directory of current script
script_directory = os.path.dirname(os.path.abspath(__file__))
# Navigate up one directory
parent_directory = os.path.dirname(script_directory)
# Construct full path to config
config_file_path = os.path.join(parent_directory, "config.json")
# Serve files from "static" directory
static_directory = os.path.join(os.path.dirname(__file__), "static")

# Define constants
APP_VERSION = about.app_version
LICENSES = about.licenses
CONFIG = helpers.read_json_file(config_file_path)

# Create root_directory if it doesn't exist
root_directory_name = CONFIG["root_directory"]
root_directory_path = os.path.join(static_directory, root_directory_name)
if not os.path.exists(root_directory_path):
    os.makedirs(root_directory_path)

# Minify JS and CSS files
if CONFIG['environment'] == 'prod' or CONFIG['environment'] == 'production':
    helpers.minify_files(os.path.join(app.root_path, 'static', 'assets', 'js'), '.js')
    helpers.minify_files(os.path.join(app.root_path, 'static', 'assets', 'css'),'.css')

from app import routes
