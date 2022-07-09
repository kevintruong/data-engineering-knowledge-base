#### Question  60


**An AWS workload in a VPC is running a legacy database on an Amazon EC2 instance. Data is stored on a 2000GB Amazon

EBS (gp2) volume. At peak load times, logs show excessive wait time.**


**What should be implemented to improve database performance using persistent storage?**


1: Change the EC2 instance type to one with burstable performance


2: Change the EC2 instance type to one with EC2 instance store volumes


3: Migrate the data on the Amazon EBS volume to an SSD-backed volume


4: Migrate the data on the EBS volume to provisioned IOPS SSD (io1)


Answer: 4


**Explanation:**


The data is already on an SSD-backed volume (gp2), therefore to improve performance the best option is to migrate the

data onto a provisioned IOPS SSD (io1) volume type which will provide improved I/O performance and therefore reduce wait

times.


- CORRECT "Migrate the data on the EBS volume to provisioned IOPS SSD (io1)" is the correct answer.


- INCORRECT "Change the EC2 instance type to one with burstable performance" is incorrect. Burstable performance

  instances provide a baseline of CPU performance with the ability to burst to a higher level when required. However,

  the issue in this scenario is disk wait time, not CPU performance, therefore we need to improve I/O not CPU

  performance.


- INCORRECT "Change the EC2 instance type to one with EC2 instance store volumes" is incorrect. Using an instance store

  volume may provide high performance but the data is not persistent so it is not suitable for a database.


- INCORRECT "Migrate the data on the Amazon EBS volume to an SSD-backed volume" is incorrect as the data is already on

  an SSD-backed volume (gp2).


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

