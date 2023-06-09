FROM ubuntu:latest
ADD test_mdns.py /app
ADD index.html /app
ADD script.js /app
RUN apt-get update && apt-get install -y python3
RUN apt-get update && apt-get install -y python3-flask
RUN apt-get update && apt-get install -y python3-zeroconf
RUN apt-get update && apt-get install -y python3-flask-cors
EXPOSE 5000
CMD python3,test_mdns.py
