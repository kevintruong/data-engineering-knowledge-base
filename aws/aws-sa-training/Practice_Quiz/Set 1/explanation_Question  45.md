**Explanation:**

Amazon DynamoDB global tables provide a fully managed solution for deploying a multi-region, multi-master database. This

is the only solution presented that provides an active-active configuration where reads and writes can take place in

multiple regions with full bi-directional synchronization.

- ✅ :  "Amazon DynamoDB with global tables" is the correct answer.

- ❌ :  "AWS Database Migration Service with change data capture" is incorrect as the DMS is used for data migration

  from a source to a destination. However, in this example we need a multi-master database and DMS will not allow this

  configuration.

- ❌ :  "Amazon Athena with Amazon S3 cross-region replication" is incorrect. Amazon Athena with S3 cross-region

  replication is not suitable. This is not a solution that provides a transactional database solution

  (Athena is used for analytics), or active-active synchronization.

- ❌ :  "Amazon Aurora Global Database" is incorrect. Amazon Aurora Global Database provides read access to a

  database in multiple regions – it does not provide active-active configuration with bi-directional synchronization (

  though you can failover to your read-only DBs and promote them to writable).

**References:**

<https://aws.amazon.com/blogs/database/how-to-use-amazon-dynamodb-global-tables-to-power-multiregion>- architectures/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- dynamodb/

----

- #<https://aws.amazon.com/blogs/database/how-to-use-amazon-dynamodb-global-tables-to-power-multiregion>>-_architectures/ #amazon_aurora_global_database #amazon_dynamodb #aws_database_migration_service #cross_-_region_replication
