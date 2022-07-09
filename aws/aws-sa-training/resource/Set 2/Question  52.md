#### Question  52


**A customer has a production application running on Amazon EC2. The application frequently overwrites and deletes data,

and it is essential that the application receives the most up-to-date version of the data whenever it is requested.**


**Which service is most appropriate for these requirements?**


1: Amazon RedShift


2: Amazon S3


3: AWS Storage Gateway


4: Amazon RDS


Answer: 4


**Explanation:**


This scenario asks that when retrieving data the chosen storage solution should always return the most up-to- date data.

Therefore we must use Amazon RDS as it provides read-after-write consistency.


- CORRECT "Amazon RDS" is the correct answer.


- INCORRECT "Amazon RedShift" is incorrect. Amazon RedShift is a data warehouse and is not used as a transactional

  database so this is the wrong use case for it.


- INCORRECT "Amazon S3" is incorrect. Amazon S3 only provides eventual consistency for overwrites and deletes.


- INCORRECT "AWS Storage Gateway" is incorrect. AWS Storage Gateway is used for enabling hybrid cloud access to AWS

  storage services from on-premises.


**References:**


https://docs.aws.amazon.com/rds/index.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

