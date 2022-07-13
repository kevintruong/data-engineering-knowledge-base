**Explanation:**

Instance stores offer very high performance and low latency. As long as you can afford to lose an instance, i.e. you are

replicating your data, these can be a good solution for high performance/low latency requirements.

Also, the cost of instance stores is included in the instance charges so it can also be more cost-effective than EBS

Provisioned IOPS.

- ✅ :  "Use Amazon Instance Store" is the correct answer.

- ❌ :  "Use Amazon EBS Provisioned IOPS volume with 135,000 IOPS" is incorrect. In the case of a HPC cluster that

  replicates data between nodes you don’t necessarily need a shared storage solution such as Amazon EBS Provisioned IOPS

  – this would also be a more expensive solution as the Instance Store is included in the cost of the HPC instance.

- ❌ :  "Use Amazon S3 with byte-range fetch" is incorrect. Amazon S3 is not a solution for this HPC application as

  in this case it will require block-based storage to provide the required IOPS.

- ❌ :  "Enhanced networking provides higher bandwidth and lower latency and is implemented using an Elastic Network

  Adapter (ENA). However, using an ENA with an HDD Throughput Optimized volume is not recommended and the volume will

  not provide the performance required for this use case." is incorrect

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----

- #amazon_instance_store #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/> #hpc_cluster #amazon_ebs #instance_store
