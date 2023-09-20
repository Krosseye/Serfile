# ! Dockerfile
# * Created by Krosseye
# * Pulling from Python slim image

FROM python:3.11.5-slim

LABEL maintainer="Krosseye"

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Run run.py when container launches
CMD ["python", "run.py"]
