**Explanation:**

Amazon EFS file systems in the Max I/O mode can scale to higher levels of aggregate throughput and operations per second

with a tradeoff of slightly higher latencies for file operations. You can also mount EFS filesystems to up to thousands

of EC2 instances across multiple AZs.

- ✅ :  "Amazon EFS in Max I/O mode" is the correct answer.

- ❌ :  "Amazon EFS in General Purpose mode" is incorrect as Max I/O mode should be used for these requirements.

- ❌ :  "Amazon EBS PIOPS" is incorrect. Amazon EBS volumes cannot be shared between instances across AZs.

- ❌ :  "Amazon S3" is incorrect. Amazon S3 is not a storage layer that can be mounted and accessed concurrently.

**References:**

<https://docs.aws.amazon.com/efs/latest/ug/performance.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #amazon_efs_file_systems #<https://docs.aws.amazon.com/efs/latest/ug/performance.html> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/> #amazon_efs #amazon_ebs_volumes
