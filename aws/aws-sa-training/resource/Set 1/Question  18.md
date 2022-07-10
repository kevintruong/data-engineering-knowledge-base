#### Question  18


**A retail company with many stores and warehouses is implementing IoT sensors to gather monitoring data from devices in

each location. The data will be sent to AWS in real time. A solutions architect must provide a solution for ensuring

events are received in order for each device and ensure that data is saved for future processing.**


**Which solution would be MOST efficient?**


- [x] Use Amazon Kinesis Data Streams for real-time events with a partition key for each device. Use Amazon Kinesis Data

Firehose to save data to Amazon S3


- [ ] Use Amazon Kinesis Data Streams for real-time events with a shard for each device. Use Amazon Kinesis Data Firehose

to save data to Amazon EBS


- [ ] Use an Amazon SQS FIFO queue for real-time events with one queue for each device. Trigger an AWS Lambda function for

the SQS queue to save data to Amazon EFS


- [ ] Use an Amazon SQS standard queue for real-time events with one queue for each device. Trigger an AWS Lambda function

from the SQS queue to save data to Amazon S3



- hasExplain:: [[explanation_Question  18.md]]

#amazon_kinesis_data_streams #amazon_kinesis_data #amazon_kinesis_data_firehose #amazon_s3 #amazon_sqs_fifo_queue 