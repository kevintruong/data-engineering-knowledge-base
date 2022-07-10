#### Question  26

**A Python application is currently running on Amazon ECS containers using the Fargate launch type. An ALB has been

created with a Target Group that routes incoming connections to the ECS-based application. The application will be used

by consumers who will authenticate using federated OIDC compliant Identity Providers such as Google and Facebook. The

users must be securely authenticated on the front-end before they access the secured portions of the application.**

**How can this be configured using an ALB?**

- [ ] The only option is to use SAML with Amazon Cognito on the ALB

- [x] This can be done on the ALB by creating an authentication action on a listener rule that configures an Amazon Cognito

user pool with the social IdP

- [ ] This cannot be done on an ALB; you’ll need to authenticate users on the back-end with AWS Single Sign-On

(SSO) integration

- [ ] This cannot be done on an ALB; you’ll need to use another layer in front of the ALB

*

- hasExplain:: [[explanation_Question  26.md]]
