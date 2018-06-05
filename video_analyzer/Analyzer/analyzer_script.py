#!/usr/bin/env python3

import requests
import analyzer_config as config
import boto3


def make_request(self):

    client = boto3.client('rekognition')
    
    response = client.start_label_detection(
        Video={
            'S3Object': {
                'Bucket': 'image-recognition-analyzer-bucket',
                'Name': 'v2.MOV',
                'Version': 'TZGKcPcMELa_jXhb58p6P3YSpfPsPhYV'
            }
        },
        ClientRequestToken = 'job7crt',
        MinConfidence = 1.0,
        NotificationChannel = {
            'SNSTopicArn':   'arn:aws:sns:us-west-2:219780720175:VideoAnalyzerTopic',
            'RoleArn': 'arn:aws:iam::219780720175:role/rekognition_role'
        },
        JobTag='job7crt'
    )      

    print(response)

def get_job_results(self, jobId):
    client = boto3.client('rekognition')        
    response = client.get_label_detection(
        JobId='job6crt',
        MaxResults=123
        # NextToken='string',
        # SortBy='NAME'|'TIMESTAMP'
    )

make_request()
# analyzer.get_job_results("job5crt")