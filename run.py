from app.app import CONFIG, app
from waitress import serve

if __name__ == "__main__":
    if CONFIG['environment'] == 'prod' or CONFIG['environment'] == 'production':
        print(f"Serving on http://{CONFIG['host']}:{CONFIG['port']}")
        serve(app, host=CONFIG["host"], port=CONFIG["port"], ident="Serfile")

    elif CONFIG['environment'] == 'dev' or CONFIG['environment'] == 'development':
        app.run(host=CONFIG["host"], port=CONFIG["port"], debug=True)
    else:
        print(" ! Error serving application:")
        print(f" * Invalid environment in config '{CONFIG['environment']}'")
