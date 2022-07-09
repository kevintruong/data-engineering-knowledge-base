#### Question  13


**A solutions architect is designing a high performance computing (HPC) application using Amazon EC2 Linux instances.

All EC2 instances need to communicate to each other with low latency and high throughput network performance.**


**Which EC2 solution BEST meets these requirements?**


1: Launch the EC2 instances in a cluster placement group in one Availability Zone


2: Launch the EC2 instances in a spread placement group in one Availability Zone


3: Launch the EC2 instances in an Auto Scaling group in two Regions. Place a Network Load Balancer in front of the

instances


4: Launch the EC2 instances in an Auto Scaling group spanning multiple Availability Zones


Answer: 1


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


For this scenario, a cluster placement group should be used as this is the best option for providing low-latency network

performance for a HPC application.


- CORRECT "Launch the EC2 instances in a cluster placement group in one Availability Zone" is the correct answer.


- INCORRECT "Launch the EC2 instances in a spread placement group in one Availability Zone" is incorrect as the spread

  placement group is used to spread instances across distinct underlying hardware.


- INCORRECT "Launch the EC2 instances in an Auto Scaling group in two Regions. Place a Network Load Balancer in front of

  the instances" is incorrect as this does not achieve the stated requirement to provide low- latency, high throughput

  network performance between instances. Also, you cannot use an ELB across Regions.


- INCORRECT "Launch the EC2 instances in an Auto Scaling group spanning multiple Availability Zones" is incorrect as

  this does not reduce network latency or improve performance.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

