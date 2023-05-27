import boto3, json

client = boto3.client('stepfunctions', region_name='us-east-1')

print("linha5")
while True:
    responde1 = client.get_activity_task(
        activityArn='arn:aws:states:us-east-1:084715651869:activity:Test0',
        workerName='Test0'
    )

    print(responde1)

    responde2 = client.send_task_success(
        taskToken=json.dumps(responde1['taskToken']),
        output='30'
    )

