**Explanation:**

For block storage the Solutions Architect should use either Amazon EBS or EC2 instance store. However, the instance

store is non-persistent so EBS must be used. With EBS you can encrypt your volume and automate volume-level backups

using snapshots that are run by Data Lifecycle Manager.

- ✅ :  "Use an encrypted Amazon EBS volume and use Data Lifecycle Manager to automate snapshots" is the correct

  answer.

- ❌ :  "Use an encrypted Amazon EFS filesystem and use an Amazon CloudWatch Events rule to start a backup copy of

  data using AWS Lambda" is incorrect. EFS is not block storage, it is a file-level storage service.

- ❌ :  "Use server-side encryption on an Amazon S3 bucket and use Cross-Region-Replication to backup on a schedule"

  is incorrect. Amazon S3 is an object-based storage system not a block-based storage system.

- ❌ :  "Use an encrypted Amazon EC2 instance store and copy the data to another EC2 instance using a cron job and a

  batch script " is incorrect as the EC2 instance store is a non-persistent volume.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----

- #amazon_efs_filesystem #<https://docs.aws.amazon.com/awsec2/latest/userguide/ebs-volumes.html> #aws_lambda #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/> #ec2_instance_store
