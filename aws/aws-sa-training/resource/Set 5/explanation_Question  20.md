**Explanation:**

The question asks for the most cost-effective solution and therefor a serverless and automated solution will be the best

choice.

AWS Lambda can run custom code in response to Amazon S3 bucket events. You upload your custom code to AWS Lambda and

create a function. When Amazon S3 detects an event of a specific type (for example, an object created event), it can

publish the event to AWS Lambda and invoke your function in Lambda. In response, AWS Lambda executes your function.

- ✅ :  "Write the log files to an Amazon S3 bucket. Create an event notification to invoke an AWS Lambda function

  that will process the files" is the correct answer.

- ❌ :  "Write the log files to an Amazon EC2 instance with an attached EBS volume. After processing, save the files

  to an Amazon S3 bucket" is incorrect. This is not cost effective as it is not serverless.

- ❌ :  "Write the log files to an Amazon SQS queue. Use AWS Lambda to process the files from the queue and save to

  an Amazon S3 bucket" is incorrect. SQS has a maximum message size of 256 KB so the message body would need to be saved

  in S3 anyway. Using an event source mapping from S3 would be less complex and preferable.

- ❌ :  "Write the log files to an Amazon S3 bucket. Create an event notification to invoke an Amazon ECS task to

  process the files and save to an Amazon S3 bucket" is incorrect. You cannot use event notifications to process Amazon

  ECS tasks.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/>

----

- #aws_lambda #amazon_s3_bucket_events #aws_lambda_function #amazon_s3_bucket #amazon_ecs_task
