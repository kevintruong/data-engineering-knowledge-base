#### Question  39


**Your company is starting to use AWS to host new web-based applications. A new two-tier application will be deployed

that provides customers with access to data records. It is important that the application is highly responsive and

retrieval times are optimized. You’re looking for a persistent data store that can provide the required performance.

From the list below what AWS service would you recommend for this requirement?**


1: RDS in a multi-AZ configuration


2: ElastiCache with the Redis engine


3: Kinesis Data Streams


4: ElastiCache with the Memcached engine


Answer: 2


```

Region A

```


```

Amazon DynamoDB

```


```

App Server

```


```

Read Write

```


```

Region B

```


```

Amazon DynamoDB

```


```

App Server

```


```

Asynchronous

replication

```


```

Write

```


```

Region C

```


```

Amazon DynamoDB

```


```

App Server

```


```

Read Read Write

```


```

Asynchronous

replication

```


**Explanation:**


ElastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocol-compliant server nodes in

the cloud. The in-memory caching provided by ElastiCache can be used to significantly improve latency and throughput for

many read-heavy application workloads or compute-intensive workloads


There are two different database engines with different characteristics as per below:


The correct choice for this scenario is Redis as Redis provides the persistency that is required.


- CORRECT "ElastiCache with the Redis engine" is the correct answer.


- INCORRECT "RDS in a multi-AZ configuration" is incorrect. RDS is not the optimum solution due to the requirement to

  optimize retrieval times which is a better fit for an in-memory data store such as ElastiCache.


- INCORRECT "Kinesis Data Streams" is incorrect. Kinesis Data Streams is used for processing streams of data, it is not

  a persistent data store.


- INCORRECT "ElastiCache with the Memcached engine" is incorrect as Memcached does not offer persistence.


**References:**


https://aws.amazon.com/elasticache/redis/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

elasticache/

