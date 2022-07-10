#### Question  57


**You are a Solutions Architect at a media company and you need to build an application stack that can receive customer

comments from sporting events. The application is expected to receive significant load that could scale to millions of

messages within a short space of time following high-profile matches. As you are unsure of the load required for the

database layer what is the most cost-effective way to ensure that the messages are not dropped?**


- [ ] Use DynamoDB and provision enough write capacity to handle the highest expected load


- [ ] Write the data to an S3 bucket, configure RDS to poll the bucket for new messages


- [x] Create an SQS queue and modify the application to write to the SQS queue. Launch another application instance the

polls the queue and writes messages to the database


- [ ] Use RDS Auto Scaling for the database layer which will automatically scale as required



- hasExplain:: [[explanation_Question  57.md]]

#dynamodb #rds_auto_scaling #s3_bucket #sqs_queue #queue 