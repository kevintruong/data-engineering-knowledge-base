#### REDIS


Data is persistent.


Can be used as a datastore.


Not multi-threaded.


Scales by adding shards, not nodes.


A Redis shard is a subset of the cluster’s keyspace, that can include a primary node and zero or more read-replicas.


Supports automatic and manual snapshots (S3).


Backups include cluster data and metadata.


You can restore your data by creating a new Redis cluster and populating it from a backup.


Supports master/slave replication.


During backup you cannot perform CLI or API operations on the cluster.


Automated backups are enabled by default (automatically deleted with Redis deletion).


You can only move snapshots between regions by exporting them from Elasticache before moving between regions (can then

populate a new cluster with data).


Multi-AZ is possible using read replicas in another AZ in the same region.


**Clustering mode disabled:**


- You can only have one shard.

- One shard can have one read/write primary node and 0 - 5 read only replicas.

- You can distribute the replicas over multiple AZs in the same region.

- Replication from the primary node is asynchronous.


A Redis cluster with cluster mode disabled is represented in the diagram below:


**Clustering mode enabled:**


- Can have up to 15 shards.

- Each shard can have one primary node and 0 - 5 read only replicas.

- Taking snapshots can slow down nodes, best to take from the read replicas.


A **Redis cluster with cluster mode enabled** is represented in the diagram below:


**Multi-AZ failover:**


- Failures are detected by Elasticache.

- Elasticache automatically promotes the replica that has the lowest replica lag.

- DNS records remain the same but point to the IP of the new primary.

- Other replicas start to sync with the new primary.


You can have a fully automated, fault tolerant Elasticache-Redis implementation by enabling both cluster mode and

multi-AZ failover.


The following table compares the Memcached and Redis engines:

