**Explanation:**

Environment variables for Lambda functions enable you to dynamically pass settings to your function code and libraries,

without making changes to your code. Environment variables are key-value pairs that you create and modify as part of

your function configuration, using either the AWS Lambda Console, the AWS Lambda CLI or the AWS Lambda SDK. You can use

environment variables to help libraries know what directory to install files in, where to store outputs, store

connection and logging settings, and more.

- ✅ :  "Use encryption helpers that leverage AWS Key Management Service to store the sensitive information as

  Ciphertext" is the correct answer.

- ❌ :  "This cannot be done, only the environment variables that relate to the Lambda function itself can be

  encrypted" is incorrect as there is a solution to this requirement.

- ❌ :  "There is no need to make any changes as all environment variables are encrypted by default with AWS Lambda"

  is incorrect. When you deploy your Lambda function, all the environment variables you’ve specified are encrypted by

  default after, but not during, the deployment process. They are then decrypted automatically by AWS Lambda when the

  function is invoked. If you need to store sensitive information in an environment variable, you should encrypt that

  information before deploying your Lambda function. The Lambda console makes that easier for you by providing

  encryption helpers that leverage AWS Key Management Service to store that sensitive information as Ciphertext.

- ❌ :  "Store the environment variables in an encrypted DynamoDB table and configure Lambda to retrieve them as

  required" is incorrect. The environment variables are not encrypted throughout the entire process so there is a need

  to take action here. Storing the variables in an encrypted DynamoDB table is not necessary when you can use encryption

  helpers.

**References:**

<https://docs.aws.amazon.com/lambda/latest/dg/env_variables.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/>

----

- #aws_lambda_sdk #aws_lambda_cli #aws_lambda #<https://docs.aws.amazon.com/lambda/latest/dg/env_variables.html> #aws_lambda_console
