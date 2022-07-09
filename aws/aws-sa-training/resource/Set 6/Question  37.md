#### Question  37


**A web application receives order processing information from customers and places the messages on an Amazon SQS queue.

A fleet of Amazon EC2 instances are configured to pick up the messages, process them, and store the results in a

DynamoDB table. The current configuration has been resulting in a large number of empty responses to ReceiveMessage API

requests.**


**A Solutions Architect needs to eliminate empty responses to reduce operational overhead. How can this be done?**


1: Use a Standard queue to provide at-least-once delivery, which means that each message is delivered at least once


2: Use a FIFO (first-in-first-out) queue to preserve the exact order in which messages are sent and received


3: Configure Long Polling to eliminate empty responses by allowing Amazon SQS to wait until a message is available in a

queue before sending a response


4: Configure Short Polling to eliminate empty responses by reducing the length of time a connection request remains open


**Answer: 3**


**Explanation:**


The correct answer is to use Long Polling which will eliminate empty responses by allowing Amazon SQS to wait until a

message is available in a queue before sending a response.


The problem does not relate to the order in which the messages are processed in and there are no concerns over messages

being delivered more than once so it doesn’t matter whether you use a FIFO or standard queue.


**Long Polling:**


- Uses fewer requests and reduces cost.

- Eliminates false empty responses by querying all servers.

- SQS waits until a message is available in the queue before sending a response.


**Short Polling:**


- Does not wait for messages to appear in the queue.

- It queries only a subset of the available servers for messages (based on weighted random execution).

- Short polling is the default.

- ReceiveMessageWaitTime is set to 0.


- CORRECT "Configure Long Polling to eliminate empty responses by allowing Amazon SQS to wait until a message is

  available in a queue before sending a response" is the correct answer.


- INCORRECT "Use a Standard queue to provide at-least-once delivery, which means that each message is delivered at least

  once" is incorrect as explained above.


- INCORRECT "Use a FIFO (first-in-first-out) queue to preserve the exact order in which messages are sent and received"

  is incorrect as explained above.


- INCORRECT "Configure Short Polling to eliminate empty responses by reducing the length of time a connection request

  remains open" is incorrect as explained above.


**References:**


https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-

polling.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

