# 🌊 Serfile - Simple File Hosting Web Server

Serfile is a lightweight web server designed for simple file hosting and browsing. It provides a minimalist web-based user interface and API for navigating folders and accessing files.

## Features

- 🚀 Easy installation and setup.
- 📁 Web-based UI for browsing and managing files.
- ✏️ Integrated editor for editing code and text files.
- ⚙️ Two deployment options: Python environment or Docker.
- 📜 MIT licensed - use, modify, and distribute with ease.

## Installation and Usage

### 🐍 Python Environment

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
   python run.py
   ```

6. Access the Serfile UI by opening a web browser and navigating to `http://localhost:8080` or your specified port.

### 🐳 Docker Compose

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

### 🔧 Server (`config.json`)

Modify the `config.json` file to customize settings.

```json
{
  "port": 8080,
  "host": "0.0.0.0",
  "title": "Serfile",
  "rootName": "home",
  "environment": "prod"
}
```

Environment options are `prod`/`production` or `dev`/`develop`

### 🐋 Docker Compose (`docker-compose.yml`)

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
      - /path/to/serve:/app/app/static/home # Make sure to modify `/path/to/serve`
    restart: unless-stopped
```

## Preview

![Preview screenshot of the Serfile Web-UI](https://i.ibb.co/CnZj4z1/01-Serfile-0-10-4.png)

## Disclaimer

### 🚧 Please be aware that Serfile is currently in its alpha stages

- **Frequent Updates and Changes:** The Serfile project is actively under development, there will be frequent updates and changes to its codebase, features, and functionality.
- **Incomplete Features:** Some features may not work as expected or may be incomplete. We are continuously working to improve and expand the capabilities of Serfile.
- **Everything is Subject to Change:** Expect that everything, including APIs, configurations, and user interfaces, is subject to change as we refine and enhance the project.
- **Not Recommended for Production:** At this stage, Serfile is not recommended for production use. It is intended primarily for testing, experimentation, and feedback purposes. Use in a production environment is discouraged.

## License

📃 Serfile is distributed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

💬 Feel free to contribute, report issues, or suggest improvements by creating a pull request or opening an issue on the [GitHub repository](https://github.com/Krosseye/Serfile). Your feedback is greatly appreciated!
