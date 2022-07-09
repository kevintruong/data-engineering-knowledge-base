#### Question  50


**The development team at your company have created a new mobile application that will be used by users to access

confidential data. The developers have used Amazon Cognito for authentication, authorization, and user management. Due

to the sensitivity of the data, there is a requirement to add another method of authentication in addition to a username

and password.**


**You have been asked to recommend the best solution. What is your recommendation?**


1: Use multi-factor authentication (MFA) with a Cognito user pool


2: Integrate a third-party identity provider (IdP)


3: Enable multi-factor authentication (MFA) in IAM


4: Integrate IAM with a user pool in Cognito


Answer: 1


**Explanation:**


You can use MFA with a Cognito user pool (not in IAM) and this satisfies the requirement.


```

Production Stage

```


```

CACHE: ENABLED

SIZE: 0. 5 GB

ENCRYPTION: ON

TTL: 900

```


```

MyAPI

Users API^ Cache Endpoint

```


```

Check cache first

```


```

1 2

```


```

If not in the cache (cache

miss), go to backend

```


A user pool is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app

through Amazon Cognito. Your users can also sign in through social identity providers like Facebook or Amazon, and

through SAML identity providers.


- CORRECT "Use multi-factor authentication (MFA) with a Cognito user pool" is the correct answer.


- INCORRECT "Integrate a third-party identity provider (IdP)" is incorrect is not the best solution as a Cognito user

  pool can satisfy the requirements along with MFA.


- INCORRECT "Enable multi-factor authentication (MFA) in IAM" is incorrect as a Cognito user pool should be used for

  this use case.


- INCORRECT "Integrate IAM with a user pool in Cognito" is incorrect. Integrating IAM with a Cognito user pool or

  integrating a 3rd party IdP does not add another factor of authentication – “factors” include something you know (e.g.

  password), something you have (e.g. token device), and something you are (e.g. retina scan or fingerprint).


**References:**


https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/amazon-cognito/

