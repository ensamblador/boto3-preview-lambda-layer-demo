import boto3
def lambda_handler(event, context):
    print(boto3.__version__)

    cases = boto3.client('connectcases')

    print(cases)