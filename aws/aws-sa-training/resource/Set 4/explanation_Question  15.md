**Explanation:**

Larger data migrations with AWS DMS can include many terabytes of information. This process can be cumbersome due to

network bandwidth limits or just the sheer amount of data. AWS DMS can use Snowball Edge and Amazon S3 to migrate large

databases more quickly than by other methods.

When you're using an Edge device, the data migration process has the following stages:

- You use the AWS Schema Conversion Tool (AWS SCT) to extract the data locally and move it to an Edge device.

- You ship the Edge device or devices back to AWS.

- After AWS receives your shipment, the Edge device automatically loads its data into an Amazon S3 bucket.

- AWS DMS takes the files and migrates the data to the target data store. If you are using change data capture (CDC),

  those updates are written to the Amazon S3 bucket and then applied to the target data store.

- ✅ :  "Use the Schema Conversion Tool (SCT) to extract and load the data to an AWS Snowball Edge device. Use the AWS

  Database Migration Service (DMS) to migrate the data to Amazon DynamoDB" is the correct answer.

- ❌ :  "Setup an AWS Direct Connect and migrate the database to Amazon DynamoDB using the AWS Database Migration

  Service (DMS)" is incorrect as Direct Connect connections can take several weeks to implement.

- ❌ :  "Enable compression on the MongoDB database and use the AWS Database Migration Service

  (DMS) to directly migrate the database to Amazon DynamoDB" is incorrect. It’s unlikely that compression is going to

  make the difference and the company want to avoid the internet link as stated in the scenario.

- ❌ :  "Use the AWS Database Migration Service (DMS) to extract and load the data to an AWS Snowball Edge device.

  Complete the migration to Amazon DynamoDB using AWS DMS in the AWS Cloud" is incorrect. This is the wrong method; the

  Solutions Architect should use the SCT to extract and load to Snowball Edge and then AWS DMS in the AWS Cloud.

**References:**

<https://docs.aws.amazon.com/dms/latest/userguide/CHAP_LargeDBs.html>

<https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/migration/aws-database>-

migration-service/

----

- #aws_database_migration_service #aws_database_migration #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/migration/aws-database>>- #amazon_dynamodb #larger_data_migrations
