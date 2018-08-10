#!/usr/bin/env python3

from cassandra.cluster import Cluster

cass_cluster = Cluster(['35.163.17.243'], port=9042)
cass_session = cass_cluster.connect('data_pipeline')
