*

**Explanation:**

Amazon ElastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocol- compliant server

nodes in the cloud. The in-memory caching provided by ElastiCache can be used to

significantly improve latency and throughput for many read-heavy application workloads or compute-intensive workloads.

Read replicas are used for read heavy DBs and replication is asynchronous. They are for workload sharing and offloading

and are created from a snapshot of the master instance

* ✅ :  "Add RDS read replicas in each AZ" is a correct answer.

* ✅ :  "Deploy ElastiCache in each AZ" is also a correct answer.

* ❌ :  "Use an ELB to distribute load between RDS instances" is incorrect. You cannot use an ELB to distributed

  load between different RDS instances.

* ❌ :  "Migrate to DynamoDB" is incorrect. Moving from a relational DB to a NoSQL DB (DynamoDB) is unlikely to be a

  viable solution.

* ❌ :  "Use a larger RDS instance size" is incorrect. Using a larger instance size may alleviate the problems the

  question states that the solution should offload reads from the main DB, read replicas can do this.

**References:**

<https://aws.amazon.com/rds/features/read-replicas/>

<https://aws.amazon.com/elasticache/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- elasticache/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----
* #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>-_elasticache/> #amazon_elasticache #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #rds_instances #dynamodb
