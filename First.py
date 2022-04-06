from os import getenv
from pprint import pprint

import boto3
import botocore.exceptions

AWS_REGION = getenv("AWS_REGION", "us-east-1")

s3_client=boto3.client("s3", region_name=AWS_REGION)


def bucket_exists(name):
    try:
        response = s3_client.head_bucket(Bucket=name)
    except botocore.exceptions.ClientError as ex:
        return False

    statusCode=response["ResponseMetadata"]["HTTPStatusCode"]
    if statusCode==200:
        return True
    return False

def createBucket(name):
    if not bucket_exists(name):
        try:
            s3_client.create_bucket(Bucket=name)
            print(f"Bucket '{name}' created successfully")
        except botocore.exceptions.ClientError as ex:
            print(ex)

    else:
        print(f"Bucket '{name}' already exists")


def main():
    bucket_name = "btutest1"
    createBucket(bucket_name)



if __name__ == '__main__':
    main()