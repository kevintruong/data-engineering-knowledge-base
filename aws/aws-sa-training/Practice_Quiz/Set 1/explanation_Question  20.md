**Explanation:**

The issue here is latency with read queries being directed from Australia to UK which is great physical distance. A

solution is required for improving read performance in Australia.

An Aurora global database consists of one primary AWS Region where your data is mastered, and up to five read-only,

secondary AWS Regions. Aurora replicates data to the secondary AWS Regions with typical latency of under a second. You

issue write operations directly to the primary DB instance in the primary AWS Region.

This solution will provide better performance for users in the Australia Region for queries. Writes must still take

place in the UK Region but read performance will be greatly improved.

- ✅ :  "Migrate the database to an Amazon Aurora global database in MySQL compatibility mode. Configure read replicas

  in ap-southeast-2" is the correct answer.

- ❌ :  "Migrate the database to Amazon RDS for MySQL. Configure Multi-AZ in the Australian Region" is incorrect.

  The database is located in UK. If the database is migrated to Australia then the reverse problem will occur. Multi-AZ

  does not assist with improving query performance across Regions.

- ❌ :  "Migrate the database to Amazon DynamoDB. Use DynamoDB global tables to enable replication to additional

  Regions" is incorrect as a relational database running on MySQL is unlikely to be compatible with DynamoDB.

- ❌ :  "Deploy MySQL instances in each Region. Deploy an Application Load Balancer in front of MySQL to reduce the

  load on the primary instance" is incorrect as you can only put ALBs in front of the web tier, not the DB tier.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-aurora/>

----

- #amazon_dynamodb #amazon_aurora #secondary_aws_regions #primary_aws_region #dynamodb
