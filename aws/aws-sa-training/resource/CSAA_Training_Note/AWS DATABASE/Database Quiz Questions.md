### Database Quiz Questions


Answers and explanations are provided below after the last question in this section.


**Question 1: An organization is migrating their relational databases to the AWS Cloud. They require full operating

system access to install custom operational toolsets. Which AWS service should they use to host their databases?**


1. Amazon EC2

2. Amazon RDS

3. Amazon DynamoDB

4. Amazon ElastiCache


**Question 2: An organization is migrating databases into the AWS Cloud. They require a managed service for their MySQL

database and need automatic failover to a secondary database. Which solution should they use?**


1. Amazon RDS with Read Replicas

2. Amazon RDS with Multi-AZ

3. Amazon EC2 with database mirroring

4. Amazon Aurora with Global Database


**Question 3: An existing Amazon RDS database needs to be encrypted. How can you enable encryption for an unencrypted

Amazon RDS database?**


1. Enable encryption through the AWS management console

2. Take an encrypted snapshot of the DB instance and restore the snapshot back to the instance

3. Take an encrypted snapshot of the DB instance and create a new database instance from the snapshot

4. Create a new encrypted RDS database and migrate the data across


**Question 4: An Amazon RDS database is experiencing heavy demand and is slowing down. Most database calls are reads.

What is the simplest way to scale the database without downtime?**


1. Create a Read Replica

2. Change to an instance type with more resources

3. Offload data to DynamoDB


**Question 5: A new application requires a database that can allow writes to DB instances in multiple availability zones

with read after write consistency. Which solution meets these requirements?**


1. Amazon Aurora Global Database

2. Amazon Aurora Replicas

3. Amazon Aurora Cross-Region Replicas

4. Amazon Aurora Multi-Master


**Question 6: A customer needs a schema-less database that can seamlessly scale. Which AWS database service would you

recommend?**


1. Amazon DynamoDB


2. Amazon ElastiCache

3. Amazon RDS

4. Amazon Aurora


**Question 7: Which DynamoDB feature integrates with AWS Lambda to automatically execute functions in response to table

updates?**


1. DynamoDB Global Tables

2. DynamoDB Auto Scaling

3. DynamoDB Streams

4. DynamoDB DAX


**Question 8: You need to implement an in-memory caching layer in front of an Amazon RDS database. The caching layer

should allow encryption and replication. Which solution meets these requirements?**


1. Amazon ElastiCache Memcached

2. Amazon ElastiCache Redis

3. Amazon DynamoDB DAX


**Question 9: Which Amazon ElastiCache engine provides data persistence?**


1. Redis

2. Memcached


**Question 10: Which of the following is a good use case for Amazon RedShift?**


1. Schema-less transactional database

2. Relational data warehouse

3. Relational transactional database

4. Analytics using the Hadoop framework


**DATABASE - ANSWERS**


**Question 1, Answer: 1**


**Explanation:**


```

1 is correct. If you need to access the underlying operating system you must use Amazon EC2 for

a relational database.

2 is incorrect. You do not get access to the underlying operating system with Amazon RDS.

3 is incorrect. Amazon DynamoDB is not a relational database; it is a NoSQL type of database.

4 is incorrect. Amazon ElastiCache is an in-memory caching database, it is typically placed in front

of other databases. It also does not provide access to the underlying operating system.

```


**Question 2, Answer: 2**


**Explanation:**


```

1 is incorrect. A read replica will not provide automatic failover.

2 is correct. RDS Multi-AZ does provide automatic failover to a secondary database.

3 is incorrect. Amazon EC2 is not a managed service.

4 is incorrect. Amazon Aurora with Global Database is used for replicating a database across

multiple regions.

```


**Question 3, Answer: 3**


**Explanation:**


```

1 is incorrect. You cannot enable encryption for an existing database.

2 is incorrect. You cannot restore the encrypted snapshot to the existing database instance.

3 is correct. You need to take an encrypted snapshot and then create a new database instance

from the snapshot.

4 is incorrect. This is not the most efficient method as it involves manual copying of data.

```


**Question 4, Answer: 1**


**Explanation:**


```

1 is correct. A read replica is an easy way to quickly scale read traffic. You just need to update

your application to direct reads to the replica endpoint.

2 is incorrect. This requires downtime when you change instance types.

3 is incorrect. You cannot offload data from Amazon RDS to DynamoDB.

```


**Question 5, Answer: 4**


**Explanation:**


```

1 is incorrect. Aurora Global Database spans multiple regions for disaster recovery.

2 is incorrect. Aurora Replicas scale read operations but do not allow writes to multiple DB

instances.

3 is incorrect. Aurora Cross-Region Replicase scale read operations across regions. They do not

allow writes to DB instances in multiple AZs.

4 is correct. Amazon Aurora Multi-Master adds the ability to scale out write performance across

multiple Availability Zones and provides configurable read after write consistency.

```


**Question 6, Answer: 1**


**Explanation:**


```

1 is correct. DynamoDB is a schema-less NoSQL database that provides push-button scaling.

2 is incorrect. ElastiCache is an in-memory relational database so it is not schema-less.

3 is incorrect. Amazon RDS is a relational database (not schema-less) and uses EC2 instances so

does not offer push-button scaling.

4 is incorrect. Amazon Aurora is a relational database (not schema-less) and uses EC2 instances

so does not offer push-button scaling.

```


**Question 7, Answer: 3**


**Explanation:**


```

1 is incorrect. DynamoDB Global Tables provides a multi-region, multi-master database solution.

2 is incorrect. DynamoDB Auto Scaling is for scaling read and write capacity.

3 is correct. DynamoDB Streams maintains a list of item level changes and can integrate with

Lambda to create triggers.

4 is incorrect. DynamoDB DAX provide microsecond latency for read requests to DynamoDB

tables.

```


**Question 8, Answer: 2**


**Explanation:**


```

1 is incorrect. Memcached does not provide encryption or replication.

2 is correct. Redis provides encryption and replication.

3 is incorrect. DynamoDB DAX works with DynamoDB not Amazon RDS.

```


**Question 9, Answer: 1**


**Explanation:**


```

1 is correct. Redis provides data persistence.

2 is incorrect. Memcached does not provide data persistence.

```


**Question 10, Answer: 2**


**Explanation:**


```

1 is incorrect. RedShift is not a schema-less database, it is a relational database.

2 is correct. RedShift is a data warehouse optimized for online analytics processing (OLAP).

3 is incorrect. RedShift is optimized for online analytics processing (OLAP) use cases not online

transactional processing (OLTP) use cases.

4 is incorrect. RedShift can be analyzed using SQL not Hadoop (should use EMR).

```

