#### Question  23


**An organization has a large amount of data on Windows (SMB) file shares in their on-premises data center. The

organization would like to move data into Amazon S3. They would like to automate the migration of data over their AWS

Direct Connect link.**


**Which AWS service can assist them?**


1: AWS Database Migration Service (DMS)


2: AWS CloudFormation


3: AWS Snowball


4: AWS DataSync


Answer: 4


**Explanation:**


AWS DataSync can be used to move large amounts of data online between on-premises storage and Amazon S3 or Amazon

Elastic File System (Amazon EFS). DataSync eliminates or automatically handles many of these tasks, including scripting

copy jobs, scheduling and monitoring transfers, validating data, and optimizing network utilization. The source

datastore can be Server Message Block (SMB) file servers.


- CORRECT "AWS DataSync" is the correct answer.


- INCORRECT "AWS Database Migration Service (DMS)" is incorrect. AWS Database Migration Service (DMS) is used for

  migrating databases, not data on file shares.


- INCORRECT "AWS CloudFormation" is incorrect. AWS CloudFormation can be used for automating infrastructure

  provisioning. This is not the best use case for CloudFormation as DataSync is designed specifically for this scenario.


- INCORRECT "AWS Snowball" is incorrect. AWS Snowball is a hardware device that is used for migrating data into AWS. The

  organization plan to use their Direct Connect link for migrating data rather than sending it in via a physical device.

  Also, Snowball will not automate the migration.


**References:**


https://aws.amazon.com/datasync/faqs/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/migration/aws-datasync/

