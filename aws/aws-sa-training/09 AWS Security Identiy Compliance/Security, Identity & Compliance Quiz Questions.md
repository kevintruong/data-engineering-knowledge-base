### Security, Identity & Compliance Quiz Questions

Answers and explanations are provided below after the last question in this section.

**Question 1:**

A company needs to deploy virtual desktops for its customers in an AWS VPC, and would like to
leverage their existing on-premise security principles. AWS Workspaces will be used as the virtual desktop solution.

Which set of AWS services and features will meet the company’s requirements?

```
A. A VPN connection. AWS Directory Services
B. A VPN connection, VPC NACLs and Security Groups
C. A VPN connection, VPC NACLs and Security Groups
D. Amazon EC2, and AWS IAM
```

**Question 2:**

To improve security in your AWS account you have decided to enable multi-factor authentication
(MFA). You can authenticate using an MFA device in which two ways? (choose 2)

```
A. Locally to EC2 instances
B. Through the AWS Management Console
C. Using biometrics
D. Using a key pair
E. Using the AWS API
```

**Question 3:**

Your company would like to restrict the ability of most users to change their own passwords whilst
continuing to allow a select group of users within specific user groups.

What is the best way to achieve this? (choose 2)

```
A. Under the IAM Password Policy deselect the option to allow users to change their own
passwords
B. Create an IAM Policy that grants users the ability to change their own password and attach
it to the groups that contain the users
C. Create an IAM Role that grants users the ability to change their own password and attach it
to the groups that contain the users
D. Create an IAM Policy that grants users the ability to change their own password and attach
it to the individual user accounts
E. Disable the ability for all users to change their own passwords using the AWS Security Token
Service
```
**Question 4:**

Your company has started using the AWS CloudHSM for secure key storage. A recent administrative
error resulted in the loss of credentials to access the CloudHSM. You need access to data that was
encrypted using keys stored on the hardware security module.

How can you recover the keys that are no longer accessible?


```
A. There is no way to recover your keys if you lose your credentials
B. Log a case with AWS support and they will use MFA to recover the credentials
C. Restore a snapshot of the CloudHSM
D. Reset the CloudHSM device and create a new set of credentials
```
**Question 5:**

The AWS Acceptable Use Policy describes permitted and prohibited behavior on AWS and includes
descriptions of prohibited security violations and network abuse. According to the policy, what is
AWS's position on penetration testing?

```
A. AWS do not allow any form of penetration testing
B. AWS allow penetration testing by customers on their own VPC resources
C. AWS allow penetration for some resources with prior authorization
D. AWS allow penetration testing for all resources
```
**Question 6:**

You have been asked to come up with a solution for providing single sign-on to existing staff in your
company who manage on-premise web applications and now need access to the AWS management
console to manage resources in the AWS cloud.

Which product combinations provide the best solution to achieve this requirement?

```
A. Use your on-premise LDAP directory with IAM
B. Use IAM and MFA
C. Use the AWS Secure Token Service (STS) and SAML
D. Use IAM and Amazon Cognito
```
**Question 7:**

You are a Developer working for Digital Cloud Training. You are planning to write some code that
creates a URL that lets users who sign in to your organization's network securely access the AWS
Management Console. The URL will include a sign-in token that you get from AWS that
authenticates the user to AWS. You are using Microsoft Active Directory Federation Services as your
identity provider (IdP) which is compatible with SAML 2.0.

Which of the steps below will you need to include when developing your custom identity broker?
(choose 2)

```
A. Generate a pre-signed URL programmatically using the AWS SDK for Java or the AWS SDK
for .NET
B. Call the AWS Security Token Service (AWS STS) AssumeRole or GetFederationToken API
operations to obtain temporary security credentials for the user
C. Delegate access to the IdP through the "Configure Provider" wizard in the IAM console
D. Call the AWS federation endpoint and supply the temporary security credentials to request
a sign-in token
E. Assume an IAM Role through the console or programmatically with the AWS CLI, Tools for
Windows PowerShell or API
```
**Question 8:**

A health club is developing a mobile fitness app that allows customers to upload statistics and view


their progress. Amazon Cognito is being used for authentication, authorization and user
management and users will sign-in with Facebook IDs.

