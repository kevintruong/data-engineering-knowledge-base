**Explanation:**

Processing each part using a separate ECS task may not be essential but means you can separate the processing of the

data. An Amazon Simple Queue Service (SQS) is used for decoupling applications. It is a message queue on which you place

messages for processing by application components. In this case you can process each data processing part in separate

ECS tasks and have them write an Amazon SQS queue. That way the backend can pick up the messages from the queue when

they’re ready and there is no delay due to the second part not being complete.

- ✅ :  "Process each part using a separate ECS task. Create an Amazon SQS queue" is the correct answer.

- ❌ :  "Process both parts using the same ECS task. Create an Amazon Kinesis Firehose stream" is incorrect. Amazon

  Kinesis Firehose is used for streaming data. This is not an example of streaming data. In this case SQS is better as a

  message can be placed on a queue to indicate that the job is complete and ready to be picked up by the backend

  application component.

- ❌ :  "Process each part using a separate ECS task. Create an Amazon SNS topic and send a notification when the

  processing completes" is incorrect. Amazon Simple Notification Service (SNS) can be used for sending notifications. It

  is useful when you need to notify multiple AWS services. In this case an Amazon SQS queue is a better solution as

  there is no mention of multiple AWS services and this is an ideal use case for SQS.

- ❌ :  "Create an Amazon DynamoDB table and save the output of the first part to the table" is incorrect. Amazon

  DynamoDB is unlikely to be a good solution for this requirement. There is a limit on the maximum amount of data that

  you can store in an entry in a DynamoDB table.

**References:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>-

integration/amazon-sqs/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>-

integration/amazon-sqs/

----

- #ecs_tasks #amazon_sqs_queue #amazon_simple_queue_service #separate_ecs_task #same_ecs_task
