#### Question  16


**A company have 500 TB of data in an on-premises file share that needs to be moved to Amazon S3 Glacier. The migration

must not saturate the company’s low-bandwidth internet connection and the migration must be completed within a few

weeks.**


**What is the MOST cost-effective solution?**


1: Create an AWS Direct Connect connection and migrate the data straight into Amazon Glacier


2: Order 7 AWS Snowball appliances and select an S3 Glacier vault as the destination. Create a bucket policy to enforce

a VPC endpoint


3: Use AWS Global Accelerator to accelerate upload and optimize usage of the available bandwidth


4: Order 7 AWS Snowball appliances and select an Amazon S3 bucket as the destination. Create a lifecycle policy to

transition the S3 objects to Amazon S3 Glacier


Answer: 4


**Explanation:**


As the company’s internet link is low-bandwidth uploading directly to Amazon S3 (ready for transition to Glacier) would

saturate the link. The best alternative is to use AWS Snowball appliances. The Snowball edge appliance can hold up to 80

TB of data so 7 devices would be required to migrate 500 TB of data.


Snowball moves data into AWS using a hardware device and the data is then copied into an Amazon S3 bucket of your

choice. From there, lifecycle policies can transition the S3 objects to Amazon S3 Glacier.


- CORRECT "Order 7 AWS Snowball appliances and select an Amazon S3 bucket as the destination. Create a lifecycle policy

  to transition the S3 objects to Amazon S3 Glacier" is the correct answer.


- INCORRECT "Order 7 AWS Snowball appliances and select an S3 Glacier vault as the destination. Create a bucket policy

  to enforce a VPC endpoint" is incorrect as you cannot set a Glacier vault as the destination, it must be an S3 bucket.

  You also can’t enforce a VPC endpoint using a bucket policy.


- INCORRECT "Create an AWS Direct Connect connection and migrate the data straight into Amazon Glacier" is incorrect as

  this is not the most cost-effective option and takes time to setup.


- INCORRECT "Use AWS Global Accelerator to accelerate upload and optimize usage of the available bandwidth" is incorrect

  as this service is not used for accelerating or optimizing the upload of data from on- premises networks.


**References:**


https://docs.aws.amazon.com/snowball/latest/developer-guide/specifications.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

