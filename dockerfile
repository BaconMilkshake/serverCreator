FROM python

WORKDIR /enviroment/
RUN apt-get update \
    && apt-get install -y docker.io
CMD ["python", "main.py"]