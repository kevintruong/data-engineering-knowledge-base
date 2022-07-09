#### Question  50


**A Solutions Architect is designing the messaging and streaming layers of a serverless application. The messaging layer

will manage communications between components and the streaming layer will manage real-time analysis and processing of

streaming data.**


**The Architect needs to select the most appropriate AWS services for these functions. Which services should be used for

the messaging and streaming layers? (Select TWO)**


1: Use Amazon Kinesis for collecting, processing and analyzing real-time streaming data


2: Use Amazon SWF for providing a fully managed messaging service


3: Use Amazon SNS for providing a fully managed messaging service


4: Use Amazon EMR for collecting, processing and analyzing real-time streaming data


5: Use AWS CloudTrail for collecting, processing and analyzing real-time streaming data


**Answer: 1,3**


**Explanation:**


Amazon Kinesis makes it easy to collect, process, and analyze real-time streaming data. With Amazon Kinesis Analytics,

you can run standard SQL or build entire streaming applications using SQL


Amazon Simple Notification Service (Amazon SNS) provides a fully managed messaging service for pub/sub patterns using

asynchronous event notifications and mobile push notifications for microservices, distributed systems, and serverless

applications.


- CORRECT "Use Amazon Kinesis for collecting, processing and analyzing real-time streaming data" is the correct answer.


- CORRECT "Use Amazon SNS for providing a fully managed messaging service" is the correct answer.


- INCORRECT "Use Amazon SWF for providing a fully managed messaging service" is incorrect. Amazon Simple Workflow

  Service is used for executing tasks not sending messages.


- INCORRECT "Use Amazon EMR for collecting, processing and analyzing real-time streaming data" is incorrect. Amazon

  Elastic Map Reduce runs on EC2 instances so is not serverless.


- INCORRECT "Use AWS CloudTrail for collecting, processing and analyzing real-time streaming data" is incorrect. AWS

  CloudTrail is used for recording API activity on your account.


**References:**


https://aws.amazon.com/kinesis/


https://aws.amazon.com/sns/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sns/

