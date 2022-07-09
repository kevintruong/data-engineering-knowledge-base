#### Question  63


**An application you are designing receives and processes files. The files are typically around 4GB in size and the

application extracts metadata from the files which typically takes a few seconds for each file. The pattern of updates

is highly dynamic with times of little activity and then multiple uploads within a short period of time.**


**What architecture will address this workload the most cost efficiently?**


1: Use a Kinesis data stream to store the file, and use Lambda for processing


2: Store the file in an EBS volume which can then be accessed by another EC2 instance for processing


3: Upload files into an S3 bucket, and use the Amazon S3 event notification to invoke a Lambda function to extract the

metadata


4: Place the files in an SQS queue, and use a fleet of EC2 instances to extract the metadata


Answer: 3


**Explanation:**


Storing the file in an S3 bucket is the most cost-efficient solution, and using S3 event notifications to invoke a

Lambda function works well for this unpredictable workload.


The following diagram depicts a similar architecture where users upload documents to an Amazon S3 bucket and an event

notification triggers a Lambda function that resizes the image.


- CORRECT "Upload files into an S3 bucket, and use the Amazon S3 event notification to invoke a Lambda function to

  extract the metadata" is the correct answer.


- INCORRECT "Use a Kinesis data stream to store the file, and use Lambda for processing" is incorrect. Kinesis data

  streams runs on EC2 instances and you must therefore provision some capacity even when the application is not

  receiving files. This is not as cost-efficient as storing them in an S3 bucket prior to using Lambda for the

  processing.


- INCORRECT "Store the file in an EBS volume which can then be accessed by another EC2 instance for processing" is

  incorrect. Storing the file in an EBS volume and using EC2 instances for processing is not cost efficient.


- INCORRECT "Place the files in an SQS queue, and use a fleet of EC2 instances to extract the metadata" is incorrect.

  SQS queues have a maximum message size of 256KB. You can use the extended client library for Java to use pointers to a

  payload on S3 but the maximum payload size is 2GB.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

