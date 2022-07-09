#### Question  11


**A company has some statistical data stored in an Amazon RDS database. The company want to allow users to access this

information using an API. A solutions architect must create a solution that allows sporadic access to the data, ranging

from no requests to large bursts of traffic.**


**Which solution should the solutions architect suggest?**


1: Set up an Amazon API Gateway and use Amazon ECS


2 : Set up an Amazon API Gateway and use AWS Elastic Beanstalk


3: Set up an Amazon API Gateway and use AWS Lambda functions


4: Set up an Amazon API Gateway and use Amazon EC2 with Auto Scaling


Answer: 3


**Explanation:**


This question is simply asking you to work out the best compute service for the stated requirements. The key

requirements are that the compute service should be suitable for a workload that can range quite broadly in demand from

no requests to large bursts of traffic.


AWS Lambda is an ideal solution as you pay only when requests are made and it can easily scale to accommodate the large

bursts in traffic. Lambda works well with both API Gateway and Amazon RDS.


- CORRECT "Set up an Amazon API Gateway and use AWS Lambda functions" is the correct answer.


- INCORRECT "Set up an Amazon API Gateway and use Amazon ECS" is incorrect


- INCORRECT "Set up an Amazon API Gateway and use AWS Elastic Beanstalk" is incorrect


- INCORRECT "Set up an Amazon API Gateway and use Amazon EC2 with Auto Scaling" is incorrect


**References:**


https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/

