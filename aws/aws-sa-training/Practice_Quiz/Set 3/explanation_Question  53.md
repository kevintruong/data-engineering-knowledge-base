**Explanation:**

Amazon EFS provides file storage in the AWS Cloud. With Amazon EFS, you can create a file system, mount the file system

on an Amazon EC2 instance, and then read and write data to and from your file system.

You can mount an Amazon EFS file system in your VPC, through the Network File System versions 4.0 and 4.1

(NFSv4) protocol. We recommend using a current generation Linux NFSv4.1 client, such as those found in the latest Amazon

Linux, Redhat, and Ubuntu AMIs, in conjunction with the Amazon EFS Mount Helper.

- ✅ :  "Amazon EFS" is the correct answer.

- ❌ :  "Amazon S3" is incorrect. Amazon S3 is an object storage system that is accessed via REST API not file-level

  protocols. It cannot be attached to EC2 instances.

- ❌ :  "Amazon EC2 instance store" is incorrect. An EC2 instance store is an ephemeral storage volume that is local

  to the server on which the instances runs and is not persistent. It is accessed via block protocols and also cannot be

  shared between instances.

- ❌ :  "Amazon EBS" is incorrect. An Amazon Elastic Block Store (EBS) volume can only be attached to a single

  instance and cannot be shared.

**References:**

<https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #amazon_efs_file_system #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/> #amazon_efs #aws_cloud #amazon_ec2_instance_store
