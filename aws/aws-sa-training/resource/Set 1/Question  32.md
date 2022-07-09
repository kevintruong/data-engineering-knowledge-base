#### Question  32


**A new relational database is being deployed on AWS. The performance requirements are unknown. Which database service

does not require you to make capacity decisions upfront?**


1: Amazon DynamoDB


2: Amazon Aurora Serverless


3: Amazon ElastiCache


4: Amazon RDS


Answer: 2


**Explanation:**


If you don’t know the performance requirements it will be difficult to determine the correct instance type to use.

Amazon Aurora Serverless does not require you to make capacity decisions upfront as you do not select an instance type.

As a serverless service it will automatically scale as needed.


- CORRECT "Amazon Aurora Serverless" is the correct answer.


- INCORRECT "Amazon DynamoDB" is incorrect. Amazon DynamoDB is not a relational database, it is a NoSQL database.


- INCORRECT "Amazon ElastiCache" is incorrect. Amazon ElastiCache is more suitable for caching and also requires an

  instance type to be selected.


- INCORRECT "Amazon RDS" is incorrect. Amazon RDS requires an instance type to be selected.


**References:**


https://aws.amazon.com/rds/aurora/serverless/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-aurora/

