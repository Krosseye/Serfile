from app import CONFIG, app
from waitress import serve


def start_server():
    config_env = CONFIG['environment']

    if config_env == 'prod' or config_env == 'production':
        print(f"Serving on http://{CONFIG['host']}:{CONFIG['port']}")
        serve(app, host=CONFIG["host"], port=CONFIG["port"], ident="Serfile")
    elif config_env == 'dev' or config_env == 'development':
        app.run(host=CONFIG["host"], port=CONFIG["port"], debug=True)
    else:
        print(" ! Error serving application:")
        print(f" * Invalid environment in config '{config_env}'")


if __name__ == "__main__":
    start_server()
