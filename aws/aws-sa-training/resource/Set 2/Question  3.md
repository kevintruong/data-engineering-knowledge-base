#### Question  3


**A solutions architect is finalizing the architecture for a distributed database that will run across multiple Amazon

EC2 instances. Data will be replicated across all instances so the loss of an instance will not cause loss of data. The

database requires block storage with low latency and throughput that supports up to several million transactions per

second per server.**


**Which storage solution should the solutions architect use?**


1: Amazon EBS


2: Amazon EC2 instance store


3: Amazon EFS


4: Amazon S3


Answer: 2


**Explanation:**


An _instance store_ provides temporary block-level storage for your instance. This storage is located on disks that are

physically attached to the host computer. Instance store is ideal for temporary storage of information that changes

frequently, such as buffers, caches, scratch data, and other temporary content, or for data that is replicated across a

fleet of instances, such as a load-balanced pool of web servers.


Some instance types use NVMe or SATA-based solid state drives (SSD) to deliver high random I/O performance. This is a

good option when you need storage with very low latency, but you don't need the data to persist when the instance

terminates or you can take advantage of fault-tolerant architectures.


In this scenario the data is replicated and fault tolerant so the best option to provide the level of performance

required is to use instance store volumes.


- CORRECT "Amazon EC2 instance store" is the correct answer.


- INCORRECT "Amazon EBS " is incorrect. The Elastic Block Store (EBS) is a block storage device but as the data is

  distributed and fault tolerant a better option for performance would be to use instance stores.


- INCORRECT "Amazon EFS " is incorrect as EFS is not a block device, it is a filesystem that is accessed using the NFS

  protocol.


- INCORRECT "Amazon S3" is incorrect as S3 is an object-based storage system, not a block-based storage system.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

