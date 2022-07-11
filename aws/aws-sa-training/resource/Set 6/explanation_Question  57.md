*

**Explanation:**

EBS optimized instances provide dedicated capacity for Amazon EBS I/O. EBS optimized instances are designed for use with

all EBS volume types.

Provisioned IOPS EBS volumes allow you to specify the amount of IOPS you require up to 50 IOPS per GB. Within this

limitation you can therefore choose to select the IOPS required to improve the performance of your volume.

RAID can be used to increase IOPS, however RAID 1 does not. For example:

* RAID 0 = 0 striping – data is written across multiple disks and increases performance but no redundancy.

* RAID 1 = 1 mirroring – creates 2 copies of the data but does not increase performance, only redundancy.

HDD, Cold – (SC1) provides the lowest cost storage and low performance

* ✅ :  "Use Provisioned IOPS (I01) EBS volumes" is a correct answer.

* ✅ :  "Use EBS optimized instances" is also a correct answer.

* ❌ :  "Use a larger instance size within the instance family" is incorrect as this may not increase storage

  performance.

* ❌ :  "Use HDD, Cold (SC1) EBS volumes" is incorrect. As this will likely decrease storage performance.

* ❌ :  "Create a RAID 1 array from multiple EBS volumes" is incorrect. As explained above, mirroring does not

  increase performance.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #multiple_ebs_volumes #ebs_volumes #<https://docs.aws.amazon.com/awsec2/latest/userguide/ebs-volume-types.html> #ebs_volume_types #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>
