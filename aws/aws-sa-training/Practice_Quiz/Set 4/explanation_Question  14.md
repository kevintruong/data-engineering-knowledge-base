**Explanation:**

You can use a Lambda function to process Amazon Simple Notification Service notifications. Amazon SNS supports Lambda

functions as a target for messages sent to a topic. This solution decouples the Amazon EC2 application from Lambda and

ensures the Lambda function is invoked.

- ✅ :  "Amazon SNS" is the correct answer.

- ❌ :  "Amazon SQS" is incorrect. You cannot invoke a Lambda function using Amazon SQS. Lambda can be configured to

  poll a queue, as SQS is pull-based, but it is not push-based like SNS which is what this solution requires.

- ❌ :  "Amazon Kinesis" is incorrect as this service is used for ingesting and processing real time streaming data,

  it is not a suitable service to be used solely for invoking a Lambda function.

- ❌ :  "Amazon OpsWorks" is incorrect as this service is used for configuration management of systems using Chef or

  Puppet.

**References:**

<https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>-

integration/amazon-sns/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/>

----

- #amazon_simple_notification_service_notifications #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/> #amazon_sns #amazon_kinesis #amazon_ec2_application
