### Analytics Quiz Questions

Answers and explanations are provided below after the last question in this section.

**Question 1:**

A user is testing a new service that receives location updates from 5,000 rental cars every hour.  Which service will collect data and automatically scale to accommodate production workload?

```
A. Amazon EC2
B. Amazon Kinesis Firehose
C. Amazon EBS
D. Amazon API Gateway
```
**Question 2:**

Which AWS service can be used to prepare and load data for analytics using an extract, transform and load (ETL) process?

```
A. AWS Lambda
B. Amazon Athena
C. AWS Glue
D. Amazon EMR
```
**Question 3:**

A Solutions Architect is designing a solution for a financial application that will receive trading data in large volumes. What is the best solution for ingesting and processing a very large number of data streams in near real time?

```
A. Amazon EMR
B. Amazon Kinesis Firehose
C. Amazon Redshift
D. Amazon Kinesis Data Streams
```
**Question 4:**

You have recently enabled Access Logs on your Application Load Balancer (ALB). One of your colleagues would like to process the log files using a hosted Hadoop service. What configuration changes and services can be leveraged to deliver this requirement?

```
A. Configure Access Logs to be delivered to DynamoDB and use EMR for processing the log files
B. Configure Access Logs to be delivered to S3 and use Kinesis for processing the log files
C. Configure Access Logs to be delivered to S3 and use EMR for processing the log files
D. Configure Access Logs to be delivered to EC2 and install Hadoop for processing the log files
```

**Question 5:**

A Solutions Architect is designing the messaging and streaming layers of a serverless application.  The messaging layer will manage communications between components and the streaming layer will manage real-time analysis and processing of streaming data.

The Architect needs to select the most appropriate AWS services for these functions. Which services should be used for the messaging and streaming layers? (choose 2)

```
A. Use Amazon Kinesis for collecting, processing and analyzing real-time streaming data
B. Use Amazon EMR for collecting, processing and analyzing real-time streaming data
C. Use Amazon SNS for providing a fully managed messaging service
D. Use Amazon SWF for providing a fully managed messaging service
E. Use Amazon CloudTrail for collecting, processing and analyzing real-time streaming data
```

**ANALYTICS - ANSWERS**

**Question 1 answer: B**

Explanation:

```
What we need here is a service that can streaming collect streaming data. The only option available is Kinesis Firehose which captures, transforms, and loads streaming data into “destinations” such as S3, RedShift, Elasticsearch and Splunk.  Amazon EC2 is not suitable for collecting streaming data.

EBS is a block-storage service in which you attach volumes to EC2 instances, this does not assist with collecting streaming data (see previous point).
Amazon API Gateway is used for hosting and managing APIs not for receiving streaming data.
```

**Question 2 answer: C**

Explanation:

```
AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for
customers to prepare and load their data for analytics.
Amazon Elastic Map Reduce (EMR) provides a managed Hadoop framework that makes it easy,
fast, and cost-effective to process vast amounts of data across dynamically scalable Amazon EC2
instances.
Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3
using standard SQL.
AWS Lambda is a serverless application that runs code as functions in response to events.
```
**Question 3 answer: D**

Explanation:

```
Kinesis Data Streams enables you to build custom applications that process or analyze streaming
data for specialized needs. It enables real-time processing of streaming big data and can be used
for rapidly moving data off data producers and then continuously processing the data. Kinesis
Data Streams stores data for later processing by applications (key difference with Firehose which
delivers data directly to AWS services).
Kinesis Firehose can allow transformation of data and it then delivers data to supported services.
RedShift is a data warehouse solution used for analyzing data.
EMR is a hosted Hadoop framework that is used for analytics.
```
**Question 4 answer: C**

Explanation:

```
Access Logs can be enabled on ALB and configured to store data in an S3 bucket. Amazon EMR is
a web service that enables businesses, researchers, data analysts, and developers to easily and
cost-effectively process vast amounts of data. EMR utilizes a hosted Hadoop framework running
on Amazon EC2 and Amazon S3.
```

```
Neither Kinesis nor EC2 provide a hosted Hadoop service.
You cannot configure access logs to be delivered to DynamoDB.
```
**Question 5 answer: A,C**

Explanation:

```
Amazon Kinesis makes it easy to collect, process, and analyze real-time streaming data. With Amazon Kinesis Analytics, you can run standard SQL or build entire streaming applications using SQL.
Amazon Simple Notification Service (Amazon SNS) provides a fully managed messaging service for pub/sub patterns using asynchronous event notifications and mobile push notifications for microservices, distributed systems, and serverless applications.
Amazon Elastic Map Reduce runs on EC2 instances so is not serverless.
Amazon Simple Workflow Service is used for executing tasks not sending messages.
Amazon CloudTrail is used for recording API activity on your account.
```