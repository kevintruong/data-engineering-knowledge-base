*

**Explanation:**

You can create a CloudWatch alarm that watches a single CloudWatch metric or the result of a math expression based on

CloudWatch metrics. The alarm performs one or more actions based on the value of the metric or expression relative to a

threshold over a number of time periods.

The action can be an Amazon EC2 action, an Amazon EC2 Auto Scaling action, or a notification sent to an Amazon SNS

topic. SNS can be configured to send an email notification

* ✅ :  "Create a CloudWatch alarm and associate an SNS topic with it that sends an email notification" is the correct

  answer.

* ❌ :  "Create a CloudWatch alarm and associate an SQS queue with it that delivers a message to SES" is incorrect.

  You cannot associate an SQS queue with a CloudWatch alarm.

* ❌ :  "Setup an RDS alarm and associate an SNS topic with it that sends an email" is incorrect. CloudWatch

  performs performance monitoring so you don’t setup alarms in RDS itself.

* ❌ :  "Create a CloudTrail alarm and configure a notification event to send an SMS" is incorrect. CloudTrail is

  used for auditing API access, not for performance monitoring.

**References:**

<https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management>-

tools/amazon-cloudwatch/

----
* #cloudwatch_alarm #cloudwatch_metrics #single_cloudwatch_metric #cloudtrail_alarm #cloudwatch
