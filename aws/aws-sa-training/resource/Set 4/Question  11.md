#### Question  11


**A Solutions Architect is designing an application that consists of AWS Lambda and Amazon RDS Aurora MySQL. The Lambda

function must use database credentials to authenticate to MySQL and security policy mandates that these credentials must

not be stored in the function code.**


**How can the Solutions Architect securely store the database credentials and make them available to the function?**


1: Store the credentials in AWS Key Management Service and use environment variables in the function code pointing to

KMS


2: Store the credentials in Systems Manager Parameter Store and update the function code and execution role


3: Use the AWSAuthenticationPlugin and associate an IAM user account in the MySQL database


4: Create an IAM policy and store the credentials in the policy. Attach the policy to the Lambda function execution role


Answer: 2


**Explanation:**


In this case the scenario requires that credentials are used for authenticating to MySQL. The credentials need to be

securely stored outside of the function code. Systems Manager Parameter Store provides secure, hierarchical storage for

configuration data management and secrets management.


You can easily reference the parameters from services including AWS Lambda as depicted in the diagram below:


- CORRECT "Store the credentials in Systems Manager Parameter Store and update the function code and execution role"

  is the correct answer.


- INCORRECT "Store the credentials in AWS Key Management Service and use environment variables in the function code

  pointing to KMS" is incorrect. You cannot store credentials in KMS, it is used for creating and managing encryption

  keys


- INCORRECT "Use the AWSAuthenticationPlugin and associate an IAM user account in the MySQL database" is incorrect. This

  is a great way to securely authenticate to RDS using IAM users or roles. However, in this case the scenario requires

  database credentials to be used by the function.


- INCORRECT "Create an IAM policy and store the credentials in the policy. Attach the policy to the Lambda function

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


https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html

