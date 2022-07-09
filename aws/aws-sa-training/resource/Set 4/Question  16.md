#### Question  16


**Every time an item in an Amazon DynamoDB table is modified a record must be retained for compliance reasons. What is

the most efficient solution to recording this information?**


1: Enable Amazon CloudWatch Logs. Configure an AWS Lambda function to monitor the log files and record deleted item data

to an Amazon S3 bucket


2: Enable DynamoDB Streams. Configure an AWS Lambda function to poll the stream and record the modified item data to an

Amazon S3 bucket


3: Enable Amazon CloudTrail. Configure an Amazon EC2 instance to monitor activity in the CloudTrail log files and record

changed items in another DynamoDB table


4: Enable DynamoDB Global Tables. Enable DynamoDB streams on the multi-region table and save the output directly to an

Amazon S3 bucket


Answer: 2


**Explanation:**


Amazon DynamoDB Streams captures a time-ordered sequence of item-level modifications in any DynamoDB table and stores

this information in a log for up to 24 hours. Applications can access this log and view the data items as they appeared

before and after they were modified, in near-real time.


For example, in the diagram below a DynamoDB stream is being consumed by a Lambda function which processes the item data

and records a record in CloudWatch Logs


- CORRECT "Enable DynamoDB Streams. Configure an AWS Lambda function to poll the stream and record the modified item

  data to an Amazon S3 bucket" is the correct answer.


- INCORRECT "Enable Amazon CloudWatch Logs. Configure an AWS Lambda function to monitor the log files and record deleted

  item data to an Amazon S3 bucket" is incorrect. The deleted item data will not be recorded in CloudWatch Logs.


- INCORRECT "Enable Amazon CloudTrail. Configure an Amazon EC2 instance to monitor activity in the CloudTrail log files

  and record changed items in another DynamoDB table" is incorrect. CloudTrail records API actions so it will not record

  the data from the item that was modified.


- INCORRECT "Enable DynamoDB Global Tables. Enable DynamoDB streams on the multi-region table and save the output

  directly to an Amazon S3 bucket" is incorrect. Global Tables is used for creating a multi-region, multi-master

  database. It is of no additional value for this requirement as you could just enable DynamoDB streams on the main

  table. You also cannot save modified data straight to an S3 bucket.


**References:**


https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/


1. Application inserts / updates /deletes item


2. A record is written to the DynamoDB stream


3. A Lambda function is triggered


4. The Lambda function writes to CloudWatch Logs


```

Application DynamoDB Table DynamoDB Streams

```


```

1 2

```


```

AWS Lambda Amazon CloudWatch

```


```

3

```


```

4

```

