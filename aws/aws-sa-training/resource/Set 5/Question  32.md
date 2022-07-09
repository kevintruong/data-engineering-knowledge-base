#### Question  32


**A Solutions Architect is designing the compute layer of a serverless application. The compute layer will manage

requests from external systems, orchestrate serverless workflows, and execute the business logic.**


**The Architect needs to select the most appropriate AWS services for these functions. Which services should be used for

the compute layer? (Select TWO)**


1: Use Amazon ECS for executing the business logic


2: Use AWS CloudFormation for orchestrating serverless workflows


3: Use AWS Step Functions for orchestrating serverless workflows


4: Use AWS Elastic Beanstalk for executing the business logic


5: Use Amazon API Gateway with AWS Lambda for executing the business logic


**Answer: 3,5**


**Explanation:**


With Amazon API Gateway, you can run a fully managed REST API that integrates with Lambda to execute your business logic

and includes traffic management, authorization and access control, monitoring, and API versioning.


AWS Step Functions orchestrates serverless workflows including coordination, state, and function chaining as well as

combining long-running executions not supported within Lambda execution limits by breaking into multiple steps or by

calling workers running on Amazon Elastic Compute Cloud (Amazon EC2) instances or on- premises.


- CORRECT "Use AWS Step Functions for orchestrating serverless workflows" is the correct answer.


- CORRECT "Use Amazon API Gateway with AWS Lambda for executing the business logics" is the correct answer.


- INCORRECT "Use Amazon ECS for executing the business logic" is incorrect. The Amazon Elastic Container Service (

  ECS) is not a serverless application stack, containers run on EC2 instances.


- INCORRECT "Use AWS CloudFormation for orchestrating serverless workflows" is incorrect. AWS CloudFormation is used for

  describing and provisioning resources not actually performing workflow functions within the application.


- INCORRECT "Use AWS Elastic Beanstalk for executing the business logic" is incorrect. AWS Elastic Beanstalk is used for

  describing and provisioning resources not actually performing workflow functions within the application.


**References:**


https://aws.amazon.com/step-functions/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-api-gateway/

