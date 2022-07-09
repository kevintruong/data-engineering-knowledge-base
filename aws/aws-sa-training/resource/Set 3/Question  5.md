#### Question  5


**A production application runs on an Amazon RDS MySQL DB instance. A solutions architect is building a new reporting

tool that will access the same data. The reporting tool must be highly available and not impact the performance of the

production application.**


**How can this be achieved?**


1: Create a cross-region Multi-AZ deployment and create a read replica in the second region


2: Create a Multi-AZ RDS Read Replica of the production RDS DB instance


3: Use Amazon Data Lifecycle Manager to automatically create and manage snapshots


4: Create a Single-AZ RDS Read Replica of the production RDS DB instance. Create a second Single-AZ RDS Read Replica

from the replica


Answer: 2


**Explanation:**


You can create a read replica as a Multi-AZ DB instance. Amazon RDS creates a standby of your replica in another

Availability Zone for failover support for the replica. Creating your read replica as a Multi-AZ DB instance is

independent of whether the source database is a Multi-AZ DB instance.


- CORRECT "Create a Multi-AZ RDS Read Replica of the production RDS DB instance" is the correct answer.


- INCORRECT "Create a Single-AZ RDS Read Replica of the production RDS DB instance. Create a second Single- AZ RDS Read

  Replica from the replica" is incorrect. Read replicas are primarily used for horizontal scaling. The best solution for

  high availability is to use a Multi-AZ read replica.


- INCORRECT "Create a cross-region Multi-AZ deployment and create a read replica in the second region" is incorrect as

  you cannot create a cross-region Multi-AZ deployment with RDS.


- INCORRECT "Use Amazon Data Lifecycle Manager to automatically create and manage snapshots" is incorrect as using

  snapshots is not the best solution for high availability.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.html#US

ER_MySQL.Replication.ReadReplicas.MultiAZ


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

