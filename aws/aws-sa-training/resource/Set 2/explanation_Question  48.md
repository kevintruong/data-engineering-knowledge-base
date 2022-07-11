**Explanation:**

Amazon S3 is great solution for storing objects such as this. You only pay for what you use and don’t need to worry

about scaling as it will scale as much as you need it to. Using Amazon Athena to analyze the data works well as it is a

serverless service so it will be very cost-effective for use cases where the analysis is only happening infrequently.

You can also configure Amazon S3 to expire the objects after 30 days.

- ✅ :  "Write the files to an S3 bucket and use Amazon Athena to query the data" is the correct answer.

- ❌ :  "Import the logs to an Amazon Redshift cluster" is incorrect. Importing the log files into an Amazon

  RedShift cluster will mean you can perform analytics on the data as this is the primary use case for RedShift (it’s a

  data warehouse). However, this is not the most cost-effective solution as RedShift uses EC2 instances (it’s not

  serverless) so the instances will be running all the time even though the analytics is infrequent.

- ❌ :  "Use AWS Data Pipeline to import the logs into a DynamoDB table" is incorrect. AWS Data Pipeline is used to

  process and move data. You can move data into DynamoDB, but this is not a good storage solution for these log files.

  Also, there is no analytics solution in this option.

- ❌ :  "Import the logs into an RDS MySQL instance" is incorrect. Importing the logs into an RDS MySQL instance is

  not a good solution. This is not the best storage solution for log files and its main use case as a DB is

  transactional rather than analytical.

**References:**

<https://aws.amazon.com/athena/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #amazon_redshift_cluster #aws_data_pipeline #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/> #dynamodb #amazon_athena
