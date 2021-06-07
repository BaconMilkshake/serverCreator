import sys
from typing import Collection
import boto3


client = boto3.client('ec2')

runningWaiter = client.get_waiter('instance_running')

def create(spec): #returns instance id
    
    instance = client.run_instances(
    ImageId='ami-0cf6f5c8a62fa5da6',
    InstanceType=spec,  
    UserData=''' #! /bin/sh
    yum update -y
    amazon-linux-extras install docker
    service docker start
    usermod -a -G docker ec2-user
    chkconfig docker on 

    curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    logout
    ''',
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=[
        'sg-057edab7ecd374bee',
    ],
    KeyName='defaultec2'
    )
    return instance["Instances"][0]["InstanceId"]

def wait_until_running(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    instance.wait_until_running()
    return None

def get_public_ip(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    return instance.public_ip_address
    #ec2_client = boto3.client("ec2", region_name="us-west-2")
    #reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    #for reservation in reservations:
    #    for instance in reservation['Instances']:
    #        return(instance.get("PublicIpAddress"))

def reboot_instance(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    instance.reboot() 