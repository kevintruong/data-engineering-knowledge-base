#### Question  45


**A retail organization is deploying a new application that will read and write data to a database. The company wants to

deploy the application in three different AWS Regions in an active-active configuration. The databases need to replicate

to keep information in sync.**


**Which solution best meets these requirements?**


1: AWS Database Migration Service with change data capture


2: Amazon DynamoDB with global tables


3: Amazon Athena with Amazon S3 cross-region replication


4: Amazon Aurora Global Database


Answer: 2


**Explanation:**


Amazon DynamoDB global tables provide a fully managed solution for deploying a multi-region, multi-master database. This

is the only solution presented that provides an active-active configuration where reads and writes can take place in

multiple regions with full bi-directional synchronization.


- CORRECT "Amazon DynamoDB with global tables" is the correct answer.


- INCORRECT "AWS Database Migration Service with change data capture" is incorrect as the DMS is used for data migration

  from a source to a destination. However, in this example we need a multi-master database and DMS will not allow this

  configuration.


- INCORRECT "Amazon Athena with Amazon S3 cross-region replication" is incorrect. Amazon Athena with S3 cross-region

  replication is not suitable. This is not a solution that provides a transactional database solution

  (Athena is used for analytics), or active-active synchronization.


- INCORRECT "Amazon Aurora Global Database" is incorrect. Amazon Aurora Global Database provides read access to a

  database in multiple regions – it does not provide active-active configuration with bi-directional synchronization (

  though you can failover to your read-only DBs and promote them to writable).


**References:**


https://aws.amazon.com/blogs/database/how-to-use-amazon-dynamodb-global-tables-to-power-multiregion-

architectures/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/