In order to securely store data in DynamoDB, the design should use temporary AWS credentials.
What feature of Amazon Cognito is used to obtain temporary credentials to access AWS services?

```
A. User Pools
B. Identity Pools
C. SAML Identity Providers
D. Key Pairs
```

**SECURITY, IDENTITY & COMPLIANCE - ANSWERS**

**Question 1 answer: A**

Explanation:

```
A security principle is an individual identity such as a user account within a directory. The AWS
Directory service includes: Active Directory Service for Microsoft Active Directory, Simple AD, AD
Connector. One of these services may be ideal depending on detailed requirements. The Active
Directory Service for Microsoft AD and AD Connector both require a VPN or Direct Connect
connection.
A VPN with NACLs and security groups will not deliver the required solution. AWS Directory
Service with IAM or EC2 with IAM are also not sufficient for leveraging on-premise security
principles. You must have a VPN.
```
**Question 2 answer: A,E**

Explanation:

```
You can authenticate using an MFA device in the following ways:
```
- Through the AWS Management Console – the user is prompted for a user name, password
    and authentication code
- Using the AWS API – restrictions are added to IAM policies and developers can request
    temporary security credentials and pass MFA parameters in their AWS STS API requests
- Using the AWS CLI by obtaining temporary security credentials from STS (aws sts get-
    session-token)

**Question 3 answer: A,B**

Explanation:

```
A password policy can be defined for enforcing password length, complexity etc. (applies to all
users).
You can allow or disallow the ability to change passwords using an IAM policy and you should
attach this to the group that contains the users, not to the individual users themselves.
You cannot use an IAM role to perform this function.
The AWS STS is not used for controlling password policies.
```
**Question 4 answer: A**

Explanation:

```
Amazon does not have access to your keys or credentials and therefore has no way to recover
your keys if you lose your credentials.
```
**Question 5 answer: C**

Explanation:

```
Permission is required for all penetration tests.
You must complete and submit the AWS Vulnerability / Penetration Testing Request Form to
```

```
request authorization for penetration testing to or originating from any AWS resources.
There is a limited set of resources on which penetration testing can be performed.
```
**Question 6 answer: C**

Explanation:

```
Single sign-on using federation allows users to login to the AWS console without assigning IAM
credentials.
The AWS Security Token Service (STS) is a web service that enables you to request temporary,
limited-privilege credentials for IAM users or for users that you authenticate (such as federated
users from an on-premise directory).
Federation (typically Active Directory) uses SAML 2.0 for authentication and grants temporary
access based on the users AD credentials. The user does not need to be a user in IAM.
You cannot use your on-premise LDAP directory with IAM, you must use federation.
Enabling multi-factor authentication (MFA) for IAM is not a federation solution.
Amazon Cognito is used for authenticating users to web and mobile apps not for providing single
sign-on between on-premises directories and the AWS management console.
```
**Question 7 answer: B,D**

Explanation:

```
The aim of this solution is to create a single sign-on solution that enables users signed in to the
organization's Active Directory service to be able to connect to AWS resources. When developing
a custom identity broker you use the AWS STS service.
The AWS Security Token Service (STS) is a web service that enables you to request temporary,
limited-privilege credentials for IAM users or for users that you authenticate (federated users).
The steps performed by the custom identity broker to sign users into the AWS management
console are:
```
1. Verify that the user is authenticated by your local identity system
2. Call the AWS Security Token Service (AWS STS) AssumeRole or GetFederationToken API
    operations to obtain temporary security credentials for the user
3. Call the AWS federation endpoint and supply the temporary security credentials to request
    a sign-in token
4. Construct a URL for the console that includes the token
5. Give the URL to the user or invoke the URL on the user's behalf
You cannot generate a pre-signed URL for this purpose using SDKs, delegate access through the
IAM console or directly assume IAM roles.

**Question 8 answer: B**

Explanation:

```
With an identity pool, users can obtain temporary AWS credentials to access AWS services, such
as Amazon S3 and DynamoDB.
A user pool is a user directory in Amazon Cognito. With a user pool, users can sign in to web or
```

mobile apps through Amazon Cognito, or federate through a third-party identity provider (IdP).

SAML Identity Providers are supported IDPs for identity pools but cannot be used for gaining
temporary credentials for AWS services.

Key pairs are used in Amazon EC2 for access to instances.