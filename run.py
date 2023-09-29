"""This module will start running the application."""

import logging

from app import CONFIG, app
from waitress import serve


def start_server() -> None:
    """
    Starts the server based on the configuration file.
    """
    if CONFIG is not None:
        config_env: str = CONFIG.get("environment", "").lower()
        port: str = CONFIG["port"]
        host: str = CONFIG["host"]
        title: str = CONFIG["title"]

        if config_env in ("production", "prod"):
            logging.info("Serving on http://%s:%s", host, port)
            serve(app, host=host, port=port, ident=title)
        elif config_env in ("development", "dev"):
            app.run(host=host, port=int(port), debug=True)
        else:
            logging.error("Invalid environment in config: '%s'", config_env)
    else:
        logging.error("No `config.json` available")
        return


if __name__ == "__main__":
    start_server()
