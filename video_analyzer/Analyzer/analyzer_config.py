
analyzer_config = {
    "ClientRequestToken": "job_20180718_3",
    "JobTag": "job1jt",
    "MinConfidence": 1.0,
    "NotificationChannel": {
        "RoleArn": "arn:aws:iam::219780720175:role/rekognition_role",
        "SNSTopicArn": "arn:aws:sns:us-west-2:219780720175:VideoAnalyzerTopic"
    },
    "Video": {
        "S3Object": {
            "Bucket": "image-recognition-analyzer-bucket",
            "Name": "v8.MOV",
            "Version": "1"
        }
    },
    "AWS": {
        "Bucket_name":"image-recognition-analyzer-bucket"
    }
}
