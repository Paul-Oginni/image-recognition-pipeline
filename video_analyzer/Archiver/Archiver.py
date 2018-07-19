#!/usr/bin/env python3.6
import archiver_config as config
import boto3
import os
from pathlib import Path

class Archiver():

    def __init__(self):
        self.Path = Path(config.configurations['path_to_data'])
        self.processed_folder = config.configurations["processed_folder"]

        # self.Path = Path(config.path_to_data)
        # self.processed_folder = config.processed_folder

    def archive(self):
        # Put all the files into a list
        try:
            s3 = boto3.resource('s3')
            # posix_file_list = list(self.Path.glob('**/*.txt'))
            posix_file_list = list(self.Path.glob('**/*.MOV'))

            # Upload the files to S3
            for i in range(len(posix_file_list)):
                s3.Object('image-recognition-analyzer-bucket', posix_file_list[i].parts[-1]).put(Body=open(posix_file_list[i], 'rb'))

                # Move files to processed folder
                os.rename(str(posix_file_list[i].absolute()), str(self.processed_folder) + "/" + str(posix_file_list[i].parts[-1]))

        except RuntimeError:
            print("A runtime error has occured")

a = Archiver()
a.archive()

