**Explanation:**

General Purpose SSD (gp2) volumes offer cost-effective storage that is ideal for a broad range of workloads. These

volumes deliver single-digit millisecond latencies and the ability to burst to 3,000 IOPS for extended periods of time.

Between a minimum of 100 IOPS (at 33.33 GiB and below) and a maximum of 16,000 IOPS (at 5,334 GiB and above), baseline

performance scales linearly at 3 IOPS per GiB of volume size. AWS designs gp2 volumes to deliver their provisioned

performance 99% of the time. A gp2 volume can range in size from 1 GiB to 16 TiB.

In this case the volume would have a baseline performance of 3 x 200 = 600 IOPS. The volume could also burst to 3,000

IOPS for extended periods. As the I/O varies, this should be suitable.

- ✅ :  "Amazon EBS General Purpose SSD (gp2)" is the correct answer.

- ❌ :  "Amazon EBS Provisioned IOPS SSD (io1) " is incorrect as this would be a more expensive option and is not

  required for the performance characteristics of this workload.

- ❌ :  "Amazon EBS Cold HDD (sc1)" is incorrect as there is no IOPS SLA for HDD volumes and they would likely not

  perform well enough for this workload.

- ❌ :  "Amazon EBS Throughput Optimized HDD (st1)" is incorrect as there is no IOPS SLA for HDD volumes and they

  would likely not perform well enough for this workload.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----

- #amazon_ebs_general_purpose_ssd #amazon_ebs_throughput_optimized_hdd #iops_ssd #<https://docs.aws.amazon.com/awsec2/latest/userguide/ebs-volume-types.html> #general_purpose_ssd
