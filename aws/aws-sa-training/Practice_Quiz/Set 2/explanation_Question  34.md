**Explanation:**

You can encrypt your Amazon RDS instances and snapshots at rest by enabling the encryption option for your Amazon RDS DB

instance when you create it. However, you cannot encrypt an existing DB, you need to create a snapshot, copy it, encrypt

the copy, then build an encrypted DB from the snapshot.

Data that is encrypted at rest includes the underlying storage for a DB instance, its automated backups, Read Replicas,

and snapshots.

A Read Replica of an Amazon RDS encrypted instance is also encrypted using the same key as the master instance when both

are in the same Region. When in different Regions, a different key can be used.

- ✅ :  "You can create an encrypted Read Replica that is encrypted with a different key" is the correct answer.

- ✅ :  "You can enable encryption for the master DB by creating a new DB from a snapshot with encryption enabled"

  is the correct answer.

- ❌ :  "You can create an encrypted Read Replica that is encrypted with the same key" is incorrect. If the master

  and Read Replica are in different regions, you encrypt using the encryption key for that region.

- ❌ :  "You can enable encryption for the master DB through the management console" is incorrect as you can only

  enable encryption when you first create the database.

- ❌ :  "You can use an ELB to provide an encrypted transport layer in front of the RDS DB" is incorrect as ELBs are

  not placed in front of RDS instances, they are placed in front of EC2 instances.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----

- #<https://docs.aws.amazon.com/amazonrds/latest/userguide/overview.encryption.html> #amazon_rds_instances #amazon_rds_db #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #rds_instances
