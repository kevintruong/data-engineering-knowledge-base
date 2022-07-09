#### Question  61


**A Solutions Architect has created a VPC and is in the process of formulating the subnet design. The VPC will be used

to host a two-tier application that will include Internet facing web servers, and internal-only DB servers. Zonal

redundancy is required.**


**How many subnets are required to support this requirement?**


1: 2 subnets


2: 6 subnets


3: 1 subnet


4: 4 subnets


**Answer: 4**


**Explanation:**


Zonal redundancy indicates that the architecture should be split across multiple Availability Zones. Subnets are mapped

1:1 to AZs.


A public subnet should be used for the Internet-facing web servers and a separate private subnet should be used for the

internal-only DB servers. Therefore, you need 4 subnets – 2 (for redundancy) per public/private subnet.


- CORRECT "4 subnets" is the correct answer.


- INCORRECT "2 subnets" is incorrect as explained above.


- INCORRECT "6 subnets" is incorrect as explained above.


- INCORRECT "2 subnet" is incorrect as explained above.


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

