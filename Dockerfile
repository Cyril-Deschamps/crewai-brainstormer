# Dockerfile
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

RUN crewai install

CMD ["crewai", "run"]