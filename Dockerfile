# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV DB_NAME db_name
ENV DB_USER db_user
ENV DB_HOST db_host

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
