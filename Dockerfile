FROM ubuntu:latest
WORKDIR /app
COPY . /app
RUN ls /app
RUN apt-get update && apt-get install -y python3
RUN apt-get update && apt-get install -y python3-pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD python3 /app/test_mdns.py
