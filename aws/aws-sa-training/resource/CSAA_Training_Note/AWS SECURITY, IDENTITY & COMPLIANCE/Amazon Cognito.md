### Amazon Cognito


**AMAZON COGNITO GENERAL**


Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily.


Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps.


Your users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, or

Google.


**The two main components of AWS Cognito are user pools and identity pools:**


- User pools are user directories that provide sign-up and sign-in options for your app users.

- Identity pools enable you to grant your users access to other AWS services.


You can use identity pools and user pools separately or together.


AWS Cognito works with external identity providers that support SAML or OpenID Connect, social identity providers (such

as Facebook, Twitter, Amazon).


Cognito Identity provides temporary security credentials to access your app’s backend resources in AWS or any service

behind Amazon API Gateway.


You can use Amazon, Facebook, Twitter, Digits, Google and any other OpenID Connect compatible identity provider.


You can also integrate your own identity provider.


Cognito exposes server-side APIs.


Users can sign-up and sign-in using email, phone number, or user name.


End users of an application can also sign in with SMS-based MFA.


There is an import tool for migrating users into an Amazon Cognito User Pool.


**USER POOLS**


A user pool is a user directory in Amazon Cognito.


With a user pool, users can sign in to your web or mobile app through Amazon Cognito.


Users can also sign in through social identity providers like Facebook or Amazon, and through SAML identity providers.


Whether users sign in directly or through a third party, all members of the user pool have a directory profile that you

can access through an SDK.


**User pools provide:**


- Sign-up and sign-in services.

- A built-in, customizable web UI to sign in users.

- Social sign-in with Facebook, Google, and Login with Amazon, as well as sign-in with SAML identity providers from your

  user pool.

- User directory management and user profiles.

- Security features such as multi-factor authentication (MFA), checks for compromised credentials, account takeover

  protection, and phone and email verification.

- Customized workflows and user migration through AWS Lambda triggers.


After successfully authenticating a user, Amazon Cognito issues JSON web tokens (JWT) that you can use to secure and

authorize access to your own APIs, or exchange for AWS credentials.


**IDENTITY POOLS**


Amazon Cognito identity pools (federated identities) enable you to create unique identities for your users and federate

them with identity providers.


With an identity pool, you can obtain temporary, limited-privilege AWS credentials to access other AWS services. Amazon

Cognito identity pools support the following identity providers:


- Public providers: Login with Amazon (Identity Pools), Facebook (Identity Pools), Google


```

(Identity Pools).

```


- Amazon Cognito User Pools

- Open ID Connect Providers (Identity Pools)

- SAML Identity Providers (Identity Pools)

- Developer Authenticated Identities (Identity Pools)


**AMAZON COGNITO SYNC**


Amazon Cognito Sync is an AWS service and client library that enables cross-device syncing of application-related user

data.


You can use it to synchronize user profile data across mobile devices and the web without requiring your own backend.


The client libraries cache data locally so your app can read and write data regardless of device connectivity status.


When the device is online, you can synchronize data, and if you set up push sync, notify other devices immediately that

an update is available.

