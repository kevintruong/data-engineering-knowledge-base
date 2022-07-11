**Explanation:**

There is no standard metric in CloudWatch for collecting EC2 memory usage. However, you can use the CloudWatch agent to

collect both system metrics and log files from Amazon EC2 instances and on-premises servers. The metrics can be pushed

to a CloudWatch custom metric.

- ✅ :  "Install the CloudWatch agent on the EC2 instance to push memory usage to an Amazon CloudWatch custom metric"

  is the correct answer.

- ❌ :  "Use an instance type that supports memory usage reporting to a metric by default" is incorrect. There is no

  such thing as an EC2 instance type that supports memory usage reporting to a metric by default. The limitation is not

  in EC2 but in the metrics that are collected by CloudWatch.

- ❌ :  "Call Amazon CloudWatch to retrieve the memory usage metric data that exists for the EC2 instance" is

  incorrect. As there is no standard metric for collecting EC2 memory usage in CloudWatch the data will not already

  exist there to be retrieved.

- ❌ :  "Assign an IAM role to the EC2 instance with an IAM policy granting access to the desired metric"

  is incorrect. This is not an issue of permissions.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management>-

tools/amazon-cloudwatch/

----

- #cloudwatch_custom_metric #amazon_cloudwatch_custom #amazon_cloudwatch #ec2_memory_usage #cloudwatch
