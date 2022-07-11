### Application Integration Quiz Questions


Answers and explanations are provided below after the last question in this section.


**Question 1:**


There is expected to be a large increase in write intensive traffic to a website you manage that registers users onto an

online learning program. You are concerned about writes to the database being dropped and need to come up with a

solution to ensure this does not happen. Which of the solution options below would be the best approach to take?


```

A. Update the application to write data to an SQS queue and provision additional EC2

instances to process the data and write it to the database

B. Use RDS in a multi-AZ configuration to distribute writes across AZs

C. Update the application to write data to an S3 bucket and provision additional EC2 instances

to process the data and write it to the database

D. Use CloudFront to cache the writes and configure the database as a custom origin

```


**Question 2:**


You are using a series of Spot instances that process messages from an SQS queue and store results in a DynamoDB table.

Shortly after picking up a message from the queue AWS terminated the Spot instance. The Spot instance had not finished

processing the message. What will happen to the message?


```

A. The message will be lost as it would have been deleted from the queue when processed

B. The message will remain in the queue and be immediately picked up by another instance

C. The message will become available for processing again after the visibility timeout expires

D. The results may be duplicated in DynamoDB as the message will likely be processed multiple

times

```


**Question 3:**


You are developing a multi-tier application that includes loosely-coupled, distributed application components and need

to determine a method of sending notifications instantaneously. Using SNS which transport protocols are supported? (

choose 2)


```

A. FTP

B. Email-JSON

C. HTTPS

D. Amazon SWF

E. AWS Lambda

```


**Question 4:**


A Solutions Architect is creating the business process workflows associated with an order fulfilment system. What AWS

service can assist with coordinating tasks across distributed application components?


```

A. Amazon STS

B. Amazon SQS

C. Amazon SWF

```


```

D. Amazon SNS

```


**Question 5:**


You are a developer at Digital Cloud Training. An application stack you are building needs a message bus to decouple the

application components from each other. The application will generate up to 300 messages per second without using

batching. You need to ensure that a message is only delivered once, and duplicates are not introduced into the queue. It

is not necessary to maintain the order of the messages.


Which SQS queue type will you use?


```

A. Standard queues

B. Long polling queues

C. Auto Scaling queues

D. FIFO queues

```


**Question 6:**


A client is in the design phase of developing an application that will process orders for their online ticketing system.

The application will use a number of front-end EC2 instances that pick-up orders and place them in a queue for

processing by another set of back-end EC2 instances. The client will have multiple options for customers to choose the

level of service they want to pay for.


The client has asked how he can design the application to process the orders in a prioritized way based on the level of

service the customer has chosen?


```

A. Create multiple SQS queues, configure the front-end application to place orders onto a

specific queue based on the level of service requested and configure the back-end instances

to sequentially poll the queues in order of priority

B. Create a combination of FIFO queues and Standard queues and configure the applications to

place messages into the relevant queue based on priority

C. Create a single SQS queue, configure the front-end application to place orders on the queue

in order of priority and configure the back-end instances to poll the queue and pick up

messages in the order they are presented

D. Create multiple SQS queues, configure exactly-once processing and set the maximum

visibility timeout to 12 hours

```


**APPLICATION INTEGRATION - ANSWERS**


**Question 1 answer: A**


Explanation:


```

This is a great use case for Amazon Simple Queue Service (Amazon SQS). SQS is a web service

that gives you access to message queues that store messages waiting to be processed and offers

a reliable, highly-scalable, hosted queue for storing messages in transit between computers. SQS

is used for distributed/decoupled applications. In this circumstance SQS will reduce the risk of

writes being dropped and it the best option presented.

RDS in a multi-AZ configuration will not help as writes are only made to the primary database.

Though writing data to an S3 bucket could potentially work, it is not the best option as SQS is

recommended for decoupling application components.

The CloudFront option is bogus as you cannot configure a database as a custom origin in

CloudFront.

```


**Question 2 answer: C**


Explanation:


```

The visibility timeout is the amount of time a message is invisible in the queue after a reader

picks up the message. If a job is processed within the visibility timeout the message will be

deleted. If a job is not processed within the visibility timeout the message will become visible

again (could be delivered twice). The maximum visibility timeout for an Amazon SQS message is

12 hours.

The message will not be lost and will not be immediately picked up by another instance. As

mentioned above it will be available for processing in the queue again after the timeout expires.

As the instance had not finished processing the message it should only be fully processed once.

Depending on your application process however it is possible some data was written to

DynamoDB.

```


**Question 3 answer: B,C**


Explanation:


```

Note that the questions asks you which transport protocols are supported, NOT which

subscribers - therefore Lambda is not supported

SNS supports notifications over multiple transport protocols:

```


- HTTP/HTTPS – subscribers specify a URL as part of the subscription registration

- Email/Email-JSON – messages are sent to registered addresses as email (text-based or JSON- object)

- SQS – users can specify an SQS standard queue as the endpoint

- SMS – messages are sent to registered phone numbers as SMS text messages


**Question 4 answer: C**


Explanation:


```

Amazon Simple Workflow Service (SWF) is a web service that makes it easy to coordinate work

across distributed application components. SWF enables applications for a range of use cases,

including media processing, web application back-ends, business process workflows, and

analytics pipelines, to be designed as a coordination of tasks.

Amazon Security Token Service (STS) is used for requesting temporary credentials.

Amazon Simple Queue Service (SQS) is a message queue used for decoupling application

components.

Amazon Simple Notification Service (SNS) is a web service that makes it easy to set up, operate,

and send notifications from the cloud.

SNS supports notifications over multiple transports including HTTP/HTTPS, Email/Email-JSON,

SQS and SMS.

```


**Question 5 answer: D**


Explanation:


```

The key fact you need to consider here is that duplicate messages cannot be introduced into the

queue. For this reason alone you must use a FIFO queue. The statement about it not being

necessary to maintain the order of the messages is meant to confuse you, as that might lead you

to think you can use a standard queue, but standard queues don't guarantee that duplicates are

not introduced into the queue.

FIFO (first-in-first-out) queues preserve the exact order in which messages are sent and received

```


- note that this is not required in the question but exactly once processing is. FIFO queues provide exactly-once

  processing, which means that each message is delivered once and remains available until a consumer processes it and

  deletes it. Standard queues provide a loose-FIFO capability that attempts to preserve the order of messages. Standard

  queues provide at-least-once delivery, which means that each message is delivered at least once. Long polling is

  configuration you can apply to a queue, it is not a queue type. There is no such thing as an Auto Scaling queue.


**Question 6 answer: A**


Explanation:


```

The best option is to create multiple queues and configure the application to place orders onto a

specific queue based on the level of service. You then configure the back-end instances to poll

these queues in order or priority, so they pick up the higher priority jobs first.

Creating a combination of FIFO and standard queues is incorrect as creating a mixture of queue

types is not the best way to separate the messages, and there is nothing in this option that

explains how the messages would be picked up in the right order.

Creating a single queue and configuring the applications to place orders on the queue in order of

priority would not work as standard queues offer best-effort ordering so there’s no guarantee

that the messages would be picked up in the correct order.

```


Creating multiple SQS queues and configuring exactly-once processing (only possible with FIFO)

would not ensure that the order of the messages is prioritized.

