##### Question 6 answer: C


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

