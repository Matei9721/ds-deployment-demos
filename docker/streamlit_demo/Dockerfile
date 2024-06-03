# Use an official Python runtime as a parent image
FROM python:3.10.14-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to Docker so we can install the packages
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt, this creates a check-point.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents (actual app) into the container at /app
COPY . /app

# Expose the port streamlit runs on
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "Streamlit_app.py"]