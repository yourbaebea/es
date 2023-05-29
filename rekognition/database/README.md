# How to add new images to the s3/dynamic database

- Add image to s3
```
python .\putimages.py
```

- add image in db from lambda function
```
open lambda function facerecognition
test > configure test
"key": "index/image6.jpg" (change here the image u want to add)
```
NOTE: this only works one at a time idk how to fix it


based on https://github.com/teja156/amazon-rekognition-example