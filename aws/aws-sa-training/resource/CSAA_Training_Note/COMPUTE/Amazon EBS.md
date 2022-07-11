### Amazon EBS


**GENERAL**


EBS is the Elastic Block Store.


EBS volumes are network attached storage that can be attached to EC2 instances.


EBS volume data persists independently of the life of the instance.


EBS volumes do not need to be attached to an instance.


You can attach multiple EBS volumes to an instance.


You cannot attach an EBS volume to multiple instances (use Elastic File Store instead).


EBS volume data is replicated across multiple servers in an AZ.


EBS volumes must be in the same AZ as the instances they are attached to.


EBS is designed for an annual failure rate of 0.1%-0.2% & an SLA of 99.95%.


Termination protection is turned off by default and must be manually enabled (keeps the volume/data when the instance is

terminated).


Root EBS volumes are deleted on termination by default.


Extra non-boot volumes are not deleted on termination by default.


The behavior can be changed by altering the “DeleteOnTermination” attribute.


You can now create AMIs with encrypted root/boot volumes as well as data volumes (you can also use separate CMKs per

volume).


Volume sizes and types can be upgraded without downtime (except for magnetic standard).


Elastic Volumes allow you to increase volume size, adjust performance, or change the volume type while the volume is in

use.


To migrate volumes between AZ’s create a snapshot then create a volume in another AZ from the snapshot (possible to

change size and type).


Auto-enable IO setting prevents the stopping of IO to a disk when AWS detects inconsistencies.


The root device is created under /dev/sda1 or /dev/xvda.


Magnetic EBS is for workloads that need throughput rather than IOPS.


Throughput optimized EBS volumes cannot be a boot volume.


Each instance that you launch has an associated root device volume, either an Amazon EBS volume or an instance store

volume.


You can use block device mapping to specify additional EBS volumes or instance store volumes to attach to an instance

when it’s launched.


You can also attach additional EBS volumes to a running instance.


You cannot decrease an EBS volume size.


When changing volumes, the new volume must be at least the size of the current volume’s snapshot.


Images can be made public but not if they’re encrypted.


AMIs can be shared with other accounts.


You can have up to 5,000 EBS volumes by default.


You can have up to 10,000 snapshots by default.


**INSTANCE STORE**


An instance store provides _temporary_ (non-persistent) block-level storage for your instance.


This is different to EBS which provides persistent storage but is also a block storage service that can be a root or

additional volume.


Instance store storage is located on disks that are physically attached to the host computer.


Instance store is ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch

data, and other temporary content, or for data that is replicated across a fleet of instances, such as a load-balanced

pool of web servers.


You can specify instance store volumes for an instance only when you launch it.


You can't detach an instance store volume from one instance and attach it to a different instance.


The instance type determines the size of the instance store available and the type of hardware used for the instance

store volumes.


Instance store volumes are included as part of the instance's usage cost.


Some instance types use NVMe or SATA-based solid state drives (SSD) to deliver high random I/O performance.


This is a good option when you need storage with very low latency, but you don't need the data to persist when the

instance terminates, or you can take advantage of fault-tolerant architectures.


**EXAM TIP:** Instance stores offer very high performance and low latency. As long as you can afford to lose an

instance, i.e. you are replicating your data, these can be a good solution for high performance/low latency

requirements. Look out for questions that mention distributed or replicated databases that need high I/O. Also, remember

that the cost of instance stores is included in the instance charges so it can also be more cost-effective than EBS

Provisioned IOPS.


**EBS VS INSTANCE STORE**


EBS-backed means the root volume is an EBS volume and storage is persistent.


Instance store-backed means the root volume is an instance store volume and storage is not persistent.


On an EBS-backed instance, the default action is for the root EBS volume to be deleted upon


termination.


Instance store volumes are sometimes called Ephemeral storage (non-persistent).


Instance store backed instances cannot be stopped. If the underlying host fails, the data will be lost.


Instance store volume root devices are created from AMI templates stored on S3.


EBS backed instances can be stopped. You will not lose the data on this instance if it is stopped

(persistent).


EBS volumes can be detached and reattached to other EC2 instances.


EBS volume root devices are launched from AMI’s that are backed by EBS snapshots.


Instance store volumes cannot be detached/reattached.


When rebooting the instances for both types data will not be lost.


By default, both root volumes will be deleted on termination unless you configured otherwise.


**EBS VOLUME TYPES**


**SSD, General Purpose – GP2**


- Baseline of 3 IOPS per GiB with a minimum of 100 IOPS.

- Burst up to 3000 IOPS (for volumes >= 334GB).

- Up to 16,000 IOPS per volume.

- AWS designs gp2 volumes to deliver 90% of the provisioned performance 99% of the time. A gp2 volume can range in size

  from 1 GiB to 16 TiB.


**SSD, Provisioned IOPS – I01**


- More than 16,000 IOPS.

- Up to 64,000 IOPS per volume.

- Up to 50 IOPS per GiB.

- Amazon EBS delivers the provisioned IOPS performance 99.9 percent of the time.


