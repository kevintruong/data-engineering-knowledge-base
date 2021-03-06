**Explanation:**

The Amazon S3 notification feature enables you to receive notifications when certain events happen in your bucket. To

enable notifications, you must first add a notification configuration that identifies the events you want Amazon S3 to

publish and the destinations where you want Amazon S3 to send the notifications. You store this configuration in the _

notification_ subresource that is associated with a bucket.

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and

load their data for analytics.

With this solution S3 event notifications triggering a Lambda function is completely serverless and cost- effective and

AWS Glue can trigger ETL jobs that will transform that data and load it into a data store such as S3.

- ✅ :  "Configure S3 event notifications to trigger a Lambda function when data is uploaded and use the Lambda

  function to trigger the ETL job" is a correct answer.

- ✅ :  "Use AWS Glue to extract, transform and load the data into the target data store" is also a correct answer.

- ❌ :  "Configure a CloudWatch alarm to send a notification to CloudFormation when data is uploaded"

  is incorrect. Using event notifications is the best solution.

- ❌ :  "Configure CloudFormation to provision a Kinesis data stream to transform the data and load it into S3"

  is incorrect. Kinesis Data Streams is used for processing data, rather than extracting and transforming it. The

  Kinesis consumers are EC2 instances which are not as cost-effective as serverless solutions.

- ❌ :  "Configure CloudFormation to provision AWS Data Pipeline to transform the data" is incorrect. AWS Data

  Pipeline can be used to automate the movement and transformation of data, it relies on other services to actually

  transform the data.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>

<https://aws.amazon.com/glue/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #amazon_s3_notification_feature #configure_s3_event_notifications #aws_data_pipeline #solution_s3_event_notifications #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>
