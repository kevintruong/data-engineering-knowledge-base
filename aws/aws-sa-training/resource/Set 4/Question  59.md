#### Question  59


**An application running AWS uses an Elastic Load Balancer (ELB) to distribute connections between EC2 instances. A

Solutions Architect needs to record information on the requester, IP, and request type for connections made to the ELB.

Additionally, the Architect will also need to perform some analysis on the log files.**


**Which AWS services and configuration options can be used to collect and then analyze the logs? (Select TWO)**


1: Use EMR for analyzing the log files


2: Update the application to use DynamoDB for storing log files


3: Use Elastic Transcoder to analyze the log files


4: Enable Access Logs on the ELB and store the log files on S3


5: Enable Access Logs on the EC2 instances and store the log files on S3


**Answer: 1,4**


**Explanation:**


The best way to deliver these requirements is to enable access logs on the ELB and then use EMR for analyzing the log

files


Access Logs on ELB are disabled by default. Information includes information about the clients (not included in

CloudWatch metrics) such as the identity of the requester, IP, request type etc. Logs can be optionally stored and

retained in S3


Amazon EMR is a web service that enables businesses, researchers, data analysts, and developers to easily and

cost-effectively process vast amounts of data. EMR utilizes a hosted Hadoop framework running on Amazon EC2 and Amazon

S3.


- CORRECT "Use EMR for analyzing the log files" is the correct answer.


- CORRECT "Enable Access Logs on the ELB and store the log files on S3" is the correct answer.


- INCORRECT "Update the application to use DynamoDB for storing log files" is incorrect. The information recorded by ELB

  access logs is exactly what you require so there is no need to get the application to record the information into

  DynamoDB.


- INCORRECT "Use Elastic Transcoder to analyze the log files" is incorrect. Elastic Transcoder is used for converting

  media file formats not analyzing files.


- INCORRECT "Enable Access Logs on the EC2 instances and store the log files on S3" is incorrect as the access logs on

  the ELB should be enabled.


**References:**


https://aws.amazon.com/blogs/aws/access-logs-for-elastic-load-balancers/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-emr/