**HDD, Throughput Optimized – (ST1):**


- Frequently accessed, throughput intensive workloads with large datasets and large I/O sizes, such as MapReduce, Kafka,

  log processing, data warehouse, and ETL workloads.

- Throughput measured in MB/s, and includes the ability to burst up to 250 MB/s per TB, with a baseline throughput of 40

  MB/s per TB and a maximum throughput of 500 MB/s per volume.

- Cannot be a boot volume.


**HDD, Cold – (SC1):**


- Lowest cost storage – cannot be a boot volume.

- Less frequently accessed workloads with large, cold datasets.

- These volumes can burst up to 80 MB/s per TB, with a baseline throughput of 12 MB/s per TB and a maximum throughput of

  250 MB/s per volume.


HDD, Magnetic – Standard – cheap, infrequently accessed storage – lowest cost storage that cannot be a boot volume.


**EBS optimized instances:**


- Dedicated capacity for Amazon EBS I/O.

- EBS-optimized instances are designed for use with all EBS volume types.

- Max bandwidth: 400 Mbps – 12000 Mbps.

- IOPS: 3000 – 65000.

- GP-SSD within 10% of baseline and burst performance 99.9% of the time.

- PIOPS within 10% of baseline and burst performance 99.9% of the time.

- Additional hourly fee.

- Available for select instance types.

- Some instance types have EBS-optimized enabled by default.


**SNAPSHOTS**


Snapshots capture a point-in-time state of an instance.


Cost-effective and easy backup strategy.


Share data sets with other users or accounts.


Can be used to migrate a system to a new AZ or region.


Can be used to convert an unencrypted volume to an encrypted volume.


Snapshots are stored on Amazon S3.


Does not provide granular backup (not a replacement for backup software).


If you make periodic snapshots of a volume, the snapshots are incremental, which means that only the blocks on the

device that have changed after your last snapshot are saved in the new snapshot.


Even though snapshots are saved incrementally, the snapshot deletion process is designed so that you need to retain only

the most recent snapshot in order to restore the volume.


Snapshots can only be accessed through the EC2 APIs.


EBS volumes are AZ specific but snapshots are region specific.


Volumes can be created from EBS snapshots that are the same size or larger.


Snapshots can be taken of non-root EBS volumes while running.


To take consistent snapshots writes must be stopped (paused) until the snapshot is complete – if not possible the volume

needs to be detached, or if it’s an EBS root volume the instance must be stopped.


To lower storage costs on S3 a full snapshot and subsequent incremental updates can be created.


You are charged for data traffic to S3 and storage costs on S3.


You are billed only for the changed blocks.


Deleting a snapshot removes only the data not needed by any other snapshot.


You can resize volumes through restoring snapshots with different sizes (configured when taking the snapshot).


Snapshots can be copied between regions (and be encrypted). Images are then created from the snapshot in the other

region which creates an AMI that can be used to boot an instance.


You can create volumes from snapshots and choose the availability zone within the region.


**ENCRYPTION**


You can encrypt both the boot and data volumes of an EC2 instance. When you create an encrypted EBS volume and attach it

to a supported instance type, the following types of data are encrypted:


- Data at rest inside the volume.

- All data moving between the volume and the instance.

- All snapshots created from the volume.

- All volumes created from those snapshots.


Encryption is supported by all EBS volume types.


Expect the same IOPS performance on encrypted volumes as on unencrypted volumes.


All instance families support encryption.


**Amazon EBS encryption is available on the instance types listed below:**


- General purpose: A1, M3, M4, M5, M5a, M5ad, M5d, T2, T3, and T3a.

- Compute optimized: C3, C4, C5, C5d, and C5n.

- Memory optimized: cr1.8xlarge, R3, R4, R5, R5a, R5ad, R5d, u-6tb1.metal, u-9tb1.metal, u- 12tb1.metal, X1, X1e, and

  z1d.

- Storage optimized: D2, h1.2xlarge, h1.4xlarge, I2, and I3.

- Accelerated computing: F1, G2, G3, G4, P2, and P3.


EBS encrypts your volume with a data key using the industry-standard AES- 256 algorithm.


Your data key is stored on-disk with your encrypted data, but not before EBS encrypts it with your CMK. Your data key

never appears on disk in plaintext..


The same data key is shared by snapshots of the volume and any subsequent volumes created from those snapshots.


Snapshots of encrypted volumes are encrypted automatically.


EBS volumes restored from encrypted snapshots are encrypted automatically.


EBS volumes created from encrypted snapshots are also encrypted.


You can share snapshots, but if they’re encrypted it must be with a custom CMK key.


There is no direct way to change the encryption state of a volume.


Either create an encrypted volume and copy data to it or take a snapshot, encrypt it, and create a new encrypted volume

from the snapshot.


To encrypt a volume or snapshot you need an encryption key, these are customer managed keys

(CMK) and they are managed by the AWS Key Management Service (KMS).


A default CMK key is generated for the first encrypted volumes.


