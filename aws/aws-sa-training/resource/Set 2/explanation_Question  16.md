**Explanation:**

As the company’s internet link is low-bandwidth uploading directly to Amazon S3 (ready for transition to Glacier) would

saturate the link. The best alternative is to use AWS Snowball appliances. The Snowball edge appliance can hold up to 80

TB of data so 7 devices would be required to migrate 500 TB of data.

Snowball moves data into AWS using a hardware device and the data is then copied into an Amazon S3 bucket of your

choice. From there, lifecycle policies can transition the S3 objects to Amazon S3 Glacier.

- ✅ :  "Order 7 AWS Snowball appliances and select an Amazon S3 bucket as the destination. Create a lifecycle policy

  to transition the S3 objects to Amazon S3 Glacier" is the correct answer.

- ❌ :  "Order 7 AWS Snowball appliances and select an S3 Glacier vault as the destination. Create a bucket policy

  to enforce a VPC endpoint" is incorrect as you cannot set a Glacier vault as the destination, it must be an S3 bucket.

  You also can’t enforce a VPC endpoint using a bucket policy.

- ❌ :  "Create an AWS Direct Connect connection and migrate the data straight into Amazon Glacier" is incorrect as

  this is not the most cost-effective option and takes time to setup.

- ❌ :  "Use AWS Global Accelerator to accelerate upload and optimize usage of the available bandwidth" is incorrect

  as this service is not used for accelerating or optimizing the upload of data from on- premises networks.

**References:**

<https://docs.aws.amazon.com/snowball/latest/developer-guide/specifications.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #amazon_s3_glacier #amazon_s3_bucket #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #s3_glacier_vault #s3_bucket
