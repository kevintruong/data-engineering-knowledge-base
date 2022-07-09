#### Question  17


**An application analyzes images of people that are uploaded to an Amazon S3 bucket. The application determines

demographic data which is then saved to a .CSV file in another S3 bucket. The data must be encrypted at rest and then

queried using SQL. The solution should be fully serverless.**


**Which actions should a Solutions Architect take to encrypt and query the data?**


1: Use Amazon S3 server-side encryption and use Amazon RedShift Spectrum to query the data


2: Use AWS KMS encryption keys for the S3 bucket and use Amazon Athena to query the data


3: Use AWS KMS encryption keys for the S3 bucket and use Amazon Kinesis Data Analytics to query the data


4: Use Amazon S3 server-side encryption and Amazon QuickSight to query the data


Answer: 2


**Explanation:**


Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena

is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run. Amazon Athena

supports encrypted data for both the source data and query results, for example, using Amazon S3 with AWS KMS.


- CORRECT "Use AWS KMS encryption keys for the S3 bucket and use Amazon Athena to query the data" is the correct answer.


- INCORRECT "Use Amazon S3 server-side encryption and use Amazon RedShift Spectrum to query the data" is incorrect.

  RedShift Spectrum is not serverless as it requires a RedShift cluster which is based on EC2 instances.


- INCORRECT "Use AWS KMS encryption keys for the S3 bucket and use Amazon Kinesis Data Analytics to query the data"

  is incorrect. Kinesis Data Analytics is used for analyzing real-time streaming data in Kinesis streams.


- INCORRECT "Use Amazon S3 server-side encryption and Amazon QuickSight to query the data" is incorrect. Amazon

  QuickSight is an interactive dashboard, it is not a service for running queries on data.


**References:**


https://d1.awsstatic.com/whitepapers/architecture/wellarchitected-Machine-Learning-Lens.pdf


https://aws.amazon.com/athena/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/

