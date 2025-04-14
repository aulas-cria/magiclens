# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Install Poetry
RUN pip install poetry

# Copy the project files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
