#!/usr/bin/env python3.6

import archiver_config as config
import boto3
import os
from pathlib import Path

class Archiver():

    def __init__(self):
        # Create a PosixPath object (named "path") that points to the directory of the pre-processed video
        self.path = Path(config.configurations['path_to_data'])
        # Identify the directory location where videos will be sent post-processing
        self.processed_folder = config.configurations["processed_folder"]

    def archive(self):
        # Put all the files into a list
        try:
            s3 = boto3.resource('s3')
            # posix_file_list = list(self.Path.glob('**/*.txt'))
            posix_file_list = list(self.path.glob('**/*.MOV'))

            # Upload the files to S3
            for i in posix_file_list:
                s3.Object('image-recognition-analyzer-bucket', posix_file_list[i].parts[-1]).put(Body=open(posix_file_list[i], 'rb'))

                # Move files to the post-processed folder
                os.rename(str(posix_file_list[i].absolute()), str(self.processed_folder) + "/" + str(posix_file_list[i].parts[-1]))

        except RuntimeError:
            print("A runtime error has occured")

a = Archiver()
a.archive()

