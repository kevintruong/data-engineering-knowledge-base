#### Question  54


**A three-tier web application that is deployed in an Amazon VPC has been experiencing heavy load on the database layer.

The database layer uses an Amazon RDS MySQL instance in a multi-AZ configuration. Customers have been complaining about

poor response times. During troubleshooting it has been noted that the database layer is experiencing high read

contention during peak hours of the day.**


**What are two possible options that could be used to offload some of the read traffic from the database to resolve the

performance issues? (Select TWO)**


1: Add RDS read replicas in each AZ


2: Use an ELB to distribute load between RDS instances


3: Migrate to DynamoDB


4: Use a larger RDS instance size


5: Deploy ElastiCache in each AZ


**Answer: 1,5**


**Explanation:**


Amazon ElastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocol- compliant server

nodes in the cloud. The in-memory caching provided by ElastiCache can be used to


significantly improve latency and throughput for many read-heavy application workloads or compute-intensive workloads.


Read replicas are used for read heavy DBs and replication is asynchronous. They are for workload sharing and offloading

and are created from a snapshot of the master instance


- CORRECT "Add RDS read replicas in each AZ" is a correct answer.


- CORRECT "Deploy ElastiCache in each AZ" is also a correct answer.


- INCORRECT "Use an ELB to distribute load between RDS instances" is incorrect. You cannot use an ELB to distributed

  load between different RDS instances.


- INCORRECT "Migrate to DynamoDB" is incorrect. Moving from a relational DB to a NoSQL DB (DynamoDB) is unlikely to be a

  viable solution.


- INCORRECT "Use a larger RDS instance size" is incorrect. Using a larger instance size may alleviate the problems the

  question states that the solution should offload reads from the main DB, read replicas can do this.


**References:**


https://aws.amazon.com/rds/features/read-replicas/


https://aws.amazon.com/elasticache/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

elasticache/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

