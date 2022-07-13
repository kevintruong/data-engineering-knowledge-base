**Explanation:**

DynamoDB Streams help you to keep a list of item level changes or provide a list of item level changes that have taken

place in the last 24hrs. Amazon DynamoDB is integrated with AWS Lambda so that you can create triggers—pieces of code

that automatically respond to events in DynamoDB Streams.

If you enable DynamoDB Streams on a table, you can associate the stream ARN with a Lambda function that you write.

Immediately after an item in the table is modified, a new record appears in the table’s stream. AWS Lambda polls the

stream and invokes your Lambda function synchronously when it detects new stream records.

An event source mapping identifies a poll-based event source for a Lambda function. It can be either an Amazon Kinesis

or DynamoDB stream. Event sources maintain the mapping configuration except for stream- based services (e.g. DynamoDB,

Kinesis) for which the configuration is made on the Lambda side and Lambda performs the polling.

- ✅ :  "Enable DynamoDB Streams and create an event source mapping between AWS Lambda and the relevant stream" is the

  correct answer.

- ❌ :  "Enable server access logging and create an event source mapping between AWS Lambda and the S3 bucket to

  which the logs are written" is incorrect. The questions asks for a solution that runs code in response to changes in a

  DynamoDB table, not an S3 bucket.

- ❌ :  "Create a local secondary index that records item level changes and write some custom code that responds to

  updates to the index" is incorrect. A local secondary index maintains an alternate sort key for a given partition key

  value, it does not record item level changes.

- ❌ :  "Use Kinesis Data Streams and configure DynamoDB as a producer" is incorrect. You cannot configure DynamoDB

  as a Kinesis Data Streams producer.

**References:**

<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- dynamodb/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/>

----

- #dynamodb_streams #dynamodb_stream #enable_dynamodb_streams #dynamodb #amazon_dynamodb
