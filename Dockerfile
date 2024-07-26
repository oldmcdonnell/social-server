# Use a specific Python version as the base image
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

# Set the working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Copy project files to the working directory
COPY . /code

# Set environment variable for secret key (or use Fly.io secrets)
ENV SECRET_KEY="g99bGSomwCJbSSuDbcEiqmhrUrRJV6lqwGquvbKI7LRp3LBem2"

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "project_social.wsgi:application"]
