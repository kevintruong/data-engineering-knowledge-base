#### Question  27


**A company is investigating ways to analyze and process large amounts of data in the cloud faster, without needing to

load or transform the data in a data warehouse. The data resides in Amazon S3.**


**Which AWS services would allow the company to query the data in place? (Select TWO)**


1: Amazon S3 Select


2: Amazon Kinesis Data Streams


3: Amazon Elasticsearch


4: Amazon RedShift Spectrum


5: Amazon SWF


**Answer: 1,4**


**Explanation:**


Amazon S3 Select is designed to help analyze and process data within an object in Amazon S3 buckets, faster and cheaper.

It works by providing the ability to retrieve a subset of data from an object in Amazon S3 using simple SQL expressions


Amazon Redshift Spectrum allows you to directly run SQL queries against exabytes of unstructured data in Amazon S3. No

loading or transformation is required.


- CORRECT "Amazon S3 Select" is a correct answer.


- CORRECT "Amazon RedShift Spectrum" is also a correct answer.


- INCORRECT "Amazon Kinesis Data Streams" is incorrect. Amazon Kinesis Data Streams (KDS) is a massively scalable and

  durable real-time data streaming service. It does not allow you to perform query-in-place operations on S3.


- INCORRECT "Amazon Elasticsearch" is incorrect. Amazon Elasticsearch Service, is a fully managed service that makes it

  easy for you to deploy, secure, operate, and scale Elasticsearch to search, analyze, and visualize data in real-time.


- INCORRECT "Amazon SWF" is incorrect. Amazon SWF helps developers build, run, and scale background jobs that have

  parallel or sequential steps.


**References:**


https://aws.amazon.com/blogs/aws/s3-glacier-select/


https://aws.amazon.com/about-aws/whats-new/2017/11/amazon-redshift-spectrum-is-now-available-in-four-

additional-aws-regions-and-enhances-query-performance-in-all-available-aws-regions/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

redshift/

