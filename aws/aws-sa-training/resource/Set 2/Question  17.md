#### Question  17

**A company has refactored a legacy application to run as two microservices using Amazon ECS. The application processes

data in two parts and the second part of the process takes longer than the first.**

**How can a solutions architect integrate the microservices and allow them to scale independently?**

- [ ] Implement code in microservice 1 to send data to an Amazon S3 bucket. Use S3 event notifications to invoke

microservice 2

- [ ] Implement code in microservice 1 to publish data to an Amazon SNS topic. Implement code in microservice 2 to

subscribe to this topic

- [ ] Implement code in microservice 1 to send data to Amazon Kinesis Data Firehose. Implement code in microservice 2 to

read from Kinesis Data Firehose

- [x] Implement code in microservice 1 to send data to an Amazon SQS queue. Implement code in microservice 2 to process

messages from the queue

- hasExplain:: [[explanation_Question  17.md]]

# microservices #microservice #amazon_sqs_queue #amazon_kinesis_data_firehose #amazon_sns_topic
