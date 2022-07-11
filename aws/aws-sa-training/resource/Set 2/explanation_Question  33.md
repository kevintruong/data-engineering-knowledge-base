**Explanation:**

The best option is to create multiple queues and configure the application to place orders onto a specific queue based

on the level of service. You then configure the back-end instances to poll these queues in order or priority so they

pick up the higher priority jobs first.

- ✅ :  "Create multiple SQS queues, configure the front-end application to place orders onto a specific queue based

  on the level of service requested and configure the back-end instances to sequentially poll the queues in order of

  priority" is the correct answer.

- ❌ :  "Create multiple SQS queues, configure exactly-once processing and set the maximum visibility timeout to 12

  hours" is incorrect. Creating multiple SQS queues and configuring exactly-once processing (only possible with FIFO)

  would not ensure that the order of the messages is prioritized.

- ❌ :  "Create a combination of FIFO queues and Standard queues and configure the applications to place messages

  into the relevant queue based on priority" is incorrect as creating a mixture of queue types is not the best way to

  separate the messages, and there is nothing in this option that explains how the messages would be picked up in the

  right order.

- ❌ :  "Create a single SQS queue, configure the front-end application to place orders on the queue in order of

  priority and configure the back-end instances to poll the queue and pick up messages in the order they are presented"

  is incorrect. This would not work as standard queues offer best-effort ordering so there’s no guarantee that the

  messages would be picked up in the correct order.

**References:**

<https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>-

integration/amazon-sqs/

----

- #multiple_sqs_queues #single_sqs_queue #specific_queue #multiple_queues #<https://docs.aws.amazon.com/awssimplequeueservice/latest/sqsdeveloperguide/standard-queues.html>
