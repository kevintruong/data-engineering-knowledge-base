*

**Explanation:**

The aim of this solution is to create a single sign-on solution that enables users signed in to the organization’s

Active Directory service to be able to connect to AWS resources. When developing a custom identity broker you use the

AWS STS service.

The AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege

credentials for IAM users or for users that you authenticate (federated users). The steps performed by the custom

identity broker to sign users into the AWS management console are:

* Verify that the user is authenticated by your local identity system

* Call the AWS Security Token Service (AWS STS) AssumeRole or GetFederationToken API operations to obtain temporary

  security credentials for the user

* Call the AWS federation endpoint and supply the temporary security credentials to request a sign-in token

* Construct a URL for the console that includes the token

* Give the URL to the user or invoke the URL on the user’s behalf

* ✅ :  "Call the AWS federation endpoint and supply the temporary security credentials to request a sign- in token"

  is the correct answer.

* ✅ :  "Call the AWS Security Token Service (AWS STS) AssumeRole or GetFederationToken API operations to obtain

  temporary security credentials for the user" is the correct answer.

* ❌ :  "Assume an IAM Role through the console or programmatically with the AWS CLI, Tools for Windows PowerShell

  or API" is incorrect as this is an example of federation so assuming a role is the wrong procedure.

* ❌ :  "Generate a pre-signed URL programmatically using the AWS SDK for Java or the AWS SDK for .NET" is

  incorrect. You cannot generate a pre-signed URL for this purpose using SDKs, delegate access through the IAM console

  or directly assume IAM roles.

* ❌ :  "Delegate access to the IdP through the "Configure Provider" wizard in the IAM console" is incorrect as this

  is not something you can do

**References:**

<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-iam/

----
* #aws_security_token_service #aws_sts_service #custom_identity_broker #identity_broker #aws_federation_endpoint
