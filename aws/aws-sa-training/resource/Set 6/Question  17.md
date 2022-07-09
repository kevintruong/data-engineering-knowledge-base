#### Question  17


**A company has a fleet of Amazon EC2 instances behind an Elastic Load Balancer (ELB) that are a mixture of c4.2xlarge

instance types and c5.large instances. The load on the CPUs on the c5.large instances has been very high, often hitting

100% utilization, whereas the c4.2xlarge instances have been performing well.**


**What should a Solutions Architect recommend to resolve the performance issues?**


1: Enable the weighted routing policy on the ELB and configure a higher weighting for the c4.2xlarge instances


2: Add all of the instances into a Placement Group


3: Change the configuration to use only c4.2xlarge instance types


4: Add more c5.large instances to spread the load more evenly


**Answer: 3**


**Explanation:**


The 2xlarge instance type provides more CPUs. The best answer is to use this instance type for all instances as the CPU

utilization has been lower.


- CORRECT "Change the configuration to use only c4.2xlarge instance types" is the correct answer.


- INCORRECT "Enable the weighted routing policy on the ELB and configure a higher weighting for the c4.2xlarge

  instances" is incorrect. The weighted routing policy is a Route 53 feature that would not assist in this situation.


- INCORRECT "Add all of the instances into a Placement Group" is incorrect. A placement group helps provide low-latency

  connectivity between instances and would not help here.


- INCORRECT "Add more c5.large instances to spread the load more evenly" is incorrect. This would not help as this

  instance type is underperforming with high CPU utilization rates.


**References:**


https://aws.amazon.com/ec2/instance-types/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

