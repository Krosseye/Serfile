
# Serfile :file_folder: - Simple File Hosting Web Server

Serfile is a lightweight web server designed for simple file hosting and browsing. It provides an intuitive web-based user interface for navigating and managing files within a specified directory.

## Features

- :rocket: Easy installation and setup.
- :file_folder: Web-based UI for browsing and managing files.
- :gear: Two deployment options: Python environment or Docker.
- :scroll: MIT licensed - use, modify, and distribute with ease.

## Installation and Usage

### :computer: Python Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/Krosseye/Serfile.git
   cd Serfile
   ```

2. Create a Python virtual environment and activate it:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the server by editing `config.json` as needed.
5. Run the application:

   ```bash
   python app.py
   ```

6. Access the Serfile UI by opening a web browser and navigating to `http://localhost:8080` or your specified port.

### :whale: Docker Compose

1. Clone the repository:

   ```bash
   git clone https://github.com/Krosseye/Serfile.git
   cd Serfile
   ```

2. Configure the server by editing the `docker-compose.yml` file as needed.
3. Build and start the Docker containers:

   ```bash
   docker-compose up -d
   ```

4. Access the Serfile UI by opening a web browser and navigating to `http://localhost:8080` or your specified port.

## Configuration

### :wrench: Python Environment (`config.json`)

Modify the `config.json` file to customize settings.

```json
{
  "port": 8080,
  "host": "0.0.0.0",
  "title": "Serfile",
  "root_directory": "root"
}
```

### :whale2: Docker Compose (`docker-compose.yml`)

Edit the `docker-compose.yml` file to adjust settings.

```yaml
version: "3"
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: serfile
    ports:
      - "8080:8080"
    volumes:
      - /path/to/serve:/app/static/root
    restart: unless-stopped
```

Make sure to modify `/path/to/serve`.

## License

:page_with_curl: Serfile is distributed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

:speech_balloon: Feel free to contribute, report issues, or suggest improvements by creating a pull request or opening an issue on the [GitHub repository](https://github.com/Krosseye/Serfile). Your feedback is greatly appreciated!
