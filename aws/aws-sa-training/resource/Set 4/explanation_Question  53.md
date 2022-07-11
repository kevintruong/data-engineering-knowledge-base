*

**Explanation:**

SSD, General Purpose (GP2) provides enough IOPS to support this requirement and is the most economical option that does.

Using Provisioned IOPS would be more expensive and the other two options do not provide an SLA for IOPS.

More information on the volume types:

* SSD, General Purpose (GP2) provides 3 IOPS per GB up to 16,000 IOPS. Volume size is 1 GB to 16 TB.

* Provisioned IOPS (Io1) provides the IOPS you assign up to 50 IOPS per GiB and up to 64,000 IOPS per volume. Volume

  size is 4 GB to 16TB.

* Throughput Optimized HDD (ST1) provides up to 500 IOPS per volume but does not provide an SLA for IOPS.

* Cold HDD (SC1) provides up to 250 IOPS per volume but does not provide an SLA for IOPS.

* ✅ :  "General Purpose (GP2)" is the correct answer.

* ❌ :  "Throughput Optimized HDD (ST1)" is incorrect as this will not provide an SLA for IOPS.

* ❌ :  "Provisioned IOPS (Io1)" is incorrect as this will be less cost-effective.

* ❌ :  "Cold HDD (SC1)" is incorrect as this will not provide an SLA for IOPS.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html?icmpid=docs_ec2_console>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #throughput_optimized_hdd #ssd #iops #sla #enough_iops
