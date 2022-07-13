#### KINESIS DATA FIREHOSE


Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools.


Captures, transforms, and loads streaming data.


Enables near real-time analytics with existing business intelligence tools and dashboards.


Kinesis Data Streams can be used as the source(s) to Kinesis Data Firehose.


You can configure Kinesis Data Firehose to transform your data before delivering it.


With Kinesis Data Firehose you don’t need to write an application or manage resources.


Firehose can batch, compress, and encrypt data before loading it.


Firehose synchronously replicates data across three AZs as it is transported to destinations.


Each delivery stream stores data records for up to 24 hours.


A source is where your streaming data is continuously generated and captured.


A delivery stream is the underlying entity of Amazon Kinesis Data Firehose.


A record is the data of interest your data producer sends to a delivery stream.


The maximum size of a record (before Base64-encoding) is 1000 KB.


A destination is the data store where your data will be delivered.


**Firehose Destinations include:**


- Amazon S3

- Amazon Redshift

- Amazon Elasticsearch Service

- Splunk


Producers provide data streams.


No shards, totally automated.


Can encrypt data with an existing AWS Key Management Service (KMS) key.


Server-side-encryption can be used if Kinesis Streams is used as the data source.


Firehose can invoke an AWS Lambda function to transform incoming data before delivering it to a destination.


For Amazon S3 destinations, streaming data is delivered to your S3 bucket. If data transformation is enabled, you can

optionally back up source data to another Amazon S3 bucket:


For Amazon Redshift destinations, streaming data is delivered to your S3 bucket first. Kinesis Data Firehose then issues

an Amazon Redshift **COPY** command to load data from your S3 bucket to your Amazon Redshift cluster. If data

transformation is enabled, you can optionally back up source data to another Amazon S3 bucket:


For Amazon Elaticsearch destinations, streaming data is delivered to your Amazon ES cluster, and it can optionally be

backed up to your S3 bucket concurrently:


For Splunk destinations, streaming data is delivered to Splunk, and it can optionally be backed up to your S3 bucket

concurrently:

