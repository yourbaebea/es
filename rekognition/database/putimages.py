import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image7.jpg','Alexa Demie'),
      ('image8.jpg','Hunter Schafer')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('pharmacy-rekognition','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
    print("img inserted")


print("all updates done")