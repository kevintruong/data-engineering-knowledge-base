#### Question  33


```

Amazon CloudFront

```


```

Distribution

```


```

Distribution User

```


```

S 3 Bucket

```


```

EC 2 Instance

```


```

Application

Load Balancer

EC 2 Instance

```


```

S 3 Origin:

```


```

S 3 Static

Website

```


```

Custom Origin:

```


```

Custom Origin:

```


```

Web Distribution:

```


- Static and dynamic content

- HTTP/HTTPS

- Add/update/delete objects + webforms

- Real time live streaming RTMP Distribution:

- Uses Adobe Flash Media RTMP protocol

- Can play media file before downloaded

- Must use S 3 origin


**A client is in the design phase of developing an application that will process orders for their online ticketing

system. The application will use a number of front-end EC2 instances that pick-up orders and place them in a queue for

processing by another set of back-end EC2 instances. The client will have multiple options for customers to choose the

level of service they want to pay for.**


**The client has asked how he can design the application to process the orders in a prioritized way based on the level

of service the customer has chosen?**


1: Create multiple SQS queues, configure exactly-once processing and set the maximum visibility timeout to 12 hours


2: Create multiple SQS queues, configure the front-end application to place orders onto a specific queue based on the

level of service requested and configure the back-end instances to sequentially poll the queues in order of priority


3: Create a combination of FIFO queues and Standard queues and configure the applications to place messages into the

relevant queue based on priority


4: Create a single SQS queue, configure the front-end application to place orders on the queue in order of priority and

configure the back-end instances to poll the queue and pick up messages in the order they are presented


Answer: 2


**Explanation:**


The best option is to create multiple queues and configure the application to place orders onto a specific queue based

on the level of service. You then configure the back-end instances to poll these queues in order or priority so they

pick up the higher priority jobs first.


- CORRECT "Create multiple SQS queues, configure the front-end application to place orders onto a specific queue based

  on the level of service requested and configure the back-end instances to sequentially poll the queues in order of

  priority" is the correct answer.


- INCORRECT "Create multiple SQS queues, configure exactly-once processing and set the maximum visibility timeout to 12

  hours" is incorrect. Creating multiple SQS queues and configuring exactly-once processing (only possible with FIFO)

  would not ensure that the order of the messages is prioritized.


- INCORRECT "Create a combination of FIFO queues and Standard queues and configure the applications to place messages

  into the relevant queue based on priority" is incorrect as creating a mixture of queue types is not the best way to

  separate the messages, and there is nothing in this option that explains how the messages would be picked up in the

  right order.


- INCORRECT "Create a single SQS queue, configure the front-end application to place orders on the queue in order of

  priority and configure the back-end instances to poll the queue and pick up messages in the order they are presented"

  is incorrect. This would not work as standard queues offer best-effort ordering so there’s no guarantee that the

  messages would be picked up in the correct order.


**References:**


https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

