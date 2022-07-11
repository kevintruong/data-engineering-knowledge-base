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

- ✅ :  "ElastiCache with the Redis engine" is the correct answer.

- ❌ :  "RDS in a multi-AZ configuration" is incorrect. RDS is not the optimum solution due to the requirement to

  optimize retrieval times which is a better fit for an in-memory data store such as ElastiCache.

- ❌ :  "Kinesis Data Streams" is incorrect. Kinesis Data Streams is used for processing streams of data, it is not

  a persistent data store.

- ❌ :  "ElastiCache with the Memcached engine" is incorrect as Memcached does not offer persistence.

**References:**

<https://aws.amazon.com/elasticache/redis/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- elasticache/

----

- #amazon_dynamodb #<https://aws.amazon.com/elasticache/redis/> #redis_engine #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>>- #elasticache
