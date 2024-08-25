# Stage 1: Build stage
FROM python:3.11 AS builder

# Set environment variables to ensure Python outputs everything to stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install build dependencies (if needed)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Install BusyBox
RUN apt-get update && apt-get install -y busybox curl


# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main.py"]
