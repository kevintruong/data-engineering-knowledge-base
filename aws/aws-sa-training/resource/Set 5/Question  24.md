#### Question  24


**An application stack is being created which needs a message bus to decouple the application components from each

other. The application will generate up to 300 messages per second without using batching. A Solutions Architect needs

to ensure that a message is delivered only once and duplicates are not introduced into the queue. It is not necessary to

maintain the order of the messages.**


**Which SQS queue type should be used?**


1: Standard queues


2: Long polling queues


3: FIFO queues


4: Auto Scaling queues


**Answer: 3**


**Explanation:**


The key fact you need to consider here is that duplicate messages cannot be introduced into the queue. For this reason

alone you must use a FIFO queue. The statement about it not being necessary to maintain the order of the messages is

meant to confuse you, as that might lead you to think you can use a standard queue, but standard queues don’t guarantee

that duplicates are not introduced into the queue.


FIFO (first-in-first-out) queues preserve the exact order in which messages are sent and received – note that this is

not required in the question but exactly once processing is. FIFO queues provide exactly-once processing, which means

that each message is delivered once and remains available until a consumer processes it and deletes it.


- CORRECT "FIFO queues" is the correct answer.


- INCORRECT "Standard queues" is incorrect. Standard queues provide a loose-FIFO capability that attempts to preserve

  the order of messages. Standard queues provide at-least-once delivery, which means that each message is delivered at

  least once.


- INCORRECT "Long polling queues" is incorrect. Long polling is configuration you can apply to a queue, it is not a

  queue type.


- INCORRECT "Auto Scaling queues" is incorrect. There is no such thing as an Auto Scaling queue.


**References:**


https://aws.amazon.com/sqs/features/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

