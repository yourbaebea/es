from django.http import HttpResponse, JsonResponse
import datetime
import boto3
import json


client = boto3.client('stepfunctions', region_name='us-east-1')

def step_start_exe(request):
    try:
        #print("chega aqui")
        response = client.start_execution(
            stateMachineArn='arn:aws:states:us-east-1:084715651869:stateMachine:Project2',
            name=('machine' + str(datetime.datetime.now())).replace(" ", "--").replace(":", "").replace(".", ""),
            input=json.dumps('paracetamol')
        )

        #print(response)
        print("Start State Machine")
        return "Start State Machine: success"

    except:
        return "Start State Machine: error"

   