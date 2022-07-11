### Amazon fsx


Amazon FSx provides fully managed third-party file systems.


Amazon FSx provides you with the native compatibility of third-party file systems with feature sets for workloads such

as Windows-based storage, high-performance computing (HPC), machine learning, and electronic design automation (EDA).


You don’t have to worry about managing file servers and storage, as Amazon FSx automates the time-consuming

administration tasks such as hardware provisioning, software configuration, patching, and backups.


Amazon FSx integrates the file systems with cloud-native AWS services, making them even more useful for a broader set of

workloads.


**Amazon FSx provides you with two file systems to choose from:**


- Amazon FSx for Windows File Server for Windows-based applications

- Amazon FSx for Lustre for compute-intensive workloads.


**AMAZON FSX FOR WINDOWS FILE SERVER**


Amazon FSx for Windows File Server provides a fully managed native Microsoft Windows file system so you can easily move

your Windows-based applications that require shared file storage to AWS.


Built on Windows Server, Amazon FSx provides the compatibility and features that your Microsoft applications rely on,

including full support for the SMB protocol, Windows NTFS, and Microsoft


Active Directory (AD) integration.


Amazon FSx uses SSD storage to provide fast performance with low latency.


This compatibility, performance, and scalability enables business-critical workloads such as home directories, media

workflows, and business applications.


Amazon FSx helps you optimize TCO with Data Deduplication, reducing costs by 50 - 60% for general- purpose file shares.


User quotas give you the option to better monitor and control costs. You pay for only the resources used, with no

upfront costs, or licensing fees.


**Details and Benefits**


**High availability:** Amazon FSx automatically replicates your data within an Availability Zone (AZ) it resides in (

which you specify during creation) to protect it from component failure, continuously monitors for hardware failures,

and automatically replaces infrastructure components in the event of a failure.


**Multi-AZ:** Amazon FSx offers a multiple availability (AZ) deployment option, designed to provide continuous

availability to data, even in the event that an AZ is unavailable. Multi-AZ file systems include an active and standby

file server in separate AZs, and any changes written to disk in your file system are synchronously replicated across AZs

to the standby.


**Supports Windows-native file system features:**


- Access Control Lists (ACLs), shadow copies, and user quotas.

- NTFS file systems that can be accessed from up to thousands of compute instances using the SMB protocol.


Works with Microsoft Active Directory (AD) to easily integrate file systems with Windows environments.


Built on SSD-storage, Amazon FSx provides fast performance with up to 2 GB/second throughput per file system, hundreds

of thousands of IOPS, and consistent sub-millisecond latencies.


Can choose a throughput level that is independent of your file system size.


Using DFS Namespaces, you can scale performance up to tens of gigabytes per second of throughput, with millions of IOPS,

across hundreds of petabytes of data.


Amazon FSx can connect file systems to Amazon EC2, VMware Cloud on AWS, Amazon WorkSpaces, and Amazon AppStream 2.0

instances.


Amazon FSx also supports on-premises access via AWS Direct Connect or AWS VPN, and access from multiple VPCs, accounts,

and regions using VPC Peering or AWS Transit Gateway.


Amazon FSx automatically encrypts your data at-rest and in-transit.


Assessed to comply with ISO, PCI-DSS, and SOC certifications, and is HIPAA eligible.


Integration with AWS CloudTrail monitors and logs your API calls letting you see actions taken by users on Amazon FSx

resources.


Pay only for the resources you use, with no minimum commitments or up-front fees.


Can optimize costs by removing redundant data with Data Deduplication.


User quotas provide tracking, monitoring, and enforcing of storage consumption to help reduce costs.


**AMAZON FSX FOR LUSTRE**


Amazon FSx for Lustre provides a high-performance file system optimized for fast processing of workloads such as machine

learning, high performance computing (HPC), video processing, financial modeling, and electronic design automation (EDA)

.


These workloads commonly require data to be presented via a fast and scalable file system interface, and typically have

data sets stored on long-term data stores like Amazon S3.


Amazon FSx for Lustre provides a fully managed high-performance Lustre file system that allows file-based applications

to access data with hundreds of gigabytes per second of data, millions of IOPS, and sub millisecond latencies.


Amazon FSx works natively with Amazon S3, letting you transparently access your S3 objects as files on Amazon FSx to run

analyses for hours to months.


You can then write results back to S3, and simply delete your file system. FSx for Lustre also enables you to burst your

data processing workloads from on-premises to AWS, by allowing you to access your FSx file system over Amazon Direct

Connect or VPN.


You can also use FSx for Lustre as a standalone high-performance file system to burst your workloads from on-premises to

the cloud.


By copying on-premises data to an FSx for Lustre file system, you can make that data available for fast processing by

compute instances running on AWS.


With Amazon FSx, you pay for only the resources you use. There are no minimum commitments, upfront hardware or software

costs, or additional fees.


**Details and Benefits**


Lustre is a popular open-source parallel file system that is designed for high-performance workloads. These workloads

include HPC, machine learning, analytics, and media processing.


A parallel file system provides high throughput for processing large amounts of data and performs operations with

consistently low latencies.


It does so by storing data across multiple networked servers that thousands of compute instances can interact with

concurrently.


The Lustre file system provides a POSIX-compliant file system interface.


Amazon FSx can scale up to hundreds of gigabytes per second of throughput, and millions of IOPS.


Amazon FSx provides high throughput for processing large amounts of data and performs operations with consistent,

sub-millisecond latencies.


Amazon FSx for Lustre supports file access to thousands of EC2 instances, enabling you to provide


file storage for your high-performance workloads, like genomics, seismic exploration, and video rendering.


**Amazon S3:**


- Amazon FSx works natively with Amazon S3, making it easy to access your S3 data to run data processing workloads.

- Your S3 objects are presented as files in your file system, and you can write your results back to S3.

- This lets you run data processing workloads on FSx for Lustre and store your long-term data on S3 or on-premises data

  stores.


**On-premises:**


- You can use Amazon FSx for Lustre for on-premises workloads that need to burst to the cloud due to peak demands or

  capacity limits.

- To move your existing on-premises data into Amazon FSx, you can mount your Amazon FSx for Lustre file system from an

  on-premises client over AWS Direct Connect or VPN, and then use parallel copy tools to import your data to your Amazon

  FSx for Lustre file system.

- At any time, you can write your results back to be durably stored in your data lake.


**Security:**


- All Amazon FSx file system data is encrypted at rest.

- You can access your file system from your compute instances using the open-source Lustre client.

- Once mounted, you can work with the files and directories in your file system just like you would with a local file

  system.

- FSx for Lustre is compatible with the most popular Linux-based AMIs, including Amazon Linux, Red Hat Enterprise

  Linux (RHEL), CentOS, Ubuntu, and SUSE Linux.

- You access your Amazon FSx file system from endpoints in your Amazon VPC, which enables you to isolate your file

  system in your own virtual network.

- You can configure security group rules and control network access to your Amazon FSx file systems.

- Amazon FSx is integrated with AWS Identity and Access Management (IAM).

- This integration means that you can control the actions your AWS IAM users and groups can take to manage your file

  systems (such as creating and deleting file systems).

- You can also tag your Amazon FSx resources and control the actions that your IAM users and groups can take based on

  those tags.

