FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

# Create a virtual environment and install packages
RUN python -m venv venv && \
    . /app/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

# Set the entry point for the CMD
# CMD ["bash"]
