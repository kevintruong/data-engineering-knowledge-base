*

**Explanation:**

EFS is a fully-managed service that makes it easy to set up and scale file storage in the Amazon Cloud. EFS file systems

are mounted using the NFSv4.1 protocol. EFS is designed to burst to allow high throughput levels for periods of time.

EFS also offers the ability to encrypt data at rest and in transit.

* ✅ :  "Use the Elastic File System (EFS) and mount the file system using NFS" is the correct answer.

* ❌ :  "Add EBS volumes to each EC2 instance and configure data replication" is incorrect. Adding EBS volumes to

  each instance and configuring data replication is not the best solution for this scenario and there is no native

  capability within AWS for performing the replication. Some 3rd party data management software does use this model,

  however.

* ❌ :  "Use the Elastic Block Store (EBS) and mount the file system at the block level" is incorrect. EBS is a

  block-level storage system not a file-level storage system. You cannot mount EBS volumes from multiple instances

  across AZs.

* ❌ :  "Add EBS volumes to each EC2 instance and use an ELB to distribute data evenly between the volumes" is

  incorrect. You cannot use an ELB to distribute data between EBS volumes.

**References:**

<https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----
* #elastic_file_system #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/> #efs_file_systems #ebs_volumes #amazon_cloud
