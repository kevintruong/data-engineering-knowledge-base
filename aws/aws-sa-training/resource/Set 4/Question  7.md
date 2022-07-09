#### Question  7


**A company is migrating a decoupled application to AWS. The application uses a message broker based on the MQTT

protocol. The application will be migrated to Amazon EC2 instances and the solution for the message broker must not

require rewriting application code.**


**Which AWS service can be used for the migrated message broker?**


1: Amazon SQS


2: Amazon SNS


3: Amazon MQ


4: AWS Step Functions


Answer: 3


**Explanation:**


Amazon MQ is a managed message broker service for Apache ActiveMQ that makes it easy to set up and operate message

brokers in the cloud. Connecting current applications to Amazon MQ is easy because it uses industry-standard APIs and

protocols for messaging, including JMS, NMS, AMQP, STOMP, MQTT, and WebSocket. Using standards means that in most cases,

there’s no need to rewrite any messaging code when you migrate to AWS.


- CORRECT "Amazon MQ" is the correct answer.


- INCORRECT "Amazon SQS" is incorrect. This is an Amazon proprietary service and does not support industry- standard

  messaging APIs and protocols.


- INCORRECT "Amazon SNS" is incorrect. This is a notification service not a message bus.


- INCORRECT "AWS Step Functions" is incorrect. This is a workflow orchestration service, not a message bus.


**References:**


https://aws.amazon.com/amazon-mq/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-mq/

