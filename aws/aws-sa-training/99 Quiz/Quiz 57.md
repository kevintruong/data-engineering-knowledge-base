## Quiz 57: You are a Solutions Architect at a media company and you need to build an application stack that can receive customer comments from sporting events. The application is expected to receive significant load that could scale to millions of messages within a short space of time following high-profile matches. As you are unsure of the load required for the database layer what is the most cost-effective way to ensure that the messages are not dropped?**

- [ ] Use DynamoDB and provision enough write capacity to handle the highest expected load
- [ ] Write the data to an S3 bucket, configure RDS to poll the bucket for new messages
- [ ] Create an SQS queue and modify the application to write to the SQS queue. Launch another application instance the polls the queue and writes messages to the database
- [ ] Use RDS Auto Scaling for the database layer which will automatically scale as required

----
Answer: 3
**Explanation:**
Amazon Simple Queue Service (Amazon SQS) is a web service that gives you access to message queues that store messages waiting to be processed. SQS offers a reliable, highly-scalable, hosted queue for storing messages in transit between computers and is used for distributed/decoupled applications. The following diagram depicts a decoupled application using an Amazon SQS queue:
![](aws-solution-architecture-practice-quiz-1641093613949.png)
This is a great use case for SQS as the messages you don’t have to over-provision the database layer or worry about messages being dropped.

- ✅: "Create an SQS queue and modify the application to write to the SQS queue. Launch another application instance the polls the queue and writes messages to the database" is the correct answer.
- ❌: "Use DynamoDB and provision enough write capacity to handle the highest expected load" is incorrect. With DynamoDB there are 2 pricing options:
- Provisioned capacity has been around forever and is one of the incorrect answers to this question. With provisioned capacity you have to specify the number of read/write capacity units to provision and pay for these regardless of the load on the database.

- With the On-demand capacity mode DynamoDB is charged based on the data reads and writes your application performs on your tables. You do not need to specify how much read and write throughput you expect your application to perform because DynamoDB instantly accommodates your workloads as they ramp up or down. it might be a good solution to this question but is not an available option.
- ❌: "Write the data to an S3 bucket, configure RDS to poll the bucket for new messages" is incorrect.
- ❌: "Use RDS Auto Scaling for the database layer which will automatically scale as required" is incorrect. RDS Auto Scaling does not exist. With RDS you have to select the underlying EC2 instance type to use and pay for that regardless of the actual load on the DB. Note that a new feature released in June 2019 does allow Auto Scaling for the RDS storage, but not the compute layer.
  **References:**
  https://aws.amazon.com/sqs/faqs/
