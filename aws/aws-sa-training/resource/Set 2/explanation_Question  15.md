**Explanation:**

There are some limitations for encrypted Amazon RDS DB Instances: you can't modify an existing unencrypted Amazon RDS DB

instance to make the instance encrypted, and you can't create an encrypted read replica from an unencrypted instance.

However, you can use the Amazon RDS snapshot feature to encrypt an unencrypted snapshot that's taken from the RDS

database that you want to encrypt. Restore a new RDS DB instance from the encrypted snapshot to deploy a new encrypted

DB instance. Finally, switch your connections to the new DB instance.

- ✅ :  "Take a snapshot of the RDS instance. Create an encrypted copy of the snapshot. Restore the RDS instance from

  the encrypted snapshot" is the correct answer.

- ❌ :  "Create an Amazon ElastiCache cluster and encrypt data using the cache nodes" is incorrect as you cannot

  encrypt an RDS database using an ElastiCache cache node.

- ❌ :  "Enable encryption for the database using the API. Take a full snapshot of the database. Delete old

  snapshots" is incorrect as you cannot enable encryption for an existing database.

- ❌ :  "Create an RDS read replica with encryption at rest enabled. Promote the read replica to master and switch

  the application over to the new master. Delete the old RDS instance" is incorrect as you cannot create an encrypted

  read replica from an unencrypted database instance.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

<https://aws.amazon.com/premiumsupport/knowledge-center/rds-encrypt-instance-mysql-mariadb/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----

- #unencrypted_amazon_rds_db #<https://docs.aws.amazon.com/amazonrds/latest/userguide/overview.encryption.html> #amazon_rds_db_instances #new_rds_db_instance #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>
