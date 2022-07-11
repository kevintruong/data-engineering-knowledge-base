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

- ✅ :  "Use multi-factor authentication (MFA) with a Cognito user pool" is the correct answer.

- ❌ :  "Integrate a third-party identity provider (IdP)" is incorrect is not the best solution as a Cognito user

  pool can satisfy the requirements along with MFA.

- ❌ :  "Enable multi-factor authentication (MFA) in IAM" is incorrect as a Cognito user pool should be used for

  this use case.

- ❌ :  "Integrate IAM with a user pool in Cognito" is incorrect. Integrating IAM with a Cognito user pool or

  integrating a 3rd party IdP does not add another factor of authentication – “factors” include something you know (e.g.

  password), something you have (e.g. token device), and something you are (e.g. retina scan or fingerprint).

**References:**

<https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity>-

compliance/amazon-cognito/

----

- #multi_-_factor_authentication #amazon_cognito #authentication #cognito_user #saml_identity_providers
