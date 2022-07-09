#### Question  25


**An application on Amazon Elastic Container Service (ECS) performs data processing in two parts. The second part takes

much longer to complete. How can an Architect decouple the data processing from the backend application component?**


1: Process both parts using the same ECS task. Create an Amazon Kinesis Firehose stream


2: Process each part using a separate ECS task. Create an Amazon SNS topic and send a notification when the processing

completes


3: Create an Amazon DynamoDB table and save the output of the first part to the table


4: Process each part using a separate ECS task. Create an Amazon SQS queue


Answer: 4


**Explanation:**


Processing each part using a separate ECS task may not be essential but means you can separate the processing of the

data. An Amazon Simple Queue Service (SQS) is used for decoupling applications. It is a message queue on which you place

messages for processing by application components. In this case you can process each data processing part in separate

ECS tasks and have them write an Amazon SQS queue. That way the backend can pick up the messages from the queue when

they’re ready and there is no delay due to the second part not being complete.


- CORRECT "Process each part using a separate ECS task. Create an Amazon SQS queue" is the correct answer.


- INCORRECT "Process both parts using the same ECS task. Create an Amazon Kinesis Firehose stream" is incorrect. Amazon

  Kinesis Firehose is used for streaming data. This is not an example of streaming data. In this case SQS is better as a

  message can be placed on a queue to indicate that the job is complete and ready to be picked up by the backend

  application component.


- INCORRECT "Process each part using a separate ECS task. Create an Amazon SNS topic and send a notification when the

  processing completes" is incorrect. Amazon Simple Notification Service (SNS) can be used for sending notifications. It

  is useful when you need to notify multiple AWS services. In this case an Amazon SQS queue is a better solution as

  there is no mention of multiple AWS services and this is an ideal use case for SQS.


- INCORRECT "Create an Amazon DynamoDB table and save the output of the first part to the table" is incorrect. Amazon

  DynamoDB is unlikely to be a good solution for this requirement. There is a limit on the maximum amount of data that

  you can store in an entry in a DynamoDB table.


**References:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

