# Serfile - Simple File Hosting Web Server

Serfile is a lightweight web server designed for simple file hosting and browsing. It provides an intuitive web-based user interface for navigating and managing files within a specified directory.

## Features

- Easy installation and setup.
- Web-based UI for browsing and managing files.
- Two deployment options: Python environment or Docker.
- MIT licensed - use, modify, and distribute with ease.

## Installation and Usage

### Python Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/serfile.git
   cd serfile
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

### Docker Compose

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/serfile.git
   cd serfile
   ```

2. Configure the server by editing the `docker-compose.yml` file as needed.
3. Build and start the Docker containers:

   ```bash
   docker-compose up -d
   ```

4. Access the Serfile UI by opening a web browser and navigating to `http://localhost:8080` or your specified port.

**Note:** When using Docker Compose, avoid modifying the `config.json` file directly. Instead, configure the application using the `docker-compose.yml` file.

## Configuration

### Python Environment (`config.json`)

Modify the `config.json` file to customize settings.

```json
{
  "port": 8080,
  "host": "0.0.0.0",
  "title": "Serfile",
  "root_directory": "root"
}
```

### Docker Compose (`docker-compose.yml`)

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
      - path/to/serve:/app/static/root
    restart: unless-stopped
```

Make sure to modify `path/to/serve`.

## License

Serfile is distributed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

Feel free to contribute, report issues, or suggest improvements by creating a pull request or opening an issue on the [GitHub repository](https://github.com/yourusername/serfile). Your feedback is greatly appreciated!
