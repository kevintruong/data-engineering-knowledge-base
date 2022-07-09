#### Question  43


**A Solutions Architect is creating a URL that lets users who sign in to the organization’s network securely access the

AWS Management Console. The URL will include a sign-in token that authenticates the user to AWS. Microsoft Active

Directory Federation Services is being used as the identity provider (IdP).**


**Which of the steps below will the Solutions Architect need to include when developing the custom identity broker? (

Select TWO)**


1: Call the AWS federation endpoint and supply the temporary security credentials to request a sign-in token


2: Call the AWS Security Token Service (AWS STS) AssumeRole or GetFederationToken API operations to obtain temporary

security credentials for the user


3: Assume an IAM Role through the console or programmatically with the AWS CLI, Tools for Windows PowerShell or API


4: Generate a pre-signed URL programmatically using the AWS SDK for Java or the AWS SDK for .NET


5: Delegate access to the IdP through the "Configure Provider" wizard in the IAM console


**Answer: 1,2**


**Explanation:**


The aim of this solution is to create a single sign-on solution that enables users signed in to the organization’s

Active Directory service to be able to connect to AWS resources. When developing a custom identity broker you use the

AWS STS service.


The AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege

credentials for IAM users or for users that you authenticate (federated users). The steps performed by the custom

identity broker to sign users into the AWS management console are:


- Verify that the user is authenticated by your local identity system

- Call the AWS Security Token Service (AWS STS) AssumeRole or GetFederationToken API operations to obtain temporary

  security credentials for the user

- Call the AWS federation endpoint and supply the temporary security credentials to request a sign-in token

- Construct a URL for the console that includes the token

- Give the URL to the user or invoke the URL on the user’s behalf


- CORRECT "Call the AWS federation endpoint and supply the temporary security credentials to request a sign- in token"

  is the correct answer.


- CORRECT "Call the AWS Security Token Service (AWS STS) AssumeRole or GetFederationToken API operations to obtain

  temporary security credentials for the user" is the correct answer.


- INCORRECT "Assume an IAM Role through the console or programmatically with the AWS CLI, Tools for Windows PowerShell

  or API" is incorrect as this is an example of federation so assuming a role is the wrong procedure.


- INCORRECT "Generate a pre-signed URL programmatically using the AWS SDK for Java or the AWS SDK for .NET" is

  incorrect. You cannot generate a pre-signed URL for this purpose using SDKs, delegate access through the IAM console

  or directly assume IAM roles.


- INCORRECT "Delegate access to the IdP through the "Configure Provider" wizard in the IAM console" is incorrect as this

  is not something you can do


**References:**


https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/

