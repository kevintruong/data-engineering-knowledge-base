**Explanation:**

DAX is a DynamoDB-compatible caching service that enables you to benefit from fast in-memory performance for demanding

applications. DAX addresses three core scenarios:

- As an in-memory cache, DAX reduces the response times of eventually consistent read workloads by an order of magnitude

  from single-digit milliseconds to microseconds.

- DAX reduces operational and application complexity by providing a managed service that is API- compatible with

  DynamoDB. Therefore, it requires only minimal functional changes to use with an existing application.

- For read-heavy or bursty workloads, DAX provides increased throughput and potential operational cost savings by

  reducing the need to overprovision read capacity units. This is especially beneficial for applications that require

  repeated reads for individual keys.

DynamoDB accelerator is the best solution for caching the reads and delivering them at extremely low latency.

- ✅ :  "Use Amazon DynamoDB Accelerator to cache the reads" is the correct answer.

- ❌ :  "Increase the number of Amazon DynamoDB write capacity units" is incorrect. This will not improve read

  performance as write capacity units affect write performance.

- ❌ :  "Add an Amazon SQS queue to decouple the requests" is incorrect. You cannot decouple a database from the

  frontend with a queue in order to decrease read latency.

- ❌ :  "Use an Amazon Kinesis Data Stream to decouple requests" is incorrect. You cannot increase read performance

  for a database by implementing a real-time streaming service.

**References:**

<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- dynamodb/

----

- #amazon_dynamodb_accelerator #<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax.html_>> #amazon_dynamodb #dynamodb #dax
