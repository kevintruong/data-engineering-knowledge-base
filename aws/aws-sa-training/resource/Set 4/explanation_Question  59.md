*

**Explanation:**

The best way to deliver these requirements is to enable access logs on the ELB and then use EMR for analyzing the log

files

Access Logs on ELB are disabled by default. Information includes information about the clients (not included in

CloudWatch metrics) such as the identity of the requester, IP, request type etc. Logs can be optionally stored and

retained in S3

Amazon EMR is a web service that enables businesses, researchers, data analysts, and developers to easily and

cost-effectively process vast amounts of data. EMR utilizes a hosted Hadoop framework running on Amazon EC2 and Amazon

S3.

* ✅ :  "Use EMR for analyzing the log files" is the correct answer.

* ✅ :  "Enable Access Logs on the ELB and store the log files on S3" is the correct answer.

* ❌ :  "Update the application to use DynamoDB for storing log files" is incorrect. The information recorded by ELB

  access logs is exactly what you require so there is no need to get the application to record the information into

  DynamoDB.

* ❌ :  "Use Elastic Transcoder to analyze the log files" is incorrect. Elastic Transcoder is used for converting

  media file formats not analyzing files.

* ❌ :  "Enable Access Logs on the EC2 instances and store the log files on S3" is incorrect as the access logs on

  the ELB should be enabled.

**References:**

<https://aws.amazon.com/blogs/aws/access-logs-for-elastic-load-balancers/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-emr/>

----
* #dynamodb #<https://aws.amazon.com/blogs/aws/access-logs-for-elastic-load-balancers/> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-emr/> #cloudwatch_metrics #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>>-
