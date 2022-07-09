#### Question  57


**The load on a MySQL database running on Amazon EC2 is increasing and performance has been impacted. Which of the

options below would help to increase storage performance? (Select TWO)**


1: Use a larger instance size within the instance family


2: Use HDD, Cold (SC1) EBS volumes


3: Use Provisioned IOPS (I01) EBS volumes


4: Use EBS optimized instances


5: Create a RAID 1 array from multiple EBS volumes


**Answer: 3,4**


**Explanation:**


EBS optimized instances provide dedicated capacity for Amazon EBS I/O. EBS optimized instances are designed for use with

all EBS volume types.


Provisioned IOPS EBS volumes allow you to specify the amount of IOPS you require up to 50 IOPS per GB. Within this

limitation you can therefore choose to select the IOPS required to improve the performance of your volume.


RAID can be used to increase IOPS, however RAID 1 does not. For example:


- RAID 0 = 0 striping – data is written across multiple disks and increases performance but no redundancy.

- RAID 1 = 1 mirroring – creates 2 copies of the data but does not increase performance, only redundancy.


HDD, Cold – (SC1) provides the lowest cost storage and low performance


- CORRECT "Use Provisioned IOPS (I01) EBS volumes" is a correct answer.


- CORRECT "Use EBS optimized instances" is also a correct answer.


- INCORRECT "Use a larger instance size within the instance family" is incorrect as this may not increase storage

  performance.


- INCORRECT "Use HDD, Cold (SC1) EBS volumes" is incorrect. As this will likely decrease storage performance.


- INCORRECT "Create a RAID 1 array from multiple EBS volumes" is incorrect. As explained above, mirroring does not

  increase performance.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

