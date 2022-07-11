**Explanation:**

In this case the scenario requires that credentials are used for authenticating to MySQL. The credentials need to be

securely stored outside of the function code. Systems Manager Parameter Store provides secure, hierarchical storage for

configuration data management and secrets management.

You can easily reference the parameters from services including AWS Lambda as depicted in the diagram below:

- ✅ :  "Store the credentials in Systems Manager Parameter Store and update the function code and execution role"

  is the correct answer.

- ❌ :  "Store the credentials in AWS Key Management Service and use environment variables in the function code

  pointing to KMS" is incorrect. You cannot store credentials in KMS, it is used for creating and managing encryption

  keys

- ❌ :  "Use the AWSAuthenticationPlugin and associate an IAM user account in the MySQL database" is incorrect. This

  is a great way to securely authenticate to RDS using IAM users or roles. However, in this case the scenario requires

  database credentials to be used by the function.

- ❌ :  "Create an IAM policy and store the credentials in the policy. Attach the policy to the Lambda function

  execution role" is incorrect. You cannot store credentials in IAM policies.

```

AWS Lambda

```

```

Amazon RDS

```

```

Parameter

Store

```

```

Retrieve database

connection string

```

**References:**

<https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html>

----

- #aws_key_management_service #aws_lambda #database_credentials #credentials #amazon_rds
