#### Question  53


**A Solutions Architect is developing a new web application on AWS that needs to be able to scale to support

unpredictable workloads. The Architect prefers to focus on value-add activities such as software development and product

roadmap development rather than provisioning and managing instances.**


**Which solution is most appropriate for this use case?**


1: Amazon API Gateway and AWS Lambda


2: Elastic Load Balancing with Auto Scaling groups and Amazon EC2


3: Amazon CloudFront and AWS Lambda


4: Amazon API Gateway and Amazon EC2


Answer: 1


**Explanation:**


The Architect requires a solution that removes the need to manage instances. Therefore it must be a serverless service

which rules out EC2. The two remaining options use AWS Lambda at the back-end for processing. Though CloudFront can

trigger Lambda functions it is more suited to customizing content delivered from an origin. Therefore, API Gateway with

AWS Lambda is the most workable solution presented.


This solution will likely require other services such as S3 for content and a database service. Refer to the link below

for an example scenario that uses API Gateway and AWS Lambda with other services to create a serverless web application.


- CORRECT "Amazon API Gateway and AWS Lambda" is the correct answer.


- INCORRECT "Elastic Load Balancing with Auto Scaling groups and Amazon EC2" is incorrect as this option requires

  managing instances.


- INCORRECT "Amazon CloudFront and AWS Lambda" is incorrect as API Gateway is a better fit for the front end of this

  serverless web application.


- INCORRECT "Amazon API Gateway and Amazon EC2" is incorrect as this option requires managing instances.


**References:**


https://aws.amazon.com/getting-started/projects/build-serverless-web-app-lambda-apigateway-s3-

dynamodb-cognito/

