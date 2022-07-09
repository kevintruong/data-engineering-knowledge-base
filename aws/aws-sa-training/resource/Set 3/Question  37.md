#### Question  37


**A Solutions Architect is determining the best method for provisioning Internet connectivity for a data- processing

application that will pull large amounts of data from an object storage system via the Internet. The solution must be

redundant and have no constraints on bandwidth.**


**Which option satisfies these requirements?**


1: Deploy NAT Instances in a public subnet


2: Use a NAT Gateway


3: Create a VPC endpoint


4: Attach an Internet Gateway


Answer: 4


**Explanation:**


An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication

between your VPC and the internet.


An internet gateway serves two purposes: to provide a target in your VPC route tables for internet-routable traffic, and

to perform network address translation (NAT) for instances that have been assigned public IPv4 addresses.


An internet gateway supports IPv4 and IPv6 traffic. It does not cause availability risks or bandwidth constraints on

your network traffic.


- CORRECT "Attach an Internet Gateway" is the correct answer.


- INCORRECT "Deploy NAT Instances in a public subnet" is incorrect. NAT instances are EC2 instances that are used, in a

  similar way to NAT gateways, by instances in private subnets to access the Internet. However they are not redundant

  and are limited in bandwidth.


- INCORRECT "Use a NAT Gateway" is incorrect as a NAT gateway does impose a limit of 45 Gbps.


- INCORRECT "Create a VPC endpoint" is incorrect. A VPC endpoint is used to access public services from a VPC without

  traversing the Internet.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

