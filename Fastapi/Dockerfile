# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /todo

# Copy the current directory contents into the container at /app 
ADD . /todo

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]