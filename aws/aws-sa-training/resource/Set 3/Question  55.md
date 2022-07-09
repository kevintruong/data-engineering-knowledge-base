#### Question  55


**You need to scale read operations for your Amazon Aurora DB within a region. To increase availability you also need to

be able to failover if the primary instance fails.**


**What should you implement?**


1: Aurora Replicas


2: A DB cluster


3: An Aurora Cluster Volume


4: Aurora Global Database


Answer: 1


**Explanation:**


Aurora Replicas are independent endpoints in an Aurora DB cluster, best used for scaling read operations and increasing

availability. Up to 15 Aurora Replicas can be distributed across the Availability Zones that a DB cluster spans within

an AWS Region. To increase availability, you can use Aurora Replicas as failover targets. That is, if the primary

instance fails, an Aurora Replica is promoted to the primary instance.


The graphic below provides an overview of Aurora Replicas:


- CORRECT "Aurora Replicas" is the correct answer.


- INCORRECT "A DB cluster" is incorrect. An **Amazon Aurora DB cluster** consists of a DB instance, compatible with

  either MySQL or PostgreSQL, and a cluster volume that represents the data for the DB cluster, copied across three

  Availability Zones as a single, virtual volume. The DB cluster contains a primary instance and, **_optionally_** , up

  to 15 Aurora Replicas. A DB cluster does not necessarily scale read operations as it is option to deploy Aurora

  Replicas, therefore it can be thought of as more of a storage level availability feature in this case and is not the

  best answer.


- INCORRECT "An Aurora Cluster Volume" is incorrect. A cluster volume manages the data for DB instances in a DB cluster

  and does not provide read scaling.


- INCORRECT "Aurora Global Database" is incorrect. Amazon Aurora Global Database is not suitable for scaling read

  operations within a region. It is a new feature in the MySQL-compatible edition of Amazon Aurora, designed for

  applications with a global footprint. It allows a single Aurora database to span multiple AWS regions, with fast

  replication to enable low-latency global reads and disaster recovery from region-wide outages.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-aurora/

