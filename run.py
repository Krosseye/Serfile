from app.app import CONFIG, app
from waitress import serve

if __name__ == "__main__":
    print(f"Serving on http://{CONFIG['host']}:{CONFIG['port']}")
    serve(app, host=CONFIG["host"], port=CONFIG["port"])
