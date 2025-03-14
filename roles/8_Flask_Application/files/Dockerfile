FROM python:3.8-slim

# Install dependencies
RUN pip install --upgrade pip
RUN pip install Flask==2.0.2 Werkzeug==2.0.2

# Add your app code
COPY . /app
WORKDIR /app

# Expose the port Flask will run on
EXPOSE 5001

# Run the Flask app
CMD ["python3", "app.py"]
# Use Python 3.8 as the base image
