FROM python:3.11-slim

# Set the working directory in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE  5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]