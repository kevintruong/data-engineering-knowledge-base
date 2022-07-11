**Explanation:**

You can create a read replica as a Multi-AZ DB instance. Amazon RDS creates a standby of your replica in another

Availability Zone for failover support for the replica. Creating your read replica as a Multi-AZ DB instance is

independent of whether the source database is a Multi-AZ DB instance.

- ✅ :  "Create a read replica as a Multi-AZ DB instance" is the correct answer.

- ❌ :  "Deploy a read replica in a different AZ to the master DB instance" is incorrect as this does not provide

  high availability for the read replica

- ❌ :  "Deploy a read replica using Amazon ElastiCache" is incorrect as ElastiCache is not used to create read

  replicas of RDS database.

- ❌ :  "Deploy a read replica in the same AZ as the master DB instance" is incorrect as this solution does not

  include HA for the read replica.

**References:**

<https://aws.amazon.com/about-aws/whats-new/2018/01/amazon-rds-read-replicas-now-support-multi-az>- deployments/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----

- #<https://aws.amazon.com/about-aws/whats-new/2018/01/amazon-rds-read-replicas-now-support-multi-az>>- #multi_-_az_db_instance #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #amazon_elasticache #amazon_rds
