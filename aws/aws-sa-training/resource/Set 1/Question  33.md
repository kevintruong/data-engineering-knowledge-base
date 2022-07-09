#### Question  33


**An Amazon RDS Read Replica is being deployed in a separate region. The master database is not encrypted but all data

in the new region must be encrypted. How can this be achieved?**


1: Enable encryption using Key Management Service (KMS) when creating the cross-region Read Replica


2: Encrypt a snapshot from the master DB instance, create an encrypted cross-region Read Replica from the snapshot


3: Enabled encryption on the master DB instance, then create an encrypted cross-region Read Replica


4: Encrypt a snapshot from the master DB instance, create a new encrypted master DB instance, and then create an

encrypted cross-region Read Replica


Answer: 4


**Explanation:**


You cannot create an encrypted Read Replica from an unencrypted master DB instance. You also cannot enable encryption

after launch time for the master DB instance. Therefore, you must create a new master DB by taking a snapshot of the

existing DB, encrypting it, and then creating the new DB from the snapshot. You can then create the encrypted

cross-region Read Replica of the master DB.


- CORRECT "Encrypt a snapshot from the master DB instance, create a new encrypted master DB instance, and then create an

  encrypted cross-region Read Replica" is the correct answer.


- INCORRECT "Enable encryption using Key Management Service (KMS) when creating the cross-region Read Replica" is

  incorrect. All other options will not work due to the limitations explained above.


- INCORRECT "Encrypt a snapshot from the master DB instance, create an encrypted cross-region Read Replica from the

  snapshot" is incorrect. All other options will not work due to the limitations explained above.


- INCORRECT "Enabled encryption on the master DB instance, then create an encrypted cross-region Read Replica" is

  incorrect. All other options will not work due to the limitations explained above.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

