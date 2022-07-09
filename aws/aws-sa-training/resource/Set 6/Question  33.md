#### Question  33


**A large multi-national client has requested a design for a multi-region database. The master database will be in the

EU (Frankfurt) region and databases will be located in 4 other regions to service local read traffic. The database

should be a managed service including the replication.**


**The solution should be cost-effective and secure. Which AWS service can deliver these requirements?**


1: RDS with Multi-AZ


2: EC2 instances with EBS replication


3: RDS with cross-region Read Replicas


4: ElastiCache with Redis and clustering mode enabled


**Answer: 3**


**Explanation:**


Amazon RDS Read replicas are used for read heavy DBs and replication is asynchronous. Read replicas are for workload

sharing and offloading. Read replicas can be in another region (uses asynchronous replication). This solution will

enable better performance for users in the other AWS regions for database queries and is a managed service.


- CORRECT "RDS with cross-region Read Replicas" is the correct answer.


- INCORRECT "RDS with Multi-AZ" is incorrect. RDS with Multi-AZ is within a region only


- INCORRECT "EC2 instances with EBS replication" is incorrect. EC2 instances with EBS replication is not a suitable

  solution.


- INCORRECT "ElastiCache with Redis and clustering mode enabled" is incorrect. ElastiCache is an in-memory key/value

  store database (more OLAP than OLTP) and is not suitable for this scenario. Clustering mod is only available within

  the same region.


**References:**


https://aws.amazon.com/blogs/aws/cross-region-read-replicas-for-amazon-rds-for-mysql/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

