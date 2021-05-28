import RPi.GPIO as GPIO
import time
import os
from picamera  import PiCamera
from datetime import datetime
import boto3



Access_key_ID = "AKIA5KCP4HJIQDGYY7EM"
Access_secret_key = "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"
Bucket_name = "newbucketvideos"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)


def current_date_time():
    now = datetime.now()
    return now.strftime("%m_%d_%Y_%H_%M_%S")

def record_video(current_date_time):
    camera = PiCamera()
    camera.resolution=(640,480)
    camera.rotation = 180
    camera.start_preview()
    camera.start_recording(f'{current_date_time}.h264')
    time.sleep(10)
    camera.stop_recording()
    camera.stop_preview()
    camera.close()
    

def get_cwd(k):
    cwd = os.getcwd()
    return f'{cwd}/{k}.h264'


def upload_on_cloud(path,name):
    s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=Access_key_ID,
    aws_secret_access_key=Access_secret_key)
    s3.Bucket(Bucket_name).upload_file(path,name)
    print("Done")
    

while True:
    i = GPIO.input(11)
    if i == 1:
        #print("Motion detected")
        k = current_date_time()
        path = get_cwd(k)
        record_video(k)
        upload_on_cloud(path,f'{k}.h264')
        
    else:
        #print("No Motion Detected")
        time.sleep(1)
    





