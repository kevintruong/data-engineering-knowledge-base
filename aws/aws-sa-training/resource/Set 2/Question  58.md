#### Question  58


**An application that you will be deploying in your VPC requires 14 EC2 instances that must be placed on distinct

underlying hardware to reduce the impact of the failure of a hardware node. The instances will use varying instance

types. What configuration will cater to these requirements taking cost-effectiveness into account?**


1: You cannot control which nodes your instances are placed on


2: Use dedicated hosts and deploy each instance on a dedicated host


3: Use a Spread Placement Group across two AZs


4: Use a Cluster Placement Group within a single AZ


Answer: 3


**Explanation:**


A spread placement group is a group of instances that are each placed on distinct underlying hardware. Spread placement

groups are recommended for applications that have a small number of critical instances that should be kept separate from

each other. Launching instances in a spread placement group reduces the risk of simultaneous failures that might occur

when instances share the same underlying hardware.


- CORRECT "Use a Spread Placement Group across two AZs" is the correct answer.


- INCORRECT "You cannot control which nodes your instances are placed on" is incorrect as you can use placement groups.


- INCORRECT "Use dedicated hosts and deploy each instance on a dedicated host" is incorrect. Using a single instance on

  each dedicated host would be extremely expensive.


- INCORRECT "Use a Cluster Placement Group within a single AZ" is incorrect. A cluster placement group is a logical

  grouping of instances within a single Availability Zone. Cluster placement groups are recommended for applications

  that benefit from low network latency, high network throughput, or both, and if the majority of the network traffic is

  between the instances in the group.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

