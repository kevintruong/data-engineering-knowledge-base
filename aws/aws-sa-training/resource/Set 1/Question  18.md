#### Question  18


**A retail company with many stores and warehouses is implementing IoT sensors to gather monitoring data from devices in

each location. The data will be sent to AWS in real time. A solutions architect must provide a solution for ensuring

events are received in order for each device and ensure that data is saved for future processing.**


**Which solution would be MOST efficient?**


1: Use Amazon Kinesis Data Streams for real-time events with a partition key for each device. Use Amazon Kinesis Data

Firehose to save data to Amazon S3


2: Use Amazon Kinesis Data Streams for real-time events with a shard for each device. Use Amazon Kinesis Data Firehose

to save data to Amazon EBS


3: Use an Amazon SQS FIFO queue for real-time events with one queue for each device. Trigger an AWS Lambda function for

the SQS queue to save data to Amazon EFS


4: Use an Amazon SQS standard queue for real-time events with one queue for each device. Trigger an AWS Lambda function

from the SQS queue to save data to Amazon S3


Answer: 1


**Explanation:**


Amazon Kinesis Data Streams collect and process data in real time. A _Kinesis data stream_ is a set of shards. Each

shard has a sequence of data records. Each data record has a sequence number that is assigned by Kinesis Data Streams.

A _shard_ is a uniquely identified sequence of data records in a stream.


A _partition key_ is used to group data by shard within a stream. Kinesis Data Streams segregates the data records

belonging to a stream into multiple shards. It uses the partition key that is associated with each data record to

determine which shard a given data record belongs to.


For this scenario, the solutions architect can use a partition key for each device. This will ensure the records for

that device are grouped by shard and the shard will ensure ordering. Amazon S3 is a valid destination for saving the

data records.


- CORRECT "Use Amazon Kinesis Data Streams for real-time events with a partition key for each device. Use Amazon Kinesis

  Data Firehose to save data to Amazon S3" is the correct answer.


- INCORRECT "Use Amazon Kinesis Data Streams for real-time events with a shard for each device. Use Amazon Kinesis Data

  Firehose to save data to Amazon EBS" is incorrect as you cannot save data to EBS from Kinesis.


- INCORRECT "Use an Amazon SQS FIFO queue for real-time events with one queue for each device. Trigger an AWS Lambda

  function for the SQS queue to save data to Amazon EFS" is incorrect as SQS is not the most efficient service for

  streaming, real time data.


- INCORRECT "Use an Amazon SQS standard queue for real-time events with one queue for each device. Trigger an AWS Lambda

  function from the SQS queue to save data to Amazon S3" is incorrect as SQS is not the most efficient service for

  streaming, real time data.


**References:**


https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/

