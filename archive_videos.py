#!/usr/bin/env python3.6
import boto3
from pathlib import Path

# Put all the files into a list
s3 = boto3.resource('s3')
p = Path('/Users/poginni/Google Drive/Coding/AWS/Streaming/20180403')
posix_file_list = list(p.glob('**/*.MOV'))

# Upload the files to S3
for i in range(len(posix_file_list)):    
    s3.Object('image-recognition-analyzer-bucket', posix_file_list[i].parts[-1]).put(Body=open(posix_file_list[i], 'rb'))
