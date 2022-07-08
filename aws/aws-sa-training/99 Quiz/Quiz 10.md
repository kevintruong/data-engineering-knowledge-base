## Quiz 10: A solutions architect is designing a new service that will use an Amazon API Gateway API on the frontend. The service will need to persist data in a backend database using key-value requests. Initially, the data requirements will be around 1 GB and future growth is unknown. Requests can range from 0 to over 800 requests per second.**

**Which combination of AWS services would meet these requirements? (Select TWO)**

- [ ] AWS Fargate
- [ ] AWS Lambda
- [ ] Amazon DynamoDB
- [ ] Amazon EC2 Auto Scaling
- [ ] Amazon RDS

----
Answer: 2, 3

**Explanation:**
In this case AWS Lambda can perform the computation and store the data in an Amazon DynamoDB table. 
- Lambda can scale concurrent executions to meet demand easily 
- and DynamoDB is built for key-value data storage requirements and is also serverless and easily scalable.
This is therefore a cost effective solution for unpredictable workloads.

- ✅: "AWS Lambda" is a correct answer.
- ✅: "Amazon DynamoDB" is also a correct answer.
- ❌: "AWS Fargate" is incorrect as containers run constantly and therefore incur costs even when no requests are being made.
- ❌: "Amazon EC2 Auto Scaling" is incorrect as this uses EC2 instances which will incur costs even when no requests are being made.
- ❌: "Amazon RDS" is incorrect as this is a relational database not a No-SQL database. It is therefore not suitable for key-value data storage requirements.
  **References:**
  https://aws.amazon.com/lambda/features/
  https://aws.amazon.com/dynamodb/



----
#quiz 
- relateTo:: [[Domain 2 Design High-Performing Architectures]]
