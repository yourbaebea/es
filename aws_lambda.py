import boto3
import json
from django.conf import settings

def lambda_start_order(p):
    print("inside lambda start order")
    #payload_bytes = json.dumps({"name":"name","age":"age"}).encode('utf-8')
    lambda_client = boto3.client('lambda', region_name=settings.AWS_REGION)
    response = lambda_client.invoke(
        FunctionName='setOrder',
        InvocationType='RequestResponse',
        Payload=json.dumps(p)
    )

    lambda_response = response['Payload'].read().decode('utf-8')
    lambda_data = json.loads(lambda_response)
    print(lambda_data)
    body = lambda_data['body']
    print(body)
    print("back to call")
    return body


def lambda_update_order(id,type):
    print("inside lambda update order")
    lambda_client = boto3.client('lambda', region_name=settings.AWS_REGION)
    response = lambda_client.invoke(
        FunctionName=type,
        InvocationType='RequestResponse',
        Payload=json.dumps({'id': id})
    )
    lambda_response = response['Payload'].read().decode('utf-8')
    lambda_data = json.loads(lambda_response)
    print(lambda_data)
    body = lambda_data['body']
    print(body)
    print("back to call")
    return body


def rekognition(image_binary):
    rekognition = boto3.client('rekognition', region_name=settings.AWS_REGION)
    dynamodb = boto3.client('dynamodb', region_name=settings.AWS_REGION)
    name= None

    print("inside rekognition")
    
    response = rekognition.search_faces_by_image(
            CollectionId='pharmacy_rekognition',
            Image={'Bytes':image_binary}                                       
            )

    found = False
    for match in response['FaceMatches']:
        print (match['Face']['FaceId'],match['Face']['Confidence'])
            
        face = dynamodb.get_item(
            TableName='facerecognition',  
            Key={'RekognitionId': {'S': match['Face']['FaceId']}}
            )
        
        if 'Item' in face:
            print ("Found Person: ",face['Item']['FullName']['S'])
            name= face['Item']['FullName']['S']
            found = True

    if not found:
        print("Person cannot be recognized")

    return name


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
    return result

