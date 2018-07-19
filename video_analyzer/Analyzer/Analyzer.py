#!/usr/bin/env python3

import requests
import analyzer_config as config
import boto3
import datetime as dt

class Analyzer():
    
    def __init__(self):
        self.ClientRequestToken = config.analyzer_config["ClientRequestToken"]
        self.JobTag = config.analyzer_config["JobTag"]
        self.MinConfidence = config.analyzer_config["MinConfidence"]
        self.NotificationChannel = config.analyzer_config["NotificationChannel"]["RoleArn"]
        self.SNSTopicArn = config.analyzer_config["NotificationChannel"]["SNSTopicArn"]
        self.SNSRoleArn = config.analyzer_config["NotificationChannel"]["RoleArn"]
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
        client = boto3.client('rekognition', region_name='us-west-2')
        
        response = client.start_label_detection(
            Video={
                'S3Object': {
                    'Bucket': self.Bucket,
                    'Name': self.Name
                }
            },
            ClientRequestToken = self.ClientRequestToken,
            MinConfidence = 1.0,
            NotificationChannel = {
                'SNSTopicArn': self.SNSTopicArn,
                'RoleArn': self.SNSRoleArn
            },
            JobTag = self.JobTag
        )
        print(response)       

    def get_job_results(self, jobId):
        client = boto3.client('rekognition', region_name='us-west-2')        
        response = client.get_label_detection(
            JobId=jobId,
            MaxResults=100
        )
        print(response)


analyzer = Analyzer()
#analyzer.make_request()
analyzer.get_job_results("3ce7cc43a9542241309aad4732b141398f91d307cb44ba46ce52dca542fa80ca")
