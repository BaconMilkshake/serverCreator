import sys
import boto3


ec2 = boto3.resource('ec2')

def create(spec):
    return ec2.create_instances(
     ImageId='ami-0cf6f5c8a62fa5da6',
     MinCount=1,
     MaxCount=1,
     InstanceType=spec,
     #KeyName='ec2-keypair'
    )