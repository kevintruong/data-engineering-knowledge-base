#### Question  36


**A company is migrating an on-premises 10 TB MySQL database to AWS. The company expects the database to quadruple in

size and the business requirement is that replicate lag must be kept under 100 milliseconds.**


**Which Amazon RDS engine meets these requirements?**


1: Amazon Aurora


2: Oracle


3: Microsoft SQL Server


4: MySQL


Answer: 1


**Explanation:**


Aurora cluster volumes automatically grow as the amount of data in your database increases. An Aurora cluster volume can

grow to a maximum size of 64 tebibytes (TiB). Table size is limited to the size of the cluster volume. That is, the

maximum table size for a table in an Aurora DB cluster is 64 TiB.


Aurora Replicas are independent endpoints in an Aurora DB cluster, best used for scaling read operations and increasing

availability. Up to 15 Aurora Replicas can be distributed across the Availability Zones that a DB cluster spans within

an AWS Region. The DB cluster volume is made up of multiple copies of the data for the DB cluster. However, the data in

the cluster volume is represented as a single, logical volume to the primary instance and to Aurora Replicas in the DB

cluster.


As a result, all Aurora Replicas return the same data for query results with minimal replica lag—usually much less than

100 milliseconds after the primary instance has written an update. Replica lag varies depending on the rate of database

change. That is, during periods where a large amount of write operations occur for the database, you might see an

increase in replica lag.


- CORRECT "Amazon Aurora" is the correct answer.


- INCORRECT "Oracle" is incorrect as this database engine does not support the size or latency requirements.


- INCORRECT "Microsoft SQL Server" is incorrect as this database engine does not support the size or latency

  requirements.


- INCORRECT "MySQL" is incorrect as millisecond latency is not guaranteed with this database engine.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

