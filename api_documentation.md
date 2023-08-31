# :ocean: Serfile API Documentation

Welcome to the Serfile API documentation. This documentation provides an overview of the endpoints and functionality offered by the Serfile API for navigating folders and accessing files.

## Base URL

The base URL for the Serfile API is `http://localhost:8080/api`.

## Get Version

Returns the version of the Serfile app.

- Endpoint: `/version`
- Method: GET
- Example: Retrieve the version using curl

```bash
curl http://localhost:8080/api/version
```

Response:

```json
{
  "version": "1.0.0"
}
```

## Get Licenses

Returns the names and licenses of Serfile's third-party assets.

- Endpoint: /licenses
- Method: GET
- Example: Retrieve asset licenses using curl

```bash
curl http://localhost:8080/api/licenses
```

Response:

```json
{
  "assets": [
    {
      "license": "SIL Open Font License, version 1.1",
      "name": "Noto Color Emoji",
      "version": "Unicode 15.0"
    },
    {
      "license": "SIL Open Font License, version 1.1",
      "name": "Inter Font",
      "version": "v3.19"
    }
  ]
}
```

## List Directory

Lists the contents of a specified directory along with information about each file.

- Endpoint: /list/`{directory}`
- Method: GET
- Parameters:
  - `directory` (string): The path of the directory to list.
- Example: List contents of a directory using curl

```bash
curl http://localhost:8080/api/list/root/myfolder
```

Response:

```json
{
  "files": [
    {
      "icon": "📝",
      "location": "root/TextFile.txt",
      "modified": "Sun, 27 Aug 2023 17:49:00 GMT",
      "name": "TextFile.txt",
      "size": "47.00 Bytes"
    }
  ]
}
```

## Upload File

Uploads a file to the specified directory. The overwrite query parameter allows overwriting an existing file.

- Endpoint: /upload/`{directory}`
- Method: POST
- Parameters:
  - `directory` (string): The path of the directory to upload the file to.
- Query Parameter:
  - overwrite (boolean, optional): If true, overwrites the file if it already exists.
- Example: Upload a file to a directory using curl

```bash
curl -X POST -F "file=@/path/to/file.txt" http://localhost:8080/api/upload/root/myfolder?overwrite=true
```

Response:

```json
{
  "message": "File uploaded successfully."
}
```

---

Please note that the above examples use curl to demonstrate how to interact with the Serfile API. You can use other HTTP clients or programming languages to achieve the same results.
