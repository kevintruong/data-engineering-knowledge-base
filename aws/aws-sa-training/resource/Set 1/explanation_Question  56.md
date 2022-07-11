**Explanation:**

The most secure method is to use an IAM role so you don’t need to embed any credentials in code and can tightly control

the services that your Lambda function can access. You need to assign the role to the Lambda function, NOT to the

DynamoDB table.

- ✅ :  "Create an identity and access management (IAM) role with the necessary permissions to access the DynamoDB

  table, and assign the role to the Lambda function" is the correct answer.

- ❌ :  "Create a DynamoDB username and password and give them to the Developer to use in the Lambda function" is

  incorrect. You cannot create a user name and password for DynamoDB and it would be bad practice to store these in the

  function code if you could.

- ❌ :  "Create an identity and access management (IAM) user and create access and secret keys for the user. Give

  the user the necessary permissions to access the DynamoDB table. Have the Developer use these keys to access the

  resources" is incorrect. You should not use an access key and secret ID to access DynamoDB. Again, this means

  embedding credentials in code which should be avoided.

- ❌ :  "Create an identity and access management (IAM) role allowing access from AWS Lambda and assign the role to

  the DynamoDB table" is incorrect as the role should be assigned to the Lambda function so it can access the table.

**References:**

<https://aws.amazon.com/blogs/security/how-to-create-an-aws-iam-policy-to-grant-aws-lambda-access-to-an>-

amazon-dynamodb-table/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- dynamodb/

----

- #dynamodb #dynamodb_table #aws_lambda #<https://aws.amazon.com/blogs/security/how-to-create-an-aws-iam-policy-to-grant-aws-lambda-access-to-an>>- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>>-
