import boto3
import json
from django.conf import settings


def hello():
    lambda_client = boto3.client('lambda', region_name=settings.AWS_REGION)
    response = lambda_client.invoke(
        FunctionName='helloWorld',
        InvocationType='RequestResponse',
        Payload=json.dumps({})
    )
    result = response['Payload'].read()
    print("result")
    print(result)

def lambda_get_prescription(p):
    lambda_client = boto3.client('lambda', region_name=settings.AWS_REGION)
    response = lambda_client.invoke(
        FunctionName='getPrescription',
        InvocationType='RequestResponse',
        Payload=json.dumps(p)
    )
    result = response['Payload'].read()
    print("result")
    print(result)
