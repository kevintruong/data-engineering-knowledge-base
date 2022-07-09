#### Question  20


**A company is planning to migrate a large quantity of important data to Amazon S3. The data will be uploaded to a

versioning enabled bucket in the us-west-1 Region. The solution needs to include replication of the data to another

Region for disaster recovery purposes.**


**How should a solutions architect configure the replication?**


1: Create an additional S3 bucket in another Region and configure cross-Region replication


2: Create an additional S3 bucket in another Region and configure cross-origin resource sharing (CORS)


3: Create an additional S3 bucket with versioning in another Region and configure cross-Region replication


4: Create an additional S3 bucket with versioning in another Region and configure cross-origin resource sharing

(CORS)


Answer: 3


**Explanation:**


Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. Buckets that are configured for

object replication can be owned by the same AWS account or by different accounts. You can copy objects between different

AWS Regions or within the same Region. Both source and destination buckets must have versioning enabled.


- CORRECT "Create an additional S3 bucket with versioning in another Region and configure cross-Region replication"

  is the correct answer.


- INCORRECT "Create an additional S3 bucket in another Region and configure cross-Region replication" is incorrect as

  the destination bucket must also have versioning enabled.


- INCORRECT "Create an additional S3 bucket in another Region and configure cross-origin resource sharing

  (CORS)" is incorrect as CORS is not related to replication.


- INCORRECT "Create an additional S3 bucket with versioning in another Region and configure cross-origin resource

  sharing (CORS)" is incorrect as CORS is not related to replication.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

