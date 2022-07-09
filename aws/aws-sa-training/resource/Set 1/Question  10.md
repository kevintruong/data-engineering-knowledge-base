#### Question  10


**A solutions architect is designing a new service that will use an Amazon API Gateway API on the frontend. The service

will need to persist data in a backend database using key-value requests. Initially, the data requirements will be

around 1 GB and future growth is unknown. Requests can range from 0 to over 800 requests per second.**


**Which combination of AWS services would meet these requirements? (Select TWO)**


1: AWS Fargate


2: AWS Lambda


3: Amazon DynamoDB


4: Amazon EC2 Auto Scaling


5: Amazon RDS


Answer: 2, 3


**Explanation:**


In this case AWS Lambda can perform the computation and store the data in an Amazon DynamoDB table. Lambda can scale

concurrent executions to meet demand easily and DynamoDB is built for key-value data storage requirements and is also

serverless and easily scalable. This is therefore a cost effective solution for unpredictable workloads.


- CORRECT "AWS Lambda" is a correct answer.


- CORRECT "Amazon DynamoDB" is also a correct answer.


- INCORRECT "AWS Fargate" is incorrect as containers run constantly and therefore incur costs even when no requests are

  being made.


- INCORRECT "Amazon EC2 Auto Scaling" is incorrect as this uses EC2 instances which will incur costs even when no

  requests are being made.


- INCORRECT "Amazon RDS" is incorrect as this is a relational database not a No-SQL database. It is therefore not

  suitable for key-value data storage requirements.


**References:**


https://aws.amazon.com/lambda/features/


https://aws.amazon.com/dynamodb/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/

