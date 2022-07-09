#### Question  31


**A mobile app uploads usage information to a database. Amazon Cognito is being used for authentication, authorization

and user management and users sign-in with Facebook IDs.**


**In order to securely store data in DynamoDB, the design should use temporary AWS credentials. What feature of Amazon

Cognito is used to obtain temporary credentials to access AWS services?**


1: User Pools


2: Identity Pools


3: Key Pairs


4: SAML Identity Providers


**Answer: 2**


**Explanation:**


Amazon Cognito identity pools provide temporary AWS credentials for users who are guests (unauthenticated)

and for users who have been authenticated and received a token. An identity pool is a store of user identity data

specific to your account.


With an identity pool, users can obtain temporary AWS credentials to access AWS services, such as Amazon S3 and

DynamoDB.


- CORRECT "Identity Pools" is the correct answer.


- INCORRECT "User Pools" is incorrect. A user pool is a user directory in Amazon Cognito. With a user pool, users can

  sign in to web or mobile apps through Amazon Cognito, or federate through a third-party identity provider (IdP).


- INCORRECT "Key Pairs" is incorrect. Key pairs are used in Amazon EC2 for access to instances.


- INCORRECT "SAML Identity Providers" is incorrect. SAML Identity Providers are supported IDPs for identity pools but

  cannot be used for gaining temporary credentials for AWS services.


**References:**


https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

