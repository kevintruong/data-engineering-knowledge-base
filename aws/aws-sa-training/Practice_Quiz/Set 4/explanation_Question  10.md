**Explanation:**

Only FIFO queues guarantee the ordering of messages and therefore a standard queue would not work. The FIFO queue

supports up to 3,000 messages per second with batching so this is a supported scenario.

- ✅ :  "Create an Amazon SQS FIFO queue" is the correct answer.

- ❌ :  "Create an Amazon SQS Standard queue" is incorrect as it does not guarantee ordering of messages.

- ❌ :  "Create an Amazon SNS topic" is incorrect. SNS is a notification service and a message queue is a better fit

  for this use case.

- ❌ :  "Create an AWS Step Functions state machine" is incorrect. Step Functions is a workflow orchestration

  service and is not useful for this scenario.

**References:**

<https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>-

integration/amazon-sqs/

----

- #amazon_sqs_fifo_queue #amazon_sqs_standard_queue #aws_step_functions_state_machine #message_queue #fifo_queue
