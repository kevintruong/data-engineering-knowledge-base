#### KINESIS DATA STREAMS


Kinesis Data Streams enables you to build custom applications that process or analyze streaming data for specialized

needs.


Kinesis Data Streams enables real-time processing of streaming big data.


Kinesis Data Streams is useful for rapidly moving data off data producers and then continuously processing the data.


Kinesis Data Streams **stores data** for later processing by applications (key difference with Firehose which delivers

data directly to AWS services).


**Common use cases include:**


- Accelerated log and data feed intake.

- Real-time metrics and reporting.

- Real-time data analytics.

- Complex stream processing.


**The following diagram illustrates the high-level architecture of Kinesis Data Streams.**


- Producers continually push data to Kinesis Data Streams.

- Consumers process the data in real time.

- Consumers can store their results using an AWS service such as Amazon DynamoDB, Amazon Redshift, or Amazon S3.

- Kinesis Streams applications are consumers that run on EC2 instances.

- Shards are uniquely identified groups or data records in a stream.

- Records are the data units stored in a Kinesis Stream.


A producer creates the data that makes up the stream.


**Producers can be used through the following:**


- Kinesis Streams API.

- Kinesis Producer Library (KPL).

- Kinesis Agent.


A record is the unit of data stored in a Amazon Kinesis data stream.


A record is composed of a sequence number, partition key, and data blob.


By default, records of a stream are accessible for up to 24 hours from the time they are added to the stream (can be

raised to 7 days by enabling extended data retention).


A data blob is the data of interest your data producer adds to a data stream.


The maximum size of a data blob (the data payload before Base64-encoding) within one record is 1 megabyte (MB).


A shard is the base throughput unit of an Amazon Kinesis data stream.


One shard provides a capacity of 1MB/sec data input and 2MB/sec data output.


Each shard can support up to 1000 PUT records per second.


A stream is composed of one or more shards.


Consumers are the EC2 instances that analyze the data received from a stream.


Consumers are known as Amazon Kinesis Streams Applications.


When the data rate increases, add more shards to increase the size of the stream.


Remove shards when the data rate decreases.


Partition keys are used to group data by shard within a stream.


Kinesis Streams uses KMS master keys for encryption.


To read from or write to an encrypted stream the producer and consumer applications must have permission to access the

master key.


Kinesis Data Streams replicates synchronously across three AZs.

