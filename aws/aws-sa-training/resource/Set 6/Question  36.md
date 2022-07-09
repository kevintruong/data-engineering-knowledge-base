#### Question  36


**A Solutions Architect enabled Access Logs on an Application Load Balancer (ALB) and needs to process the log files

using a hosted Hadoop service. What configuration changes and services can be leveraged to deliver this requirement?**


1: Configure Access Logs to be delivered to EC2 and install Hadoop for processing the log files


2: Configure Access Logs to be delivered to DynamoDB and use EMR for processing the log files


3: Configure Access Logs to be delivered to S3 and use Kinesis for processing the log files


4: Configure Access Logs to be delivered to S3 and use EMR for processing the log files


**Answer: 4**


**Explanation:**


Access Logs can be enabled on ALB and configured to store data in an S3 bucket. Amazon EMR is a web service that enables

businesses, researchers, data analysts, and developers to easily and cost-effectively process vast amounts of data. EMR

utilizes a hosted Hadoop framework running on Amazon EC2 and Amazon S3.


- CORRECT "Configure Access Logs to be delivered to S3 and use EMR for processing the log files" is the correct answer.


- INCORRECT "Configure Access Logs to be delivered to EC2 and install Hadoop for processing the log files" is incorrect.

  EC2 does not provide a hosted Hadoop service.


- INCORRECT "Configure Access Logs to be delivered to DynamoDB and use EMR for processing the log files" is incorrect.

  You cannot configure access logs to be delivered to DynamoDB.


- INCORRECT "Configure Access Logs to be delivered to S3 and use Kinesis for processing the log files" is incorrect.

  Kinesis does not provide a hosted Hadoop service.


**References:**


https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-emr/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

