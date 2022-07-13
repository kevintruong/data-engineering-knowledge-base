##### Question 7

You are a Developer working for Digital Cloud Training. You are planning to
write some code that creates a URL that lets

users who sign in to your organization's network securely access the AWS
Management Console. The URL will include a

sign-in token that you get from AWS that authenticates the user to AWS. You are
using Microsoft Active Directory

Federation Services as your identity provider (IdP) which is compatible with
SAML 2.0.

Which of the steps below will you need to include when developing your custom
identity broker?

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

