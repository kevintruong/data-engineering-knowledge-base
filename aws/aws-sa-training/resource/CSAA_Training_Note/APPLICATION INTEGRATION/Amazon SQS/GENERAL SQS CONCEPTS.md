#### GENERAL SQS CONCEPTS


Amazon Simple Queue Service (Amazon SQS) is a web service that gives you access to message queues that store messages

waiting to be processed.


SQS offers a reliable, highly-scalable, hosted queue for storing messages in transit between computers.


SQS is used for distributed/decoupled applications.


SQS can be used with RedShift, DynamoDB, EC2, ECS, RDS, S3 and Lambda.


SQS uses a message-oriented API.


SQS uses pull based (polling) not push based.


Messages are 256KB in size.


Messages can be kept in the queue from 1 minute to 14 days (default is 4 days).


The visibility timeout is the amount of time a message is invisible in the queue after a reader picks up the message.


If a job is processed within the visibility timeout the message will be deleted.


If a job is not processed within the visibility timeout the message will become visible again (could be delivered twice)

.


The maximum visibility timeout for an Amazon SQS message is 12 hours.


An Amazon SQS message can contain up to 10 metadata attributes.


**The table below compares solution requirements that are more suitable for Amazon Kinesis Data Streams and Amazon

SQS:**

