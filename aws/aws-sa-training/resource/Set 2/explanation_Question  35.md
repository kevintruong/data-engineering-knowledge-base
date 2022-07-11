**Explanation:**

Amazon EFS is a fully managed service that requires no changes to your existing applications and tools, providing access

through a standard file system interface for seamless integration. It is built to scale on demand to petabytes without

disrupting applications, growing and shrinking automatically as you add and remove files. This is an easy solution to

implement and the option that requires the least management and configuration.

An instance store provides temporary block-level storage for an EC2 instance. If you terminate the instance you lose all

data. The alternative is to use Elastic Block Store volumes which are also block-level storage devices but the data is

persistent. However, EBS is not a fully managed solution and doesn’t grow automatically as your data requirements

increase – you would need to increase the volume size and then extend your filesystem.

- ✅ :  "Amazon EFS" is the correct answer.

- ❌ :  "Amazon S3" is incorrect. Amazon S3 is an object storage solution and as the data is currently sitting on a

  block storage you would need to develop some way to use the REST API to upload/manage data on S3 – this is not the

  easiest solution to implement.

- ❌ :  "Amazon EBS" is incorrect as EBS is not a fully managed solution and doesn’t grow automatically as your data

  requirements increase – you would need to increase the volume size and then extend your filesystem.

- ❌ :  "Amazon RDS" is incorrect. Amazon RDS is a relational database service, the question is not looking for a

  database, just a way of storing data.

**References:**

<https://aws.amazon.com/efs/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/> #amazon_efs #elastic_block_store_volumes #amazon_ebs #ec2_instance
