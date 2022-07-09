#### Question  28


**An application running on Amazon EC2 needs to asynchronously invoke an AWS Lambda function to perform data processing.

The services should be decoupled.**


**Which service can be used to decouple the compute services?**


1: Amazon SQS


2: Amazon SNS


3: Amazon MQ


4: AWS Step Functions


Answer: 2


**Explanation:**


You can use a Lambda function to process Amazon Simple Notification Service notifications. Amazon SNS supports Lambda

functions as a target for messages sent to a topic. This solution decouples the Amazon EC2 application from Lambda and

ensures the Lambda function is invoked.


- CORRECT "Amazon SNS" is the correct answer.


- INCORRECT "Amazon SQS" is incorrect. You cannot invoke a Lambda function using Amazon SQS. Lambda can be configured to

  poll a queue, as SQS is pull-based, but it is not push-based like SNS which is what this solution is looking for.


- INCORRECT "Amazon MQ" is incorrect. Amazon MQ is similar to SQS but is used for existing applications that are being

  migrated into AWS. SQS should be used for new applications being created in the cloud.


- INCORRECT "AWS Step Functions" is incorrect. AWS Step Functions is a workflow service. It is not the best solution for

  this scenario.


**References:**


https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html


https://aws.amazon.com/sns/features/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sns/

