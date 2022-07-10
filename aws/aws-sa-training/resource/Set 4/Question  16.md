#### Question  16


**Every time an item in an Amazon DynamoDB table is modified a record must be retained for compliance reasons. What is

the most efficient solution to recording this information?**


- [ ] Enable Amazon CloudWatch Logs. Configure an AWS Lambda function to monitor the log files and record deleted item data

to an Amazon S3 bucket


- [x] Enable DynamoDB Streams. Configure an AWS Lambda function to poll the stream and record the modified item data to an

Amazon S3 bucket


- [ ] Enable Amazon CloudTrail. Configure an Amazon EC2 instance to monitor activity in the CloudTrail log files and record

changed items in another DynamoDB table


- [ ] Enable DynamoDB Global Tables. Enable DynamoDB streams on the multi-region table and save the output directly to an

Amazon S3 bucket



- hasExplain:: [[explanation_Question  16.md]]

#dynamodb #aws #cloudwatch #cloudtrail #logs 