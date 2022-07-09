#### Question  14


**A web application in a three-tier architecture runs on a fleet of Amazon EC2 instances. Performance issues have been

reported and investigations point to insufficient swap space. The operations team requires monitoring to determine if

this is correct.**


**What should a solutions architect recommend?**


1: Configure an Amazon CloudWatch SwapUsage metric dimension. Monitor the SwapUsage dimension in the EC2 metrics in

CloudWatch


2: Use EC2 metadata to collect information, then publish it to Amazon CloudWatch custom metrics. Monitor SwapUsage

metrics in CloudWatch


3: Install an Amazon CloudWatch agent on the instances. Run an appropriate script on a set schedule. Monitor

SwapUtilization metrics in CloudWatch


4: Enable detailed monitoring in the EC2 console. Create an Amazon CloudWatch SwapUtilization custom metric. Monitor

SwapUtilization metrics in CloudWatch


Answer: 3


**Explanation:**


You can use the CloudWatch agent to collect both system metrics and log files from Amazon EC2 instances and on-premises

servers. The agent supports both Windows Server and Linux, and enables you to select the metrics to be collected,

including sub-resource metrics such as per-CPU core.


There is now a unified agent and previously there were monitoring scripts. Both of these tools can capture

SwapUtilization metrics and send them to CloudWatch. This is the best way to get memory utilization metrics from Amazon

EC2 instnaces.


- CORRECT "Install an Amazon CloudWatch agent on the instances. Run an appropriate script on a set schedule. Monitor

  SwapUtilization metrics in CloudWatch" is the correct answer.


- INCORRECT "Enable detailed monitoring in the EC2 console. Create an Amazon CloudWatch SwapUtilization custom metric.

  Monitor SwapUtilization metrics in CloudWatch" is incorrect as you do not create custom metrics in the console, you

  must configure the instances to send the metric information to CloudWatch.


- INCORRECT "Configure an Amazon CloudWatch SwapUsage metric dimension. Monitor the SwapUsage dimension in the EC2

  metrics in CloudWatch" is incorrect as there is no SwapUsage metric in CloudWatch. All memory metrics must be custom

  metrics.


- INCORRECT "Use EC2 metadata to collect information, then publish it to Amazon CloudWatch custom metrics. Monitor

  SwapUsage metrics in CloudWatch" is incorrect as performance related information is not stored in metadata.


**References:**


https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-

tools/amazon-cloudwatch/

