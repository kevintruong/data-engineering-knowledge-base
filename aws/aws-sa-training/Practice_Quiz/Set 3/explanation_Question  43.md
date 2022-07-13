**Explanation:**

When you launch a new EC2 instance, the EC2 service attempts to place the instance in such a way that all of your

instances are spread out across underlying hardware to minimize correlated failures. You can use _placement groups_ to

influence the placement of a group of _interdependent_ instances to meet the needs of your workload. Depending on the

type of workload, you can create a placement group using one of the following placement strategies:

- _Cluster_ – packs instances close together inside an Availability Zone. This strategy enables workloads to achieve the

  low-latency network performance necessary for tightly-coupled node-to-node communication that is typical of HPC

  applications.

- _Partition_ – spreads your instances across logical partitions such that groups of instances in one partition do not

  share the underlying hardware with groups of instances in different partitions. This strategy is typically used by

  large distributed and replicated workloads, such as Hadoop, Cassandra, and Kafka.

- _Spread_ – strictly places a small group of instances across distinct underlying hardware to reduce correlated

  failures.

Cluster placement groups are recommended for applications that benefit from low network latency, high network

throughput, or both. They are also recommended when the majority of the network traffic is between the instances in the

group. To provide the lowest latency and the highest packet-per-second network performance for your placement group,

choose an instance type that supports **enhanced networking**.

- ✅ :  "Use EC2 instances with Enhanced Networking" is the correct answer.

- ✅ :  "Use Placement groups" is the correct answer.

- ❌ :  "Use Provisioned IOPS EBS volumes" is incorrect

- ❌ :  "Launch I/O Optimized EC2 instances in one private subnet in an AZ" is incorrect. I/O optimized instances

  and provisioned IOPS EBS volumes are more geared towards storage performance than network performance.

- ❌ :  "Use dedicated hosts" is incorrect. Dedicated hosts might ensure close proximity of instances but would not

  be cost efficient.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

----

- #cluster_placement_groups #optimized_ec2_instances #ec2_instances #placement_groups #cluster__
