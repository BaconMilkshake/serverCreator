import sys
from typing import Collection
import boto3


client = boto3.client('ec2')

runningWaiter = client.get_waiter('instance_running')
def create(spec):
    return client.run_instances(
    ImageId='ami-0cf6f5c8a62fa5da6',
    InstanceType=spec,  
    UserData=''' #! /bin/sh
yum update -y
amazon-linux-extras install docker
service docker start
usermod -a -G docker ec2-user
chkconfig docker on ''',
    MinCount=1,
    MaxCount=1
)
