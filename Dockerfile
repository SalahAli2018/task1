# Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt .


RUN pip install virtualenv

# Create a virtual environment and activate it
RUN virtualenv venv && . /app/venv/bin/activate

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY tests/ ./tests

RUN ["pytest"]
# Set the entry point for the CMD
CMD ["bash"]