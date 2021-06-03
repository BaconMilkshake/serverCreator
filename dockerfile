FROM ubuntu

WORKDIR /enviroment/
RUN apt-get update \
    && apt-get install -y docker.io \
    && apt-get install -y python3.9.4
CMD ["python", "main.py"]