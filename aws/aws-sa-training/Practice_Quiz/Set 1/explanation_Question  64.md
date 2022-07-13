**Explanation:**

This is a good use case for Amazon Kinesis streams as it is able to scale to the required load, allow multiple

applications to access the records and process them sequentially.

```

AWS Lambda

```

```

Users

Images Bucket

```

```

Resized Images

Bucket

```

```

Jpg image upload

```

```

Amazon CloudWatch

```

```

Event written to

CloudWatch Logs S 3 notifies Lambda

```

```

Region

```

```

Lambda runs your

code in response

to anevent

(trigger)

```

```

Resized image saved

in bucket

```

Amazon Kinesis Data Streams enables real-time processing of streaming big data. It provides ordering of records, as well

as the ability to read and/or replay records in the same order to multiple Amazon Kinesis Applications.

Amazon Kinesis streams allows up to 1 MiB of data per second or 1,000 records per second for writes per shard. There is

no limit on the number of shards so you can easily scale Kinesis Streams to accept 50,000 per second.

The Amazon Kinesis Client Library (KCL) delivers all records for a given partition key to the same record processor,

making it easier to build multiple applications reading from the same Amazon Kinesis data stream.

- ✅ :  "Amazon Kinesis Streams" is the correct answer.

- ❌ :  "Amazon SQS FIFO queue" is incorrect as SQS is not best suited to streaming data and Kinesis is a better

  solution.

- ❌ :  "AWS CloudTrail trail" is incorrect. CloudTrail is used for auditing and is not useful here.

- ❌ :  "Amazon SQS standard queue" is incorrect. Standard SQS queues do not ensure that messages are processed

  sequentially and FIFO SQS queues do not scale to the required number of transactions a second.

**References:**

<https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html>

<https://aws.amazon.com/kinesis/data-streams/faqs/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/>

----

- #amazon_kinesis_data_streams #same_amazon_kinesis_data_stream #<https://aws.amazon.com/kinesis/data-streams/faqs/> #amazon_kinesis_streams #aws_lambda