Subsequent encrypted volumes will use their own unique key (AES 256 bit).


The CMK used to encrypt a volume is used by any snapshots and volumes created from snapshots.


You cannot share encrypted volumes created using a default CMK key.


You cannot change the CMK key that is used to encrypt a volume.


You must create a copy of the snapshot and change encryption keys as part of the copy.


This is required in order to be able to share the encrypted volume.


By default, only the account owner can create volumes from snapshots.


You can share unencrypted snapshots with the AWS community by making them public.


You can also share unencrypted snapshots with other AWS accounts by making them private and selecting the accounts to

share them with.


You cannot make encrypted snapshots public.


You can share encrypted snapshots with other AWS accounts using a non-default CMK key and configuring cross-account

permissions to give the account access to the key, mark as private and configure the account to share with.


The receiving account must copy the snapshot before they can then create volumes from the snapshot.


It is recommended that the receiving account re-encrypt the shared and encrypted snapshot using their own CMK key.


**The following information applies to snapshots:**


- Snapshots are created asynchronously and are incremental.

- You can copy unencrypted snapshots (optionally encrypt).

- You can copy an encrypted snapshot (optionally re-encrypt with a different key).

- Snapshot copies receive a new unique ID.

- You can copy within or between regions.


- You cannot move snapshots, only copy them.

- You cannot take a copy of a snapshot when it is in a “pending” state, it must be “complete”.

- S3 Server Side Encryption (SSE) protects data in transit while copying.

- User defined tags are not copied.

- You can have up to 5 snapshot copy requests running in a single destination per account.

- You can copy Import/Export service, AWS Marketplace, and AWS Storage Gateway snapshots.

- If you try to copy an encrypted snapshot without having access to the encryption keys it will fail silently (

  cross-account permissions are required).


**Copying snapshots may be required for:**


- Creating services in other regions.

- DR – the ability to restore from snapshot in another region.

- Migration to another region.

- Applying encryption.

- Data retention.


**To take application-consistent snapshots of RAID arrays:**


- Stop the application from writing to disk.

- Flush all caches to the disk.

- Freeze the filesystem.

- Unmount the RAID array.

- Shut down the associated EC2 instance.


**AMIS**


An Amazon Machine Image (AMI) is a special type of virtual appliance that is used to create a virtual machine within the

Amazon Elastic Compute Cloud (“EC2”).


**An AMI includes the following:**


- A template for the root volume for the instance (for example, an operating system, an application server, and

  applications).

- Launch permissions that control which AWS accounts can use the AMI to launch instances.

- A block device mapping that specifies the volumes to attach to the instance when it’s launched.


AMIs are either instance store-backed or EBS-backed.


**Instance store-backed:**


- Launch an EC2 instance from an AWS instance store-backed AMI.

- Update the root volume as required.

- Create the AMI which will upload to a user-specified S3 bucket (user bucket).

- Register the AMI with EC2 (creates another EC2 controlled S3 image).

- To make changes update the source then deregister and reregister.

- Upon launch the image is copied to the EC2 host.

- Deregister an image when the AMI is not needed anymore (does not affect existing


```

instances created from the AMI).

```


- Instance store-backed volumes can only be created at launch time.


**EBS-backed:**


- Must stop the instance to create a consistent image and then create the AMI.

- AWS registers the AMIs manually.

- During creation AWS creates snapshots of all attached volumes – there is no need to specify a bucket but you will be

  charged for storage on S3.

- You cannot delete the snapshot of the root volume as long as the AMI is registered

  (deregister and delete).

- You can now create AMIs with encrypted root/boot volumes as well as data volumes (can also use separate CMKs per

  volume).


**Copying AMIs:**


- You can copy an Amazon Machine Image (AMI) within or across an AWS region using the AWS Management Console, the AWS

  AWS Command Line Interface or SDKs, or the Amazon EC2 API, all of which support theCopyImage action.

- You can copy both Amazon EBS-backed AMIs and instance store-backed AMIs.

- You can copy encrypted AMIs and AMIs with encrypted snapshots.


**EBS COPYING, SHARING AND ENCRYPTION METHODS**


The following diagram aims to articulate the various possible options for copying EBS volumes, sharing AMIs and

snapshots and applying encryption:


**RAID**


RAID can be used to increase IOPS.


RAID 0 = 0 striping – data is written across multiple disks and increases performance but no redundancy.


RAID 1 = 1 mirroring – creates 2 copies of the data but does not increase performance, only redundancy.


RAID 10 = 10 combination of RAID 1 and 2 resulting in increase performance and redundancy (at the cost of additional

disks).


You can configure multiple striped gp2 or standard volumes (typically RAID 0).


You can configure multiple striped PIOPS volumes (typically RAID 0).


RAID is configured through the guest OS.


EBS optimized EC2 instances are another way of increasing performance.


Ensure the EC2 instance can handle the bandwidth required for the increased performance.


Use EBS optimized instances or instances with a 10 Gbps network interface.


Not recommended to use RAID for root/boot volumes.


**EBS LIMITS (PER REGION)**

