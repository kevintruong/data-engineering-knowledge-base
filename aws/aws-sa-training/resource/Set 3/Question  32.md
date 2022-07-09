#### Question  32


**You work for Digital Cloud Training and have just created a number of IAM users in your AWS account. You need to

ensure that the users are able to make API calls to AWS services. What else needs to be done?**


1: Enable Multi-Factor Authentication for the users


2: Create a set of Access Keys for the users


3: Set a password for each user


4: Create a group and add the users to it


Answer: 2


**Explanation:**


Access keys are a combination of an access key ID and a secret access key and you can assign two active access keys to a

user at a time. These can be used to make programmatic calls to AWS when using the API in program code or at a command

prompt when using the AWS CLI or the AWS PowerShell tools.


- CORRECT "Create a set of Access Keys for the users" is the correct answer.


- INCORRECT "Enable Multi-Factor Authentication for the users" is incorrect. Multi-factor authentication can be used to

  control access to AWS service APIs but the question is not asking how to better secure the calls but just being able

  to make them.


- INCORRECT "Set a password for each user" is incorrect. A password is needed for logging into the console but not for

  making API calls to AWS services. Similarly you don’t need to create a group and add the users to it to provide access

  to make API calls to AWS services.


- INCORRECT "Create a group and add the users to it" is incorrect as you need access keys for programmatic access using

  the API.


**References:**


https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/

