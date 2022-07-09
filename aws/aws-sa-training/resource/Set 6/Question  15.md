#### Question  15


**The database layer of an on-premises web application is being migrated to AWS. The database currently uses an

in-memory cache. A Solutions Architect must deliver a solution that supports high availability and replication for the

caching layer.**


**Which service should the Solutions Architect recommend?**


1: Amazon ElastiCache Redis


2: Amazon RDS Multi-AZ


3: Amazon ElastiCache Memcached


4: Amazon DynamoDB


Answer: 1


**Explanation:**


Amazon ElastiCache Redis is an in-memory database cache and supports high availability through replicas and multi-AZ.

The table below compares ElastiCache Redis with Memcached:


- CORRECT "Amazon ElastiCache Redis" is the correct answer.


- INCORRECT "Amazon ElastiCache Memcached" is incorrect as it does not support high availability or multi-AZ.


- INCORRECT "Amazon RDS Multi-AZ" is incorrect. This is not an in-memory database and it not suitable for use as a

  caching layer.


- INCORRECT "Amazon DynamoDB" is incorrect. DynamoDB is a non-relational database, you would not use it for a caching

  layer. Also, the in-memory, low-latency caching for DynamoDB is implemented using DynamoDB Accelerator (DAX).


**References:**


https://aws.amazon.com/elasticache/redis-vs-memcached/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

elasticache/

