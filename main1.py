import boto3
from botocore.client import Config
Access_key_ID = "AKIA5KCP4HJIQDGYY7EM"
Access_secret_key = "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"
Bucket_name = "newbucketvideos"


s3 = boto3.resource(
    service_name='s3',

    aws_access_key_id=Access_key_ID,
    aws_secret_access_key=Access_secret_key
)

#for bucket in s3.buckets.all():
#print(bucket.name)

s3.Bucket(Bucket_name).upload_file("05_22_2021_212058.mp4","05_22_2021_212058.mp4")

'''
import boto3
from botocore.client import Config

Access_key_ID = "AKIA5KCP4HJIQDGYY7EM"
Access_secret_key = "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"
Bucket_name = "newbucketvideos"
data = open('C:\\Users\\joshi\\PycharmProjects\\first\\main.py',"rb")

s3 = boto3.resource('s3',aws_access_key_id=Access_key_ID,aws_secret_access_key=Access_secret_key,
                    config=Config(signature_version='s3v4'))

s3.Bucket(Bucket_name).put_object(key ='main.py',Body = data )
print("successful")



import boto
from boto.s3.key import Key

keyId = 'AKIA5KCP4HJIQDGYY7EM'
sKeyId='fVD3yyeJzNrKGZwk/LTTYOvJ3wWVmhbzPSQjRv+g'
bucketName='newbucketvideos'

conn = boto.connect_s3(keyId,sKeyId)
bucket = conn.get_bucket(bucketName)
print(bucket)
#for key in bucket.list():
 #   print(">>>>>"+key.name)
'''