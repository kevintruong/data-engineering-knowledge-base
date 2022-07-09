#### Question  3


**A tool needs to analyze data stored in an Amazon S3 bucket. Processing the data takes a few seconds and results are

then written to another S3 bucket. Less than 256 MB of memory is needed to run the process. What would be the MOST

cost-effective compute solutions for this use case?**


1: AWS Fargate tasks


2: AWS Lambda functions


3: Amazon EC2 spot instances


4: Amazon Elastic Beanstalk


Answer: 2


**Explanation:**


AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.

Lambda has a maximum execution time of 900 seconds and memory can be allocated up to 3008 MB. Therefore, the most

cost-effective solution will be AWS Lambda.


- CORRECT "AWS Lambda functions" is the correct answer.


- INCORRECT "AWS Fargate tasks" is incorrect. Fargate runs Docker containers and is serverless. However, you do pay for

  the running time of the tasks so it will not be as cost-effective.


- INCORRECT "Amazon EC2 spot instances" is incorrect. EC2 instances must run continually waiting for jobs to process so

  even with spot this would be less cost-effective (and subject to termination).


- INCORRECT "Amazon Elastic Beanstalk" is incorrect. This services also relies on Amazon EC2 instances so would not be

  as cost-effective.


**References:**


https://aws.amazon.com/lambda/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/

