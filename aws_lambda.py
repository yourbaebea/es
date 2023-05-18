import boto3
import json
from django.conf import settings


def hello():
    lambda_client = boto3.client('lambda', region_name=settings.AWS_REGION)
    response = lambda_client.invoke(
        FunctionName='helloWorld',
        InvocationType='RequestResponse',
        Payload='{}'  # Pass any input data to the Lambda function as a JSON string
    )
    result = response['Payload'].read()
    print("result")
    print(result)

def findUserByUsername():
    lambda_client = boto3.client('lambda', region_name=settings.AWS_REGION)
    response = lambda_client.invoke(
        FunctionName='findUserByUsername',
        InvocationType='RequestResponse',
        Payload='{"username":"ana"}'  # Pass any input data to the Lambda function as a JSON string
    )
    result = response['Payload'].read().decode('utf-8')
    result_json = json.loads(result)
    print("result")
    print(result_json)
