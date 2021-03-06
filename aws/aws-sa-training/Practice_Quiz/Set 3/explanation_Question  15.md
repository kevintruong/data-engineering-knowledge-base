**Explanation:**

Amazon ElastiCache is an in-memory database. With ElastiCache Memcached there is no data replication or high

availability. As you can see in the diagram, each node is a separate partition of data:

Therefore, the Redis engine must be used which does support both data replication and clustering. The following diagram

shows a Redis architecture with cluster mode enabled:

```

Region A

```

```

Availability Zone A

```

```

Node 2

```

```

Availability Zone B

```

```

Node 4

```

Node (^1) Node 5 ElastiCache Memcached Cluster Each node is a partition of data Node 3 Node n

- ✅ :  "Amazon ElastiCache for Redis" is the correct answer.

- ❌ :  "Amazon ElastiCache for Memcached" is incorrect as Memcached does not support data replication or high

  availability.

- ❌ :  "Amazon RDS for MySQL" is incorrect as this is not an in-memory database.

- ❌ :  "Amazon RDS for PostgreSQL" is incorrect as this is not an in-memory database.

**References:**

<https://aws.amazon.com/elasticache/redis/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- elasticache/

----

- #elasticache_memcached_cluster #<https://aws.amazon.com/elasticache/redis/> #amazon_elasticache #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>>- #redis_architecture
