*

**Explanation:**

To handle a higher load in your database, you can vertically scale up your master database with a simple push of a

button. In addition to scaling your master database vertically, you can also improve the performance of a read-heavy

database by using read replicas to horizontally scale your database.

* ✅ :  "Vertical scaling for read and write by choosing a larger instance size" is a correct answer.

* ✅ :  "Horizontal scaling for read capacity by creating a read-replica" is also a correct answer.

* ❌ :  "Horizontal scaling for write capacity by enabling Multi-AZ" is incorrect. You cannot scale write capacity

  by enabling Multi-AZ as only one DB is active and can be written to.

* ❌ :  "Vertical scaling for read and write by using Transfer Acceleration" is incorrect. Transfer Acceleration is

  a feature of S3 for fast uploads of objects.

* ❌ :  "Horizontal scaling for read and write by enabling Multi-Master RDS DB" is incorrect. There is no such thing

  as a Multi-Master MySQL RDS DB (there is for Aurora).

**References:**

<https://aws.amazon.com/blogs/database/scaling-your-amazon-rds-instance-vertically-and-horizontally/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----
* #multi_-_master_mysql_rds_db #multi_-_master_rds_db #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #write_capacity #larger_instance_size
