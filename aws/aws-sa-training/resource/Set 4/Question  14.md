#### Question  14


**A Solutions Architect is designing an application that will run on an Amazon EC2 instance. The application must

asynchronously invoke and AWS Lambda function to analyze thousands of .CSV files. The services should be decoupled.**


**Which service can be used to decouple the compute services?**


1: Amazon SQS


2: Amazon SNS


3: Amazon Kinesis


4: Amazon OpsWorks


Answer:


**Explanation:**


You can use a Lambda function to process Amazon Simple Notification Service notifications. Amazon SNS supports Lambda

functions as a target for messages sent to a topic. This solution decouples the Amazon EC2 application from Lambda and

ensures the Lambda function is invoked.


- CORRECT "Amazon SNS" is the correct answer.


- INCORRECT "Amazon SQS" is incorrect. You cannot invoke a Lambda function using Amazon SQS. Lambda can be configured to

  poll a queue, as SQS is pull-based, but it is not push-based like SNS which is what this solution requires.


- INCORRECT "Amazon Kinesis" is incorrect as this service is used for ingesting and processing real time streaming data,

  it is not a suitable service to be used solely for invoking a Lambda function.


- INCORRECT "Amazon OpsWorks" is incorrect as this service is used for configuration management of systems using Chef or

  Puppet.


**References:**


https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sns/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/

