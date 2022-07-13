*

**Explanation:**

This is simply about understanding the performance characteristics of the different EBS volume types. The only EBS

volume type that supports over 16,000 IOPS per volume is Provisioned IOPS SSD.

**SSD, General Purpose – gp2**

* Volume size 1 GiB – 16 TiB.

* Max IOPS/volume 16,000.

**SSD, Provisioned IOPS – i01**

* Volume size 4 GiB – 16 TiB.

* Max IOPS/volume 64,000.

* **HDD, Throughput Optimized – (st1)**

* Volume size 500 GiB – 16 TiB.

Throughput measured in MB/s, and includes the ability to burst up to 250 MB/s per TB, with a baseline throughput of 40

MB/s per TB and a maximum throughput of 500 MB/s per volume.

**HDD, Cold – (sc1)**

* Volume size 500 GiB – 16 TiB.

Lowest cost storage – cannot be a boot volume.

* These volumes can burst up to 80 MB/s per TB, with a baseline throughput of 12 MB/s per TB and a maximum throughput of

  250 MB/s per volume

HDD, Magnetic – Standard – cheap, infrequently accessed storage – lowest cost storage that can be a boot volume.

* ✅ :  "EBS Provisioned IOPS SSD" is the correct answer.

* ❌ :  "EBS General Purpose SSD" is incorrect as the max IOPS is 16,000.

* ❌ :  "EBS General Purpose SSD in a RAID 1 configuration" is incorrect. RAID 1 is mirroring and does not increase

  the amount of IOPS you can generate.

* ❌ :  "EBS Throughput Optimized HDD" is incorrect as this type of disk does not support the IOPS requirement.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #ebs_throughput_optimized_hdd #ebs_general_purpose_ssd #iops_ssd #different_ebs_volume_types #<https://docs.aws.amazon.com/awsec2/latest/userguide/ebs-volume-types.html>
