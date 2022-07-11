**Explanation:**

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena

is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run. Amazon Athena

supports encrypted data for both the source data and query results, for example, using Amazon S3 with AWS KMS.

- ✅ :  "Use AWS KMS encryption keys for the S3 bucket and use Amazon Athena to query the data" is the correct answer.

- ❌ :  "Use Amazon S3 server-side encryption and use Amazon RedShift Spectrum to query the data" is incorrect.

  RedShift Spectrum is not serverless as it requires a RedShift cluster which is based on EC2 instances.

- ❌ :  "Use AWS KMS encryption keys for the S3 bucket and use Amazon Kinesis Data Analytics to query the data"

  is incorrect. Kinesis Data Analytics is used for analyzing real-time streaming data in Kinesis streams.

- ❌ :  "Use Amazon S3 server-side encryption and Amazon QuickSight to query the data" is incorrect. Amazon

  QuickSight is an interactive dashboard, it is not a service for running queries on data.

**References:**

<https://d1.awsstatic.com/whitepapers/architecture/wellarchitected-Machine-Learning-Lens.pdf>

<https://aws.amazon.com/athena/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/>

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/> #amazon_kinesis_data_analytics #amazon_redshift_spectrum #amazon_athena #aws_kms
