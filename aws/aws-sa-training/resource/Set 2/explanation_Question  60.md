**Explanation:**

The data is already on an SSD-backed volume (gp2), therefore to improve performance the best option is to migrate the

data onto a provisioned IOPS SSD (io1) volume type which will provide improved I/O performance and therefore reduce wait

times.

- ✅ :  "Migrate the data on the EBS volume to provisioned IOPS SSD (io1)" is the correct answer.

- ❌ :  "Change the EC2 instance type to one with burstable performance" is incorrect. Burstable performance

  instances provide a baseline of CPU performance with the ability to burst to a higher level when required. However,

  the issue in this scenario is disk wait time, not CPU performance, therefore we need to improve I/O not CPU

  performance.

- ❌ :  "Change the EC2 instance type to one with EC2 instance store volumes" is incorrect. Using an instance store

  volume may provide high performance but the data is not persistent so it is not suitable for a database.

- ❌ :  "Migrate the data on the Amazon EBS volume to an SSD-backed volume" is incorrect as the data is already on

  an SSD-backed volume (gp2).

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----

- #<https://docs.aws.amazon.com/awsec2/latest/userguide/burstable-performance-instances.html> #ec2_instance_store_volumes #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/> #iops_ssd #burstable_performance
