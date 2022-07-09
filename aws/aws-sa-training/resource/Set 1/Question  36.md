#### Question  36


**A company is deploying a big data and analytics workload. The analytics will be run from a fleet of thousands of EC2

instances across multiple AZs. Data needs to be stored on a shared storage layer that can be mounted and accessed

concurrently by all EC2 instances. Latency is not a concern however extremely high throughput is required.**


**What storage layer would be most suitable for this requirement?**


1: Amazon EFS in General Purpose mode


2: Amazon EFS in Max I/O mode


3: Amazon EBS PIOPS


4: Amazon S3


Answer: 2


**Explanation:**


Amazon EFS file systems in the Max I/O mode can scale to higher levels of aggregate throughput and operations per second

with a tradeoff of slightly higher latencies for file operations. You can also mount EFS filesystems to up to thousands

of EC2 instances across multiple AZs.


- CORRECT "Amazon EFS in Max I/O mode" is the correct answer.


- INCORRECT "Amazon EFS in General Purpose mode" is incorrect as Max I/O mode should be used for these requirements.


- INCORRECT "Amazon EBS PIOPS" is incorrect. Amazon EBS volumes cannot be shared between instances across AZs.


- INCORRECT "Amazon S3" is incorrect. Amazon S3 is not a storage layer that can be mounted and accessed concurrently.


**References:**


https://docs.aws.amazon.com/efs/latest/ug/performance.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/

