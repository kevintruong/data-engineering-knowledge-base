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

- ✅ :  "Amazon EC2 instance store" is the correct answer.

- ❌ :  "Amazon EBS " is incorrect. The Elastic Block Store (EBS) is a block storage device but as the data is

  distributed and fault tolerant a better option for performance would be to use instance stores.

- ❌ :  "Amazon EFS " is incorrect as EFS is not a block device, it is a filesystem that is accessed using the NFS

  protocol.

- ❌ :  "Amazon S3" is incorrect as S3 is an object-based storage system, not a block-based storage system.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----

- #amazon_ec2_instance_store #instance_store #instance_stores #instance_store_volumes #**instance_store**
