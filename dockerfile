FROM python

WORKDIR /tempSetup/
RUN apt-get update \
    && apt-get install -y docker.io \
    && apt-get install -y docker-compose

#RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
#    && apt-get install -y nodejs

#RUN npm install -g aws-cdk
#RUN python -m pip install aws-cdk.aws-s3 aws-cdk.aws-ec2
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR /root/.aws/
COPY ./.aws/ ./
COPY ./id_rsa /root/.ssh/
WORKDIR /root/.ssh/
RUN chmod 400 ./id_rsa
WORKDIR /enviroment/
CMD ["python", "main.py"]