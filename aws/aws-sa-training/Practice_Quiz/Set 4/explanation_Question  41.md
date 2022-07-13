*

**Explanation:**

Single sign-on using federation allows users to login to the AWS console without assigning IAM credentials. The AWS

Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege

credentials for IAM users or for users that you authenticate (such as federated users from an on-premise directory).

Federation (typically Active Directory) uses SAML 2.0 for authentication and grants temporary access based on the users

AD credentials. The user does not need to be a user in IAM.

* ✅ :  "Use the AWS Secure Token Service (STS) and SAML" is the correct answer.

* ❌ :  "Use IAM and Amazon Cognito" is incorrect. Amazon Cognito is used for authenticating users to web and mobile

  apps not for providing single sign-on between on-premises directories and the AWS management console.

* ❌ :  "Use your on-premise LDAP directory with IAM" is incorrect. You cannot use your on-premise LDAP directory

  with IAM, you must use federation.

* ❌ :  "Use IAM and MFA" is incorrect. Enabling multi-factor authentication (MFA) for IAM is not a federation

  solution..

**References:**

<https://aws.amazon.com/identity/federation/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/aws-iam/

----
* #<https://aws.amazon.com/identity/federation/> #iam_credentials #aws_secure_token_service #use_iam #aws_management_console
