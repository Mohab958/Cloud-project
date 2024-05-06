FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY server.py /app
EXPOSE 5000
CMD ["python", "server.py"]  # Start the backend server on container startup