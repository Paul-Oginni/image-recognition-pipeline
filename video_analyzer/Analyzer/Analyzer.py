#!/usr/bin/env python3

import requests
import analyzer_config as config
import boto3

class Analyzer():
    
    def __init__(self):
        self.ClientRequestToken = config.analyzer_config["ClientRequestToken"]
        self.JobTag = config.analyzer_config["JobTag"]
        self.MinConfidence = config.analyzer_config["MinConfidence"]
        self.NotificationChannel = config.analyzer_config["NotificationChannel"]["RoleArn"]
        self.SNSTopicArn = config.analyzer_config["NotificationChannel"]["SNSTopicArn"]
        self.Bucket = config.analyzer_config["Video"]["S3Object"]["Bucket"]
        self.Name = config.analyzer_config["Video"]["S3Object"]["Name"]
        self.Video = config.analyzer_config["Video"]
        


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
        client = boto3.client('rekognition')
        
        response = client.start_label_detection(
            Video={
                'S3Object': {
                    'Bucket': 'image-recognition-analyzer-bucket',
                    'Name': 'v2.MOV',
                    'Version': 'TZGKcPcMELa_jXhb58p6P3YSpfPsPhYV'
                }
            },
            ClientRequestToken = 'job9crt',
            MinConfidence = 1.0,
            NotificationChannel = {
                'SNSTopicArn':   'arn:aws:sns:us-west-2:219780720175:VideoAnalyzerTopic',
                'RoleArn': 'arn:aws:iam::219780720175:role/rekognition_role'
            },
            JobTag='job9crt'
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


analyzer = Analyzer()
# analyzer.make_request()
analyzer.get_job_results("<jobid>")