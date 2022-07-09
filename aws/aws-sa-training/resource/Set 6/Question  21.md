#### Question  21


**Some data has become corrupted in an Amazon RDS database. A Solutions Architect plans to use point-in- time restore to

recover the data to the last known good configuration. Which of the following statements is correct about restoring an

RDS database to a specific point-in-time? (Select TWO)**


1: You can restore up to the last 5 minutes


2: Custom DB security groups are applied to the new DB instance


3: You can restore up to the last 1 minute


4: The default DB security group is applied to the new DB instance


5: The database restore overwrites the existing database


**Answer: 1,4**


**Explanation:**


You can restore a DB instance to a specific point in time, creating a new DB instance. When you restore a DB instance to

a point in time, the default DB security group is applied to the new DB instance. If you need custom DB security groups

applied to your DB instance, you must apply them explicitly using the AWS Management Console, the AWS CLI

modify-db-instance command, or the Amazon RDS API ModifyDBInstance operation after the DB instance is available.


Restored DBs will always be a new RDS instance with a new DNS endpoint and you can restore up to the last 5 minutes.


- CORRECT "You can restore up to the last 5 minutes" is a correct answer.


- CORRECT "The default DB security group is applied to the new DB instance" is also a correct answer.


- INCORRECT "Custom DB security groups are applied to the new DB instance" is incorrect. Only default DB parameters and

  security groups are restored – you must manually associate all other DB parameters and SGs..


- INCORRECT "You can restore up to the last 1 minute" is incorrect. You can restore up to the last 5 minutes.


- INCORRECT "The database restore overwrites the existing database" is incorrect. You cannot restore from a DB snapshot

  to an existing DB – a new instance is created when you restore.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

