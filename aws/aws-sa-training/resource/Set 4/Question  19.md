#### Question  19


**The disk configuration for an Amazon EC2 instance must be finalized. The instance will be running an application that

requires heavy read/write IOPS. A single volume is required that is 500 GiB in size and needs to support 20,000 IOPS.**


**What EBS volume type should be selected?**


1: EBS General Purpose SSD


2: EBS Provisioned IOPS SSD


3: EBS General Purpose SSD in a RAID 1 configuration


4: EBS Throughput Optimized HDD


**Answer: 2**


**Explanation:**


This is simply about understanding the performance characteristics of the different EBS volume types. The only EBS

volume type that supports over 16,000 IOPS per volume is Provisioned IOPS SSD.


**SSD, General Purpose – gp2**


- Volume size 1 GiB – 16 TiB.

- Max IOPS/volume 16,000.


**SSD, Provisioned IOPS – i01**


- Volume size 4 GiB – 16 TiB.

- Max IOPS/volume 64,000.

- **HDD, Throughput Optimized – (st1)**

- Volume size 500 GiB – 16 TiB.


Throughput measured in MB/s, and includes the ability to burst up to 250 MB/s per TB, with a baseline throughput of 40

MB/s per TB and a maximum throughput of 500 MB/s per volume.


**HDD, Cold – (sc1)**


- Volume size 500 GiB – 16 TiB.


Lowest cost storage – cannot be a boot volume.


- These volumes can burst up to 80 MB/s per TB, with a baseline throughput of 12 MB/s per TB and a maximum throughput of

  250 MB/s per volume


HDD, Magnetic – Standard – cheap, infrequently accessed storage – lowest cost storage that can be a boot volume.


- CORRECT "EBS Provisioned IOPS SSD" is the correct answer.


- INCORRECT "EBS General Purpose SSD" is incorrect as the max IOPS is 16,000.


- INCORRECT "EBS General Purpose SSD in a RAID 1 configuration" is incorrect. RAID 1 is mirroring and does not increase

  the amount of IOPS you can generate.


- INCORRECT "EBS Throughput Optimized HDD" is incorrect as this type of disk does not support the IOPS requirement.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

