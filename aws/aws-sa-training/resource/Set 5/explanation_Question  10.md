**Explanation:**

With MySQL, authentication is handled by AWSAuthenticationPlugin—an AWS-provided plugin that works seamlessly with IAM

to authenticate your IAM users. Connect to the DB instance and issue the CREATE USER statement, as shown in the

following example.

CREATE USER jane_doe IDENTIFIED WITH AWSAuthenticationPlugin AS 'RDS';

The IDENTIFIED WITH clause allows MySQL to use the AWSAuthenticationPlugin to authenticate the database account (

jane_doe). The AS 'RDS' clause refers to the authentication method, and the specified database account should have the

same name as the IAM user or role. In this example, both the database account and the IAM user or role are named

jane_doe.

- ✅ :  "Create the MySQL user accounts to use the AWSAuthenticationPlugin with IAM" is the correct answer.

- ❌ :  "Configure the MySQL databases to use the AWS Security Token Service (STS)" is incorrect. You cannot

  configure MySQL to directly use the AWS STS.

- ❌ :  "Configure the application to use the AUTH command to send a unique password" is incorrect. This is used

  with Redis databases, not with RDS databases.

- ❌ :  "Configure the MySQL databases to use AWS KMS data encryption keys" is incorrect. Data encryption keys are

  used for data encryption not management of connections strings.

**References:**

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----

- #aws_security_token_service #<https://docs.aws.amazon.com/amazonrds/latest/userguide/usingwithrds.iamdbauth.dbaccounts.html> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/> #awsauthenticationplugin #iam_users
