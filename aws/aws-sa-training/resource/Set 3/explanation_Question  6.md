**Explanation:**

Aurora Replicas are independent endpoints in an Aurora DB cluster, best used for scaling read operations and increasing

availability. Up to 15 Aurora Replicas can be distributed across the Availability Zones that a DB cluster spans within

an AWS Region.

The DB cluster volume is made up of multiple copies of the data for the DB cluster. However, the data in the cluster

volume is represented as a single, logical volume to the primary instance and to Aurora Replicas in the DB cluster.

As well as providing scaling for reads, Aurora Replicas are also targets for multi-AZ. In thi case the solutions

architect can update the application to read from the Multi-AZ standby instance.

- ✅ :  "Update the application to read from the Multi-AZ standby instance" is the correct answer.

- ❌ :  "Create a read replica and modify the application to use the appropriate endpoint" is incorrect. An Aurora

  Replica is both a standby in a Multi-AZ configuration and a target for read traffic. The architect simply needs to

  direct traffic to the Aurora Replica.

- ❌ :  "Enable read through caching on the Amazon Aurora database." is incorrect as this is not a feature of Amazon

  Aurora.

- ❌ :  "Create a second Amazon Aurora database and link it to the primary database as a read replica" is incorrect

  as an Aurora Replica already exists as this is a Multi-AZ configuration and the standby is an Aurora Replica that can

  be used for read traffic.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-aurora/>

----

- #aurora_db_cluster #amazon_aurora_database #second_amazon_aurora_database #aurora_replica #aurora_replicas
