import json
from os import getenv
from pprint import pprint
import argparse
import boto3
import botocore.exceptions
from botocore.config import Config

AWS_REGION = getenv("AWS_REGION", "us-east-1")
custom_config = Config(region_name=AWS_REGION)
s3_client=boto3.client("s3", region_name=AWS_REGION)

def policy_exists(bucket_name):
    try:
        s3_client.get_bucket_policy(Bucket=bucket_name)
        return True
    except botocore.exceptions.ClientError as ex:
        return False
def generate_policy(name):
    Policy= {
        "Version" : "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": [
                    f"arn:aws:s3:::{name}/test",
                    f"arn:aws:s3:::{name}/dev"
                ]

            }
        ]


    }
    return json.dumps(Policy)


def check_policy_And_Create(bucket_name):
    if not policy_exists(bucket_name):
        try:
            s3_client.put_bucket_policy(Bucket=bucket_name, Policy=generate_policy(bucket_name))
            print("policy generated successfully")
        except botocore.exceptions.ClientError as ex:
            print(ex)

    else:
        print("policy already exists")


def main():
    check_policy_And_Create("btutest2")

if __name__ == '__main__':
    main()