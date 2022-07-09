#### Question  8


**A new application will be launched on an Amazon EC2 instance with an Elastic Block Store (EBS) volume. A solutions

architect needs to determine the most cost-effective storage option. The application will have infrequent usage, with

peaks of traffic for a couple of hours in the morning and evening. Disk I/O is variable with peaks of up to 3,000

IOPS.**


**Which solution should the solutions architect recommend?**


1: Amazon EBS Cold HDD (sc1)


2: Amazon EBS General Purpose SSD (gp2)


3: Amazon EBS Provisioned IOPS SSD (io1)


4: Amazon EBS Throughput Optimized HDD (st1)


```

Users in US Amazon Route 53

```


```

Resolve dctlabs.com

```


```

Answer:

51. 45. 2. 12

53. 58. 31. 89

```


```

dctlabs.comin

us-east- 1

```


```

Edge location

```


```

dctlabs.comin

eu-central- 1

```


```

Addresses:

51. 45. 2. 12

53. 58. 31. 89

```


```

Uses the AWS

global network

```


```

Static anycast IP

addresses

```


Answer: 2


**Explanation:**


General Purpose SSD (gp2) volumes offer cost-effective storage that is ideal for a broad range of workloads. These

volumes deliver single-digit millisecond latencies and the ability to burst to 3,000 IOPS for extended periods of time.


Between a minimum of 100 IOPS (at 33.33 GiB and below) and a maximum of 16,000 IOPS (at 5,334 GiB and above), baseline

performance scales linearly at 3 IOPS per GiB of volume size. AWS designs gp2 volumes to deliver their provisioned

performance 99% of the time. A gp2 volume can range in size from 1 GiB to 16 TiB.


In this case the volume would have a baseline performance of 3 x 200 = 600 IOPS. The volume could also burst to 3,000

IOPS for extended periods. As the I/O varies, this should be suitable.


- CORRECT "Amazon EBS General Purpose SSD (gp2)" is the correct answer.


- INCORRECT "Amazon EBS Provisioned IOPS SSD (io1) " is incorrect as this would be a more expensive option and is not

  required for the performance characteristics of this workload.


- INCORRECT "Amazon EBS Cold HDD (sc1)" is incorrect as there is no IOPS SLA for HDD volumes and they would likely not

  perform well enough for this workload.


- INCORRECT "Amazon EBS Throughput Optimized HDD (st1)" is incorrect as there is no IOPS SLA for HDD volumes and they

  would likely not perform well enough for this workload.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

