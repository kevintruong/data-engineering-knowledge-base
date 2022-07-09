#### Question  26


**A Python application is currently running on Amazon ECS containers using the Fargate launch type. An ALB has been

created with a Target Group that routes incoming connections to the ECS-based application. The application will be used

by consumers who will authenticate using federated OIDC compliant Identity Providers such as Google and Facebook. The

users must be securely authenticated on the front-end before they access the secured portions of the application.**


**How can this be configured using an ALB?**


1: The only option is to use SAML with Amazon Cognito on the ALB


2: This can be done on the ALB by creating an authentication action on a listener rule that configures an Amazon Cognito

user pool with the social IdP


3: This cannot be done on an ALB; you’ll need to authenticate users on the back-end with AWS Single Sign-On

(SSO) integration


4: This cannot be done on an ALB; you’ll need to use another layer in front of the ALB


**Answer: 2**


**Explanation:**


ALB supports authentication from OIDC compliant identity providers such as Google, Facebook and Amazon. It is

implemented through an authentication action on a listener rule that integrates with Amazon Cognito to create user

pools.


SAML can be used with Amazon Cognito but this is not the only option.


- CORRECT "This can be done on the ALB by creating an authentication action on a listener rule that configures an Amazon

  Cognito user pool with the social IdP" is the correct answer.


- INCORRECT "The only option is to use SAML with Amazon Cognito on the ALB" is incorrect as explained above.


- INCORRECT "This cannot be done on an ALB; you’ll need to authenticate users on the back-end with AWS Single Sign-On (

  SSO) integration" is incorrect as explained above.


- INCORRECT "This cannot be done on an ALB; you’ll need to use another layer in front of the ALB" is incorrect as

  explained above.


**References:**


https://aws.amazon.com/blogs/aws/built-in-authentication-in-alb/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

