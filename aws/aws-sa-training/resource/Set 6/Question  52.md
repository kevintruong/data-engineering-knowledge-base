#### Question  52


**A Solutions Architect is designing the disk configuration for an Amazon EC2 instance. The instance needs to support a

MapReduce process that requires high throughput for a large dataset with large I/O sizes.**


**Which Amazon EBS volume is the MOST cost-effective solution for these requirements?**


1: EBS General Purpose SSD in a RAID 1 configuration


2: EBS Throughput Optimized HDD


3: EBS Provisioned IOPS SSD


4: EBS General Purpose SSD


**Answer: 2**


**Explanation:**


EBS Throughput Optimized HDD is good for the following use cases (and is the most cost-effective option:


- Frequently accessed, throughput intensive workloads with large datasets and large I/O sizes, such as MapReduce, Kafka,

  log processing, data warehouse, and ETL workloads


Throughput is measured in MB/s, and includes the ability to burst up to 250 MB/s per TB, with a baseline throughput of

40 MB/s per TB and a maximum throughput of 500 MB/s per volume.


- CORRECT "EBS Throughput Optimized HDD" is the correct answer.


- INCORRECT "EBS General Purpose SSD in a RAID 1 configuration" is incorrect. This is not the best solution for the

  requirements or the most cost-effective.


- INCORRECT "EBS Provisioned IOPS SSD" is incorrect. SSD disks are more expensive.


- INCORRECT "EBS General Purpose SSD" is incorrect. SSD disks are more expensive.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

