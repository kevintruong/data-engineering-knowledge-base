#### Question  17


**A company has refactored a legacy application to run as two microservices using Amazon ECS. The application processes

data in two parts and the second part of the process takes longer than the first.**


**How can a solutions architect integrate the microservices and allow them to scale independently?**


1: Implement code in microservice 1 to send data to an Amazon S3 bucket. Use S3 event notifications to invoke

microservice 2


2: Implement code in microservice 1 to publish data to an Amazon SNS topic. Implement code in microservice 2 to

subscribe to this topic


3: Implement code in microservice 1 to send data to Amazon Kinesis Data Firehose. Implement code in microservice 2 to

read from Kinesis Data Firehose


4: Implement code in microservice 1 to send data to an Amazon SQS queue. Implement code in microservice 2 to process

messages from the queue


Answer: 4


**Explanation:**


This is a good use case for Amazon SQS. The microservices must be decoupled so they can scale independently. An Amazon

SQS queue will enable microservice 1 to add messages to the queue. Microservice 2 can then pick up the messages and

process them. This ensures that if there’s a spike in traffic on the frontend, messages do not get lost due to the

backend process not being ready to process them.


- CORRECT "Implement code in microservice 1 to send data to an Amazon SQS queue. Implement code in microservice 2 to

  process messages from the queue" is the correct answer.


- INCORRECT "Implement code in microservice 1 to send data to an Amazon S3 bucket. Use S3 event notifications to invoke

  microservice 2" is incorrect as a message queue would be preferable to an S3 bucket.


- INCORRECT "Implement code in microservice 1 to publish data to an Amazon SNS topic. Implement code in microservice 2

  to subscribe to this topic" is incorrect as notifications to topics are pushed to subscribers. In this case we want

  the second microservice to pickup the messages when ready (pull them).


- INCORRECT "Implement code in microservice 1 to send data to Amazon Kinesis Data Firehose. Implement code in

  microservice 2 to read from Kinesis Data Firehose" is incorrect as this is not how Firehose works. Firehose sends data

  directly to destinations, it is not a message queue.


**References:**


https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

