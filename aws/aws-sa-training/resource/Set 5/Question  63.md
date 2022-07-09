#### Question  63


**A Solutions Architect needs to create a file system that can be concurrently accessed by multiple Amazon EC2 instances

across multiple availability zones. The file system needs to support high throughput and the ability to burst. As the

data that will be stored on the file system will be sensitive, it must be encrypted at rest and in transit.**


**Which storage solution should the Solutions Architect use for the shared file system?**


1: Add EBS volumes to each EC2 instance and configure data replication


2: Use the Elastic Block Store (EBS) and mount the file system at the block level


3: Use the Elastic File System (EFS) and mount the file system using NFS


4: Add EBS volumes to each EC2 instance and use an ELB to distribute data evenly between the volumes


**Answer: 3**


**Explanation:**


EFS is a fully-managed service that makes it easy to set up and scale file storage in the Amazon Cloud. EFS file systems

are mounted using the NFSv4.1 protocol. EFS is designed to burst to allow high throughput levels for periods of time.

EFS also offers the ability to encrypt data at rest and in transit.


- CORRECT "Use the Elastic File System (EFS) and mount the file system using NFS" is the correct answer.


- INCORRECT "Add EBS volumes to each EC2 instance and configure data replication" is incorrect. Adding EBS volumes to

  each instance and configuring data replication is not the best solution for this scenario and there is no native

  capability within AWS for performing the replication. Some 3rd party data management software does use this model,

  however.


- INCORRECT "Use the Elastic Block Store (EBS) and mount the file system at the block level" is incorrect. EBS is a

  block-level storage system not a file-level storage system. You cannot mount EBS volumes from multiple instances

  across AZs.


- INCORRECT "Add EBS volumes to each EC2 instance and use an ELB to distribute data evenly between the volumes" is

  incorrect. You cannot use an ELB to distribute data between EBS volumes.


**References:**


https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

