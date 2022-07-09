#### Question  10


**A Solutions Architect is rearchitecting an application with decoupling. The application will send batches of up to

1000 messages per second that must be received in the correct order by the consumers.**


**Which action should the Solutions Architect take?**


1: Create an Amazon SQS Standard queue


2: Create an Amazon SNS topic


3: Create an Amazon SQS FIFO queue


4: Create an AWS Step Functions state machine


Answer: 3


**Explanation:**


Only FIFO queues guarantee the ordering of messages and therefore a standard queue would not work. The FIFO queue

supports up to 3,000 messages per second with batching so this is a supported scenario.


- CORRECT "Create an Amazon SQS FIFO queue" is the correct answer.


- INCORRECT "Create an Amazon SQS Standard queue" is incorrect as it does not guarantee ordering of messages.


- INCORRECT "Create an Amazon SNS topic" is incorrect. SNS is a notification service and a message queue is a better fit

  for this use case.


- INCORRECT "Create an AWS Step Functions state machine" is incorrect. Step Functions is a workflow orchestration

  service and is not useful for this scenario.


**References:**


https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

