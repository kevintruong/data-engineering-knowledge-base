### Amazon EFS


**GENERAL**


EFS is a fully-managed service that makes it easy to set up and scale file storage in the Amazon Cloud.


Implementation of an NFS file share and is accessed using the NFSv4.1 protocol.


Elastic storage capacity and pay for what you use (in contrast to EBS with which you pay for what you provision).


Multi-AZ metadata and data storage.


Can configure mount-points in one, or many, AZs.


Can be mounted from on-premises systems ONLY if using Direct Connect or a VPN connection.


Alternatively, use the EFS File Sync agent.


Good for big data and analytics, media processing workflows, content management, web serving, home directories etc.


Pay for what you use (no pre-provisioning required).


Can scale up to petabytes.


EFS is elastic and grows and shrinks as you add and remove data.


Can concurrently connect 1 to 1000s of EC2 instances, from multiple AZs.


A file system can be accessed concurrently from all AZs in the region where it is located.


The following diagram depicts the various options for mounting an EFS filesystem:


By default, you can create up to 10 file systems per account.


Access to EFS file systems from on-premises servers can be enabled via Direct Connect or AWS VPN.


You mount an EFS file system on your on-premises Linux server using the standard Linux mount command for mounting a file

system via the NFSv4.1 protocol.


Can choose General Purpose or Max I/O (both SSD).


The VPC of the connecting instance must have DNS hostnames enabled.


EFS provides a file system interface, file system access semantics (such as strong consistency and file locking).


Data is stored across multiple AZ’s within a region.


Read after write consistency.


Need to create mount targets and choose AZ’s to include (recommended to include all AZ’s).


Instances can be behind an ELB.


EC2 Classic instances must mount via ClassicLink.


EFS is compatible with all Linux-based AMIs for Amazon EC2.


Using the EFS-to-EFS Backup solution, you can schedule automatic incremental backups of your Amazon EFS file system.


The following table provides a comparison of the **storage characteristics of EFS vs EBS** :


**PERFORMANCE**


**There are two performance modes:**


- “General Purpose” performance mode is appropriate for most file systems.

- “Max I/O” performance mode is optimized for applications where tens, hundreds, or thousands of EC2 instances are

  accessing the file system.


Amazon EFS is designed to burst to allow high throughput levels for periods of time.


Amazon EFS file systems are distributed across an unconstrained number of storage servers, enabling file systems to grow

elastically to petabyte scale and allowing massively parallel access from Amazon EC2 instances to your data.


This distributed data storage design means that multithreaded applications and applications that concurrently access

data from multiple Amazon EC2 instances can drive substantial levels of aggregate throughput and IOPS.


The table below compares high-level performance and storage characteristics for AWS’s file (EFS)

and block (EBS) cloud storage offerings:


**ACCESS CONTROL**


When you create a file system, you create endpoints in your VPC called “mount targets”.


When mounting from an EC2 instance, your file system’s DNS name, which you provide in your mount command, resolves to a

mount target’s IP address.


You can control who can administer your file system using IAM.


You can control access to files and directories with POSIX-compliant user and group-level permissions.


POSIX permissions allow you to restrict access from hosts by user and group.


EFS Security Groups act as a firewall, and the rules you add define the traffic flow.


**EFS ENCRYPTION**


EFS offers the ability to encrypt data at rest and in transit.


Encryption keys are managed by the AWS Key Management Service (KMS).


Data encryption in transit uses industry standard Transport Layer Security (TLS) 1.2 to encrypt data sent between your

clients and EFS file systems.


Data encrypted at rest is transparently encrypted while being written, and transparently decrypted while being read.


Enable encryption at rest in the EFS console or by using the AWS CLI or SDKs.


Encryption of data at rest and of data in transit can be configured together or separately to help meet your unique

security requirements.


**EFS FILE SYNC**


EFS File Sync provides a fast and simple way to securely sync existing file systems into Amazon EFS.


EFS File Sync copies files and directories into Amazon EFS at speeds up to 5x faster than standard Linux copy tools,

with simple setup and management in the AWS Console.


EFS File Sync securely and efficiently copies files over the internet or an AWS Direct Connect connection.


Copies file data and file system metadata such as ownership, timestamps, and access permissions.


**EFS File Sync provides the following benefits:**


- Efficient high-performance parallel data transfer that tolerates unreliable and high-latency networks.

- Encryption of data transferred from your IT environment to AWS.

- Data transfer rate up to five times faster than standard Linux copy tools.

- Full and incremental syncs for repetitive transfers.


The following diagram shows a high-level view of the EFS File Sync architecture:


**Note:** EFS File Sync currently doesn’t support syncing from an Amazon EFS source to an NFS destination.


When deploying Amazon EFS File Sync on EC2, the instance size must be at least xlarge for your EFS File Sync to

function.


Recommended to use one of the Memory optimized r4.xlarge instance types.


Can choose to run EFS File Sync either on-premises as a virtual machine (VM), or in AWS as an EC2 instance.


Supports VMware ESXi.


**COMPATIBILITY**


EFS is integrated with a number of other AWS services, including CloudWatch, CloudFormation, CloudTrail, IAM, and

Tagging services.


CloudWatch allows you to monitor file system activity using metrics.


CloudFormation allows you to create and manage file systems using templates.


CloudTrail allows you to record all Amazon EFS API calls in log files.


IAM allows you to control who can administer your file system.


Tagging services allows you to label your file systems with metadata that you define.


**PRICING AND BILLING**


You pay only for the amount of file system storage you use per month.


When using the Provisioned Throughput mode, you pay for the throughput you provision per month.


There is no minimum fee and there are no set-up charges.


With EFS File Sync, you pay per-GB for data copied to EFS.

