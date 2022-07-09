#### Question  48


**A Solutions Architect needs to work programmatically with IAM. Which feature of IAM allows direct access to the IAM

web service using HTTPS to call service actions and what is the method of authentication that must be used? (Select

TWO)**


1: OpenID Connect


2: Query API


3: API Gateway


4: Access key ID and secret access key


5: IAM role


**Answer: 2,4**


**Explanation:**


AWS recommend that you use the AWS SDKs to make programmatic API calls to IAM. However, you can also use the IAM Query

API to make direct calls to the IAM web service. An access key ID and secret access key must be used for authentication

when using the Query API.


- CORRECT "Query API" is a correct answer.


- CORRECT "Access key ID and secret access key" is also a correct answer.


- INCORRECT "OpenID Connect" is incorrect. OpenID Connect is a provider for connecting external directories.


- INCORRECT "API Gateway" is incorrect. API gateway is a separate service for accepting and processing API calls.


- INCORRECT "IAM role" is incorrect. An IAM role is not used for authentication to the Query API.


**References:**


https://docs.aws.amazon.com/IAM/latest/APIReference/iam-api.pdf


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/

