#!/usr/bin/env python3

from cassandra.cluster import Cluster

# Instantiate cluster 
with Cluster(['35.163.17.243'], port=9042) as cass_cluster:
    # Connect to nodes on the cluster
    cass_session = cass_cluster.connect('data_pipeline')
    cass_session.execute(
        """
        INSERT INTO data_pipeline.rekognition_records (RequestId, Labels)
        VALUES ('81242968-9bd5-11e8-9536-05daccb47a39', ['AlloyWheel', 'AlloyWheels'])
        """
    )
