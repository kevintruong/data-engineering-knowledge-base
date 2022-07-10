#### Question  17

**A solutions architect is designing a microservices architecture. AWS Lambda will store data in an Amazon DynamoDB

table named Orders. The solutions architect needs to apply an IAM policy to the Lambda function’s execution role to

allow it to put, update, and delete items in the Orders table. No other actions should be allowed.**

**Which of the following code snippets should be included in the IAM policy to fulfill this requirement whilst providing

the LEAST privileged access?**

- [x] :  

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

- [ ] :

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

- [ ] :

```json5

{

  "Sid": "PutUpdateDeleteOnOrders",

  "Effect": "Allow",

  "Action": "dynamodb:* ",

  "Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/Orders"

}       

```

- [ ] :

```json5

{

  "Sid": "PutUpdateDeleteOnOrders",

  "Effect": "Deny",

  "Action": "dynamodb:* ",

  "Resource": "arn:aws:dynamodb:us-east-1:227392126428:table/Orders"

}

```

----

- #aws_lambda #amazon_dynamodb #iam_policy #aws #execution_role
- hasExplain:: [[explanation_Question  17.md]]
