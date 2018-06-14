#!/usr/bin/env python3

import requests
import tagger_config as config
import boto3

class Tagger():
    
    def __init__(self):
        self.ClientRequestToken = config.tagger_config["ClientRequestToken"]
        self.JobTag = config.tagger_config["JobTag"]
        self.MinConfidence = config.tagger_config["MinConfidence"]
        self.NotificationChannel = config.tagger_config["NotificationChannel"]["RoleArn"]
        self.SNSTopicArn = config.tagger_config["NotificationChannel"]["SNSTopicArn"]
        self.Bucket = config.tagger_config["Video"]["S3Object"]["Bucket"]
        self.Name = config.tagger_config["Video"]["S3Object"]["Name"]
        self.Video = config.tagger_config["Video"]
        


    def test_print(self):
        print(self.ClientRequestToken)
        print(self.JobTag)
        print(self.MinConfidence)
        print(self.NotificationChannel)
        print(self.SNSTopicArn)
        print(self.Bucket)
        print(self.Name)

    def make_request(self):
        data = {
            "ClientRequestToken": self.ClientRequestToken,
            "JobTag": self.JobTag,
            "MinConfidence": self.MinConfidence,
            "NotificationChannel": self.NotificationChannel,
            "SNSTopicArn": self.SNSTopicArn,
            "Bucket": self.Bucket,
            "Name": self.Name
        }

    # def boto_client(self):
        # initialize client
        client = boto3.client('rekognition', region_name='us-west-2')
        
        response = client.start_label_detection(
            Video={
                'S3Object': {
                    'Bucket': 'image-recognition-analyzer-bucket',
                    'Name': 'v1.MOV'
                    #'Version': 'TZGKcPcMELa_jXhb58p6P3YSpfPsPhYV'
                }
            },
            ClientRequestToken = 'job16crt',
            MinConfidence = 1.0,
            NotificationChannel = {
                'SNSTopicArn':   'arn:aws:sns:us-west-2:219780720175:VideoAnalyzerTopic',
                'RoleArn': 'arn:aws:iam::219780720175:role/rekognition_role'
            },
            JobTag='job16crt'
        )
        print(response)       

    def get_job_results(self, jobId):
        client = boto3.client('rekognition')        
        response = client.get_label_detection(
            JobId=jobId,
            MaxResults=123
            # NextToken='string',
            # SortBy='NAME'|'TIMESTAMP'
        )
        print(response)


tagger = Tagger()
tagger.make_request()
#tagger.get_job_results("job12crt")
