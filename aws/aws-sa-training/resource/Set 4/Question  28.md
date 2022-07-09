#### Question  28


**An Auto Scaling Group is unable to respond quickly enough to load changes resulting in lost messages from another

application tier. The messages are typically around 128KB in size.**


**What is the best design option to prevent the messages from being lost?**


1: Store the messages on Amazon S3


2: Launch an Elastic Load Balancer


3: Store the messages on an SQS queue


4: Use larger EC2 instance sizes


**Answer: 3**


**Explanation:**


In this circumstance the ASG cannot launch EC2 instances fast enough. You need to be able to store the messages

somewhere so they don’t get lost whilst the EC2 instances are launched. This is a classic use case for decoupling and

SQS is designed for exactly this purpose.


Amazon Simple Queue Service (Amazon SQS) is a web service that gives you access to message queues that store messages

waiting to be processed. SQS offers a reliable, highly-scalable, hosted queue for storing messages in transit between

computers. An SQS queue can be used to create distributed/decoupled applications.


- CORRECT "Store the messages on an SQS queue" is the correct answer.


- INCORRECT "Store the messages on Amazon S3" is incorrect. Storing the messages on S3 is potentially feasible but SQS

  is the preferred solution as it is designed for decoupling. If the messages are over 256KB and therefore cannot be

  stored in SQS, you may want to consider using S3 and it can be used in combination with SQS by using the Amazon SQS

  Extended Client Library for Java.


- INCORRECT "Launch an Elastic Load Balancer" is incorrect. An ELB can help to distribute incoming connections to the

  back-end EC2 instances however if the ASG is not scaling fast enough then there aren’t enough resources for the ELB to

  distribute traffic to.


- INCORRECT "Use larger EC2 instance sizes" is incorrect. Scaling horizontally and decoupling will have a greater effect

  over using larger instance sizes.


**References:**


https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

