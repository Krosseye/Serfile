# Use official Python runtime as parent image
FROM python:3.11.5-slim

# Set working directory to /app
WORKDIR /app

# Copy current directory contents into container at /app
COPY . /app

# Install packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available outside container
EXPOSE 8080

# Run app.py when container launches
CMD ["python", "run.py"]
