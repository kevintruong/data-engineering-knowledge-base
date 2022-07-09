#### Question  59


**A Solutions Architect needs to monitor application logs and receive a notification whenever a specific number of

occurrences of certain HTTP status code errors occur. Which tool should the Architect use?**


1: CloudWatch Metrics


2: CloudWatch Events


3: CloudTrail Trails


4: CloudWatch Logs


Answer: 4


**Explanation:**


You can use CloudWatch Logs to monitor applications and systems using log data. For example, CloudWatch Logs can track

the number of errors that occur in your application logs and send you a notification whenever the rate of errors exceeds

a threshold you specify. This is the best tool for this requirement.


- CORRECT "CloudWatch Logs" is the correct answer.


- INCORRECT "CloudWatch Metrics" is incorrect. CloudWatch Metrics are the fundamental concept in CloudWatch. A metric

  represents a time-ordered set of data points that are published to CloudWatch. You cannot use a metric alone, it is

  used when setting up monitoring for any service in CloudWatch.


- INCORRECT "CloudWatch Events" is incorrect. Amazon CloudWatch Events delivers a near real-time stream of system events

  that describe changes in Amazon Web Services (AWS) resources. Though you can generate custom application-level events

  and publish them to CloudWatch Events this is not the best tool for monitoring application logs.


- INCORRECT "CloudTrail Trails" is incorrect. CloudTrail is used for monitoring API activity on your account, not for

  monitoring application logs.


**References:**


https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-

tools/amazon-cloudwatch/

