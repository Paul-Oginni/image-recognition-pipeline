#!/usr/bin/env python3

from cassandra.cluster import Cluster

# Instantiate cluster 

def execute_query(query):
    with Cluster(['35.163.17.243'], port=9042) as cass_cluster:
        # Connect to nodes on the cluster
        cass_session = cass_cluster.connect('data_pipeline')
        cass_session.execute(query)
