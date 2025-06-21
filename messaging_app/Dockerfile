FROM python:3.10

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /messaging_app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy .env file (should be in same directory now)
COPY .env .

# Copy the rest of the application code into the container
COPY . .

# Copy .env file
COPY ../.env .

# Add a non-root user to run the application:
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /messaging_app && \
    chmod -R 755 /messaging_app

# Switch to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application (migrations will run via docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]