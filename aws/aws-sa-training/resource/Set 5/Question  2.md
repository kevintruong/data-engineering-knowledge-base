#### Question  2


**A Solutions Architect is deploying a high performance computing (HPC) application on Amazon EC2 instances. The

application requires extremely low inter-instance latency. How should the instances be deployed for BEST performance?**


1: Use an instance with enhanced networking and deploy the instances in a partition placement group


2: Use an Elastic Fabric Adapter (EFA) and deploy instances in a cluster placement group


3: Add multiple Elastic Network Adapters (ENAs) to each instance and create a NIC team


4: Use an EBS-optimized instance with 10 Gigabit networking and deploy to a single subnet


Answer: 2


**Explanation:**


It is recommended to use either enhanced networking or an Elastic Fabric Adapter (EFA) for the nodes of an HPC

application. This will assist with decreasing latency. Additionally, a cluster placement group packs instances close

together inside an Availability Zone.


Using a cluster placement group enables workloads to achieve the low-latency network performance necessary for

tightly-coupled node-to-node communication that is typical of HPC applications.


The table below helps you to understand the key differences between the different placement group options:


- CORRECT "Use an Elastic Fabric Adapter (EFA) and deploy instances in a cluster placement group" is the correct answer.


- INCORRECT "Use an instance with enhanced networking and deploy the instances in a partition placement group" is

  incorrect. A partition placement group protects instances from correlated hardware failures, it does not offer the

  best inter-instance network performance.


- INCORRECT "Add multiple Elastic Network Adapters (ENAs) to each instance and create a NIC team" is incorrect. You

  cannot use NIC teaming methods on AWS to increase the bandwidth to your application. This will also not reduce

  latency.


- INCORRECT "Use an EBS-optimized instance with 10 Gigabit networking and deploy to a single subnet" is incorrect. EBS

  optimization is related to storage, not to network performance. A 10 Gigabit adapter offers great bandwidth but for

  lowest latency enhanced networking with a cluster placement group should be used.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

