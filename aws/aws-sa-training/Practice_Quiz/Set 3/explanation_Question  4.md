**Explanation:**

The application is writing the files using API calls which means it will be compatible with Amazon S3 which uses a REST

API. S3 is a massively scalable key-based object store that is well-suited to allowing concurrent access to the files

from many instances.

Amazon S3 will also be the most cost-effective choice. A rough calculation using the AWS pricing calculator shows the

cost differences between 1TB of storage on EBS, EFS, and S3 Standard.

- ✅ :  "Amazon S3" is the correct answer.

- ❌ :  "Amazon EFS" is incorrect as though this does offer concurrent access from many EC2 Linux instances, it is

  not the most cost-effective solution.

- ❌ :  "Amazon EBS" is incorrect. The Elastic Block Store (EBS) is not a good solution for concurrent access from

  many EC2 instances and is not the most cost-effective option either. EBS volumes are mounted to a single instance

  except when using multi-attach which is a new feature and has several constraints.

- ❌ :  "Amazon EC2 instance store" is incorrect as this is an ephemeral storage solution which means the data is

  lost when powered down. Therefore, this is not an option for long-term data storage.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/optimizing-performance.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #amazon_efs #many_ec2_linux #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #amazon_ec2_instance_store #many_ec2_instances
