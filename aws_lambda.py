import boto3
import botocore
import json

def lambda_start_order(p):
    print("inside lambda start order")
    try:
        #payload_bytes = json.dumps({"name":"name","age":"age"}).encode('utf-8')
        lambda_client = boto3.client('lambda', region_name='us-east-1')
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
        return True, body
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        error_aws= "AWS Token not updated, please refresh on https://awsacademy.instructure.com/courses/44430/modules/items/3817170 ."
        if error_code == 'ExpiredTokenException':
            print(error_aws)
            return False, error_aws
        else:
            print("An error occurred:", error_code)
            return False, error_code

def lambda_update_order(id,type):
    print("inside lambda update order")
    try:
        lambda_client = boto3.client('lambda', region_name='us-east-1')
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
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        print(error_code)
        return None

def rekognition(image_binary):
    try:
        rekognition = boto3.client('rekognition', region_name='us-east-1')
        dynamodb = boto3.client('dynamodb', region_name='us-east-1')
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
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        print(error_code)
        return None

def lambda_get_prescription(p):
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    response = lambda_client.invoke(
        FunctionName='getPrescription',
        InvocationType='RequestResponse',
        Payload=json.dumps(p)
    )
    result = response['Payload'].read()
    print("result")
    print(result)
    return result

