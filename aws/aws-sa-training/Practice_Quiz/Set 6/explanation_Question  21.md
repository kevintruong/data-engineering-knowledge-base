*

**Explanation:**

You can restore a DB instance to a specific point in time, creating a new DB instance. When you restore a DB instance to

a point in time, the default DB security group is applied to the new DB instance. If you need custom DB security groups

applied to your DB instance, you must apply them explicitly using the AWS Management Console, the AWS CLI

modify-db-instance command, or the Amazon RDS API ModifyDBInstance operation after the DB instance is available.

Restored DBs will always be a new RDS instance with a new DNS endpoint and you can restore up to the last 5 minutes.

* ✅ :  "You can restore up to the last 5 minutes" is a correct answer.

* ✅ :  "The default DB security group is applied to the new DB instance" is also a correct answer.

* ❌ :  "Custom DB security groups are applied to the new DB instance" is incorrect. Only default DB parameters and

  security groups are restored – you must manually associate all other DB parameters and SGs..

* ❌ :  "You can restore up to the last 1 minute" is incorrect. You can restore up to the last 5 minutes.

* ❌ :  "The database restore overwrites the existing database" is incorrect. You cannot restore from a DB snapshot

  to an existing DB – a new instance is created when you restore.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----
* #amazon_rds_api_modifydbinstance_operation #new_db_instance #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #db_instance #default_db_security_group
