#### Question  20


**A company has multiple Amazon VPCs that are peered with each other. The company would like to use a single Elastic

Load Balancer (ELB) to route traffic to multiple EC2 instances in peered VPCs within the same region. How can this be

achieved?**


1: This is not possible, the instances that an ELB routes traffic to must be in the same VPC


2: This is possible using the Classic Load Balancer (CLB) if using Instance IDs


3: This is possible using the Network Load Balancer (NLB) and Application Load Balancer (ALB) if using IP addresses as

targets


4: This is not possible with ELB, you would need to use Route 53


**Answer: 3**


**Explanation:**


With ALB and NLB IP addresses can be used to register:


- Instances in a peered VPC.

- AWS resources that are addressable by IP address and port.

- On-premises resources linked to AWS through Direct Connect or a VPN connection.


- CORRECT "This is possible using the Network Load Balancer (NLB) and Application Load Balancer (ALB) if using IP

  addresses as targets" is the correct answer.


- INCORRECT "This is not possible, the instances that an ELB routes traffic to must be in the same VPC" is incorrect.

  Instances can be in peered VPCs.


- INCORRECT "This is possible using the Classic Load Balancer (CLB) if using Instance IDs" is incorrect. This is not

  possible with the CLB.


- INCORRECT "This is not possible with ELB, you would need to use Route 53" is incorrect. This is not true, as detailed

  above.


**References:**


https://aws.amazon.com/blogs/aws/new-application-load-balancing-via-ip-address-to-aws-on-premises-

resources/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

