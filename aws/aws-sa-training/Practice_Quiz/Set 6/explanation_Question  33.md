*

**Explanation:**

Amazon RDS Read replicas are used for read heavy DBs and replication is asynchronous. Read replicas are for workload

sharing and offloading. Read replicas can be in another region (uses asynchronous replication). This solution will

enable better performance for users in the other AWS regions for database queries and is a managed service.

* ✅ :  "RDS with cross-region Read Replicas" is the correct answer.

* ❌ :  "RDS with Multi-AZ" is incorrect. RDS with Multi-AZ is within a region only

* ❌ :  "EC2 instances with EBS replication" is incorrect. EC2 instances with EBS replication is not a suitable

  solution.

* ❌ :  "ElastiCache with Redis and clustering mode enabled" is incorrect. ElastiCache is an in-memory key/value

  store database (more OLAP than OLTP) and is not suitable for this scenario. Clustering mod is only available within

  the same region.

**References:**

<https://aws.amazon.com/blogs/aws/cross-region-read-replicas-for-amazon-rds-for-mysql/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----
* #<https://aws.amazon.com/blogs/aws/cross-region-read-replicas-for-amazon-rds-for-mysql/> #amazon_rds_read_replicas #other_aws_regions #cross_-_region_read_replicas #ebs_replication
