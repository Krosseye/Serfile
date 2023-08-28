from app.app import app, config
from waitress import serve

if __name__ == "__main__":
    print(f"Serving on http://{config['host']}:{config['port']}")
    serve(app, host=config["host"], port=config["port"])
