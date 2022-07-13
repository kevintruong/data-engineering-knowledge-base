#### HIGH AVAILABILITY APPROACHES FOR DATABASES


If possible, choose DynamoDB over RDS because of inherent fault tolerance.


If DynamoDB can’t be used, choose Aurora because of redundancy and automatic recovery features.


If Aurora can’t be used, choose Multi-AZ RDS.


Frequent RDS snapshots can protect against data corruption or failure and they won’t impact performance of Multi-AZ

deployment.


Regional replication is also an option but will not be strongly consistent.


If the database runs on EC2, you have to design the HA yourself.

