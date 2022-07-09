#### Question  45


**Your Business Intelligence team use SQL tools to analyze data. What would be the best solution for performing queries

on structured data that is being received at a high velocity?**


1: EMR using Hive


2: Kinesis Firehose with RDS


3: EMR running Apache Spark


4: Kinesis Firehose with RedShift


Answer: 4


**Explanation:**


Kinesis Data Firehose is the easiest way to load streaming data into data stores and analytics tools. Firehose

Destinations include: Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk.


Amazon Redshift is a fast, fully managed data warehouse that makes it simple and cost-effective to analyze all your data

using standard SQL and existing Business Intelligence (BI) tools.


RDS is a transactional database and is not a supported Kinesis Firehose destination.


- CORRECT "Kinesis Firehose with RedShift" is the correct answer.


- INCORRECT "EMR using Hive" is incorrect. EMR is a hosted Hadoop framework and doesn’t natively support SQL.


- INCORRECT "Kinesis Firehose with RDS" is incorrect as RedShift is a better solution for an analytics use case.


- INCORRECT "EMR running Apache Spark" is incorrect. EMR is a hosted Hadoop framework and doesn’t natively support SQL.


**References:**


https://aws.amazon.com/kinesis/data-firehose/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/

