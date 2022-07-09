#### Question  17


**A solutions architect is designing a microservices architecture. AWS Lambda will store data in an Amazon DynamoDB

table named Orders. The solutions architect needs to apply an IAM policy to the Lambda function’s execution role to

allow it to put, update, and delete items in the Orders table. No other actions should be allowed.**


**Which of the following code snippets should be included in the IAM policy to fulfill this requirement whilst providing

the LEAST privileged access?**


1:


```json5

{

  "Sid": "PutUpdateDeleteOnOrders",

  "Effect": "Allow",

  "Action": [

    "dynamodb:PutItem",

    "dynamodb:UpdateItem",

    "dynamodb:DeleteItem"

  ],

  "Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/Orders"

}

```


2:


```json5

{

  "Sid": "PutUpdateDeleteOnOrders",

  "Effect": "Allow",

  "Action": [

    "dynamodb:PutItem",

    "dynamodb:UpdateItem",

    "dynamodb:DeleteItem"

  ],

  "Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/*"

}       

```


3:


```json5

{

  "Sid": "PutUpdateDeleteOnOrders",

  "Effect": "Allow",

  "Action": "dynamodb:* ",

  "Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/Orders"

}       

```


4:


```json5

{

  "Sid": "PutUpdateDeleteOnOrders",

  "Effect": "Deny",

  "Action": "dynamodb:* ",

  "Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/Orders"

}

```


Answer: 1


**Explanation:**


The key requirements are to allow the Lambda function the put, update, and delete actions on a single table. Using the

principle of least privilege the answer should not allow any other access.


- CORRECT The following answer is correct:


"Sid": "PutUpdateDeleteOnOrders",


"Effect": "Allow",


"Action": [


"dynamodb:PutItem",


"dynamodb:UpdateItem",


"dynamodb:DeleteItem"


],


"Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/Orders"


This code snippet specifies the exact actions to allow and also specified the resource to apply those permissions to.


- INCORRECT the following answer is incorrect:


"Sid": "PutUpdateDeleteOnOrders",


"Effect": "Allow",


"Action": [


"dynamodb:PutItem",


"dynamodb:UpdateItem",


"dynamodb:DeleteItem"


],


"Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/*"


This code snippet specifies the correct list of actions but it provides a wildcard “*” instead of specifying the exact

resource. Therefore, the function will be able to put, update, and delete items on any table in the account.


- INCORRECT the following answer is incorrect:


"Sid": "PutUpdateDeleteOnOrders",


"Effect": "Allow",


"Action": "dynamodb:* ",


"Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/Orders"


This code snippet allows any action on DynamoDB by using a wildcard “dynamodb:*”. This does not follow the principle of

least privilege.


- INCORRECT the following answer is incorrect:


"Sid": "PutUpdateDeleteOnOrders",


"Effect": "Deny",


"Action": "dynamodb:* ",


"Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/Orders"


This code snippet denies any action on the table. This does not have the desired effect.


**References:**


https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-

compliance/aws-iam/

