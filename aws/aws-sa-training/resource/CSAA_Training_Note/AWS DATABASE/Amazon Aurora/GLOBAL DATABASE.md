#### GLOBAL DATABASE


For globally distributed applications you can use Global Database, where a single Aurora database can span multiple AWS

regions to enable fast local reads and quick disaster recovery.


Global Database uses storage-based replication to replicate a database across multiple AWS Regions, with typical latency

of less than 1 second.


You can use a secondary region as a backup option in case you need to recover quickly from a regional degradation or

outage.


A database in a secondary region can be promoted to full read/write capabilities in less than 1 minute.


The following table depicts the Aurora Global Database topology:

