*

**Explanation:**

ALB supports authentication from OIDC compliant identity providers such as Google, Facebook and Amazon. It is

implemented through an authentication action on a listener rule that integrates with Amazon Cognito to create user

pools.

SAML can be used with Amazon Cognito but this is not the only option.

* ✅ :  "This can be done on the ALB by creating an authentication action on a listener rule that configures an Amazon

  Cognito user pool with the social IdP" is the correct answer.

* ❌ :  "The only option is to use SAML with Amazon Cognito on the ALB" is incorrect as explained above.

* ❌ :  "This cannot be done on an ALB; you’ll need to authenticate users on the back-end with AWS Single Sign-On (

  SSO) integration" is incorrect as explained above.

* ❌ :  "This cannot be done on an ALB; you’ll need to use another layer in front of the ALB" is incorrect as

  explained above.

**References:**

<https://aws.amazon.com/blogs/aws/built-in-authentication-in-alb/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----
* #alb #aws_single_sign #amazon_cognito #cognito_user_pool #authentication
