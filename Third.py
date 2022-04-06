from os import getenv
from pprint import pprint

import boto3
import botocore.exceptions
from botocore.config import Config

AWS_REGION = getenv("AWS_REGION", "us-east-1")
custom_config = Config(region_name=AWS_REGION)
s3_client=boto3.client("s3", region_name=AWS_REGION)

def bucket_exists(name):
    try:
        response = s3_client.head_bucket(Bucket=name)
    except botocore.exceptions.ClientError as ex:
        return False

    status_code=response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code==200:
        return True
    return False


def check_and_delete(name):
    if bucket_exists(name):
        try:
            s3_client.delete_bucket(Bucket=name)
            print(f"Bucket '{name}' deleted successfully")
        except botocore.exceptions.ClientError as ex:
            print(ex)
    else:
        print("bucket doesnot exists")

def main():
    check_and_delete("btutest1")

if __name__ == '__main__':
    main()