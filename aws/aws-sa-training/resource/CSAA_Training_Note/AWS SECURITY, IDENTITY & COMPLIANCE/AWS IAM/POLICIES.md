#### POLICIES


Policies are documents that define permissions and can be applied to users, groups and roles.


Policy documents are written in JSON (key value pair that consists of an attribute and a value).


All permissions are implicitly denied by default.


The most restrictive policy is applied.


The IAM policy simulator is a tool to help you understand, test, and validate the effects of access control policies.


The Condition element can be used to apply further conditional logic.


The diagram below provides some more information on the relationship between IAM roles, users, groups and policies.


**SECURITY TOKEN SERVICE (STS)**


The AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege

credentials for IAM users or for users that you authenticate (federated users).


By default, AWS STS is available as a global service, and all AWS STS requests go to a single endpoint

at https://sts.amazonaws.com


You can optionally send your AWS STS requests to endpoints in any region (can reduce latency).


All regions are enabled for STS by default but can be disabled.


The region in which temporary credentials are requested must be enabled.


Credentials will always work globally.


STS supports AWS CloudTrail, which records AWS calls for your AWS account and delivers log files to an S3 bucket.


**Temporary security credentials work almost identically to long-term access key credentials that IAM users can use,

with the following differences:**


- Temporary security credentials are short-term.

- They can be configured to last anywhere from a few minutes to several hours.

- After the credentials expire, AWS no longer recognizes them or allows any kind of access to API requests made with

  them.

- Temporary security credentials are not stored with the user but are generated dynamically and provided to the user

  when requested.

- When (or even before) the temporary security credentials expire, the user can request new credentials, as long as the

  user requesting them still has permission to do so.


**Advantages of STS are:**


- You do not have to distribute or embed long-term AWS security credentials with an application.

- You can provide access to your AWS resources to users without having to define an AWS identity for them (temporary

  security credentials are the basis for IAM Roles and ID Federation).

- The temporary security credentials have a limited lifetime, so you do not have to rotate them or explicitly revoke

  them when they’re no longer needed.



- After temporary security credentials expire, they cannot be reused (you can specify how long the credentials are valid

  for, up to a maximum limit).


**The AWS STS API action returns temporary security credentials that consist of:**


- An access key which consists of an access key ID and a secret ID.

- A session token.

- Expiration or duration of validity.

- Users (or an application that the user runs) can use these credentials to access your resources.


**With STS you can request a session token using one of the following APIs:**


- AssumeRole – can only be used by IAM users (can be used for MFA).

- AssumeRoleWithSAML – can be used by any user who passes a SAML authentication response that indicates authentication

  from a known (trusted) identity provider.

- AssumeRoleWithWebIdentity – can be used by a user who passes a web identity token that indicates authentication from a

  known (trusted) identity provider.

- GetSessionToken – can be used by an IAM user or AWS account root user (can be used for MFA).

- GetFederationToken – can be used by an IAM user or AWS account root user.


AWS recommends using Cognito for identity federation with Internet identity providers.


**Users can come from three sources:**


**Federation (typically AD):**


- Uses SAML 2.0.

- Grants temporary access based on the users AD credentials.

- Does not need to be a user in IAM.

- Single sign-on allows users to login to the AWS console without assigning IAM credentials.


**Federation with Mobile Apps:**


- Use Facebook/Amazon/Google or other OpenID providers to login.


**Cross Account Access:**


- Lets users from one AWS account access resources in another.

- To make a request in a different account the resource in that account must have an attached resource-based policy with

  the permissions you need.

- Or you must assume a role (identity-based policy) within that account with the permissions you need.


**There are a couple of ways STS can be used:**


**Scenario 1:**


1. Develop an Identity Broker to communicate with LDAP and AWS STS.

2. Identity Broker always authenticates with LDAP first, then with AWS STS.

3. Application then gets temporary access to AWS resources.


**Scenario 2:**


1. Develop an Identity Broker to communicate with LDAP and AWS STS.

2. Identity Broker authenticates with LDAP first, then gets an IAM role associated with the user.

3. Application then authenticates with STS and assumes that IAM role.

4. Application uses that IAM role to interact with the service.

