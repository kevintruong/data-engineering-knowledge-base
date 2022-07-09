#### Question  42


**An Amazon EC2 instance is generating very high packets-per-second and performance of the application stack is being

impacted. A Solutions Architect needs to determine a resolution to the issue that results in improved performance.**


**Which action should the Architect take?**


1: Configure a RAID 1 array from multiple EBS volumes


2: Create a placement group and put the EC2 instance in it


3: Use enhanced networking


4: Add multiple Elastic IP addresses to the instance


**Answer: 3**


**Explanation:**


Enhanced networking provides higher bandwidth, higher packet-per-second (PPS) performance, and consistently lower

inter-instance latencies. If your packets-per-second rate appears to have reached its ceiling, you should consider

moving to enhanced networking because you have likely reached the upper thresholds of the VIF driver. It is only

available for certain instance types and only supported in VPC. You must also launch an HVM AMI with the appropriate

drivers


AWS currently supports enhanced networking capabilities using SR-IOV. SR-IOV provides direct access to network adapters,

provides higher performance (packets-per-second) and lower latency.


- CORRECT "Use enhanced networking" is the correct answer.


- INCORRECT "Configure a RAID 1 array from multiple EBS volumes" is incorrect. You do not need to create a RAID 1

  array (which is more for redundancy than performance anyway).


- INCORRECT "Create a placement group and put the EC2 instance in it" is incorrect. A placement group is used to

  increase network performance between instances. In this case there is only a single instance so it won’t help.


- INCORRECT "Add multiple Elastic IP addresses to the instance" is incorrect. Adding multiple IP addresses is not a way

  to increase performance of the instance as the same amount of bandwidth is available to the Elastic Network

  Interface (ENI).


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/enable-configure-enhanced-networking/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

