# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY github-repo-scrape.py /app/github-repo-scrape.py
COPY requirements.txt /app/requirements.txt

# Install project dependencies
RUN pip install -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "github-repo-scrape.py"]

