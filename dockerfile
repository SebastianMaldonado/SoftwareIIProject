# Use an official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app/softwarebackend

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port for Django (default is 8000)
EXPOSE 8000

# Command to run the Django development server (update with WSGI server in production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
