#### Question  25


**A new application will run across multiple Amazon ECS tasks. Front-end application logic will process data and then

pass that data to a back-end ECS task to perform further processing and write the data to a datastore. The Architect

would like to reduce-interdependencies so failures do no impact other components.**


**Which solution should the Architect use?**


1 : Create an Amazon Kinesis Firehose delivery stream and configure the front-end to add data to the stream and the

back-end to read data from the stream


2: Create an Amazon Kinesis Firehose delivery stream that delivers data to an Amazon S3 bucket, configure the front-end

to write data to the stream and the back-end to read data from Amazon S3


3: Create an Amazon SQS queue that pushes messages to the back-end. Configure the front-end to add messages to the queue


4: Create an Amazon SQS queue and configure the front-end to add messages to the queue and the back-end to poll the

queue for messages


Answer: 4


**Explanation:**


This is a good use case for Amazon SQS. SQS is a service that is used for decoupling applications, thus reducing

interdependencies, through a message bus. The front-end application can place messages on the queue and the back-end can

then poll the queue for new messages. Please remember that Amazon SQS is pull-based

(polling) not push-based (use SNS for push-based).


- CORRECT "Create an Amazon SQS queue and configure the front-end to add messages to the queue and the back-end to poll

  the queue for messages" is the correct answer.


- INCORRECT "Create an Amazon Kinesis Firehose delivery stream and configure the front-end to add data to the stream and

  the back-end to read data from the stream" is incorrect. Amazon Kinesis Firehose is used for streaming data. With

  Firehose the data is immediately loaded into a destination that can be Amazon S3, RedShift, Elasticsearch, or Splunk.

  This is not an ideal use case for Firehose as this is not streaming data and there is no need to load data into an

  additional AWS service.


- INCORRECT "Create an Amazon Kinesis Firehose delivery stream that delivers data to an Amazon S3 bucket, configure the

  front-end to write data to the stream and the back-end to read data from Amazon S3" is incorrect as per the previous

  explanation.


- INCORRECT "Create an Amazon SQS queue that pushes messages to the back-end. Configure the front-end to add messages to

  the queue " is incorrect as SQS is pull-based, not push-based. EC2 instances must poll the queue to find jobs to

  process.


**References:**


https://docs.aws.amazon.com/AmazonECS/latest/developerguide/common_use_cases.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

