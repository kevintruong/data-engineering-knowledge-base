**Explanation:**

Amazon EFS provides high-performance, secure access for thousands of connections to a shared file system using a

traditional file permissions model, file locking, and hierarchical directory structure via the NFSv4 protocol.

It allows you to simultaneously share files between multiple Amazon EC2 instances across multiple AZs, regions, VPCs,

and accounts as well as on-premises servers via AWS Direct Connect or AWS VPN.

This is ideal for your business applications that need to share a common data source. For application workloads with

many instances accessing the same set of files, Amazon EFS provides strong data consistency helping to ensure that any

file read will reflect the last write of the file.

- ✅ :  "Amazon EFS" is the correct answer.

- ❌ :  "AWS Storage Gateway" is incorrect. AWS Storage Gateway supports multiple modes of operation but none of

  them provide a single shared storage location that is accessible from multiple accounts, regions and on-premise

  servers simultaneously.

- ❌ :  "Amazon EBS" is incorrect. Amazon EBS is a block-storage device that is attached to an individual instance

  and cannot be shared between multiple instances. EBS does not support multiple requirements in this scenario.

- ❌ :  "Amazon S3" is incorrect. Amazon S3 does not support a hierarchical structure. Though you can create folders

  within buckets, these are actually just pointers to groups of objects. The structure is flat in Amazon S3. Also, the

  consistency model of Amazon S3 is read-after-write for PUTS of new objects, but only eventual consistency for

  overwrite PUTS and DELETES. This does not support the requirement for strong consistency.

**References:**

<https://aws.amazon.com/efs/features/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #aws_storage_gateway #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/> #amazon_efs #multiple_amazon_ec2 #aws_vpn
