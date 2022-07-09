#### Question  56


**An organization has a data lake on Amazon S3 and needs to find a solution for performing in-place queries of the data

assets in the data lake. The requirement is to perform both data discovery and SQL querying, and complex queries from a

large number of concurrent users using BI tools.**


**What is the BEST combination of AWS services to use in this situation? (Select TWO)**


1: RedShift Spectrum for the complex queries


2: Amazon Athena for the ad hoc SQL querying


3: AWS Glue for the ad hoc SQL querying


4: AWS Lambda for the complex queries


5: Amazon Kinesis for the complex queries


**Answer: 1,2**


**Explanation:**


Performing in-place queries on a data lake allows you to run sophisticated analytics queries directly on the data in S3

without having to load it into a data warehouse.


You can use both Athena and Redshift Spectrum against the same data assets. You would typically use Athena for ad hoc

data discovery and SQL querying, and then use Redshift Spectrum for more complex queries and scenarios where a large

number of data lake users want to run concurrent BI and reporting workloads.


- CORRECT "RedShift Spectrum for the complex queries" is a correct answer.


- CORRECT "Amazon Athena for the ad hoc SQL querying" is also a correct answer.


- INCORRECT "AWS Glue for the ad hoc SQL querying" is incorrect. AWS Glue is an extract, transform and load

  (ETL) service.


- INCORRECT "AWS Lambda for the complex queries" is incorrect. AWS Lambda is a serverless technology for running

  functions, it is not the best solution for running analytics queries.


- INCORRECT "Amazon Kinesis for the complex queries" is incorrect. Amazon Kinesis is used for ingesting and processing

  real time streaming data, not performing queries.


**References:**


https://docs.aws.amazon.com/aws-technical-content/latest/building-data-lakes/in-place-querying.html


https://aws.amazon.com/redshift/


https://aws.amazon.com/athena/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

redshift/

