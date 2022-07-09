#### Question  34


**Your company is opening a new office in the Asia Pacific region. Users in the new office will need to read data from

an RDS database that is hosted in the U.S. To improve performance, you are planning to implement a Read Replica of the

database in the Asia Pacific region. However, your Chief Security Officer

(CSO) has explained to you that the company policy dictates that all data that leaves the U.S must be encrypted at rest.

The master RDS DB is not currently encrypted.**


**What options are available to you? (Select TWO)**


1: You can create an encrypted Read Replica that is encrypted with the same key


2: You can create an encrypted Read Replica that is encrypted with a different key


3: You can enable encryption for the master DB by creating a new DB from a snapshot with encryption enabled


4: You can enable encryption for the master DB through the management console


5: You can use an ELB to provide an encrypted transport layer in front of the RDS DB


Answer: 2,3


**Explanation:**


You can encrypt your Amazon RDS instances and snapshots at rest by enabling the encryption option for your Amazon RDS DB

instance when you create it. However, you cannot encrypt an existing DB, you need to create a snapshot, copy it, encrypt

the copy, then build an encrypted DB from the snapshot.


Data that is encrypted at rest includes the underlying storage for a DB instance, its automated backups, Read Replicas,

and snapshots.


A Read Replica of an Amazon RDS encrypted instance is also encrypted using the same key as the master instance when both

are in the same Region. When in different Regions, a different key can be used.


- CORRECT "You can create an encrypted Read Replica that is encrypted with a different key" is the correct answer.


- CORRECT "You can enable encryption for the master DB by creating a new DB from a snapshot with encryption enabled"

  is the correct answer.


- INCORRECT "You can create an encrypted Read Replica that is encrypted with the same key" is incorrect. If the master

  and Read Replica are in different regions, you encrypt using the encryption key for that region.


- INCORRECT "You can enable encryption for the master DB through the management console" is incorrect as you can only

  enable encryption when you first create the database.


- INCORRECT "You can use an ELB to provide an encrypted transport layer in front of the RDS DB" is incorrect as ELBs are

  not placed in front of RDS instances, they are placed in front of EC2 instances.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

