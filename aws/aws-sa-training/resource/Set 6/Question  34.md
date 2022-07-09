#### Question  34


**A Solutions Architect is designing the system monitoring and deployment layers of a serverless application. The system

monitoring layer will manage system visibility through recording logs and metrics and the deployment layer will deploy

the application stack and manage workload changes through a release management process.**


**The Architect needs to select the most appropriate AWS services for these functions. Which services and frameworks

should be used for the system monitoring and deployment layers? (Select TWO)**


1: Use AWS CloudTrail for consolidating system and application logs and monitoring custom metrics


2: Use AWS X-Ray to package, test, and deploy the serverless application stack


3: Use AWS SAM to package, test, and deploy the serverless application stack


4: Use Amazon CloudWatch for consolidating system and application logs and monitoring custom metrics


5: Use AWS Lambda to package, test, and deploy the serverless application stack


**Answer: 3,4**


**Explanation:**


AWS Serverless Application Model (AWS SAM) is an extension of AWS CloudFormation that is used to package, test, and

deploy serverless applications.


With Amazon CloudWatch, you can access system metrics on all the AWS services you use, consolidate system and

application level logs, and create business key performance indicators (KPIs) as custom metrics for your specific needs.


- CORRECT "Use AWS SAM to package, test, and deploy the serverless application stack" is a correct answer.


- CORRECT "Use Amazon CloudWatch for consolidating system and application logs and monitoring custom metrics" is also a

  correct answer.


- INCORRECT "Use AWS CloudTrail for consolidating system and application logs and monitoring custom metrics" is

  incorrect as CloudTrail is used for auditing not performance monitoring.


- INCORRECT "Use AWS X-Ray to package, test, and deploy the serverless application stack" is incorrect. AWS X- Ray lets

  you analyze and debug serverless applications by providing distributed tracing and service maps to easily identify

  performance bottlenecks by visualizing a request end-to-end.


- INCORRECT "Use AWS Lambda to package, test, and deploy the serverless application stack" is incorrect. AWS Lambda is

  used for executing your code as functions, it is not used for packaging, testing and deployment. AWS Lambda is used

  with AWS SAM.


**References:**


https://docs.aws.amazon.com/lambda/latest/dg/serverless_app.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-

tools/amazon-cloudwatch/

