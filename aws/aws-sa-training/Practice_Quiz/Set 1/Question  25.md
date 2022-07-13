#### Question  25

**A new application will run across multiple Amazon ECS tasks. Front-end application logic will process data and then

pass that data to a back-end ECS task to perform further processing and write the data to a datastore. The Architect

would like to reduce-interdependencies so failures do no impact other components.**

**Which solution should the Architect use?**

- [ ] :  Create an Amazon Kinesis Firehose delivery stream and configure the front-end to add data to the stream and the

back-end to read data from the stream

- [ ] :  Create an Amazon Kinesis Firehose delivery stream that delivers data to an Amazon S3 bucket, configure the front-end

to write data to the stream and the back-end to read data from Amazon S3

- [ ] :  Create an Amazon SQS queue that pushes messages to the back-end. Configure the front-end to add messages to the queue

- [x] :  Create an Amazon SQS queue and configure the front-end to add messages to the queue and the back-end to poll the

queue for messages

----

- #multiple_amazon_ecs_tasks #amazon_kinesis_firehose_delivery_stream #amazon_sqs_queue #end_ecs_task #amazon_s3_bucket
- hasExplain:: [[explanation_Question  25.md]]
