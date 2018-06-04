
analyzer_config = {
    "ClientRequestToken": "job1crt",
    "JobTag": "job1jt",
    "MinConfidence": 1.0,
    "NotificationChannel": {
        "RoleArn": "arn:aws:iam::219780720175:role/rekognition_role",
        "SNSTopicArn": "arn:aws:sns:us-west-2:219780720175:VideoAnalyzerTopic"
    },
    "Video": {
        "S3Object": {
            "Bucket": "image-recognition-analyzer-bucket",
            "Name": "v1.MOV",
            "Version": "1"
        }
    }
}