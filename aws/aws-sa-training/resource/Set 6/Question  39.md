#### Question  39


**A company is deploying a new two-tier web application that uses EC2 web servers and a DynamoDB database backend. An

Internet facing ELB distributes connections between the web servers.**


**The Solutions Architect has created a security group for the web servers and needs to create a security group for the

ELB. What rules should be added? (Select TWO)**


1: Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as the web server security group


2: Add an Outbound rule that allows ALL TCP, and specify the destination as the Internet Gateway


3: Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as VPC CIDR


4: Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/0


5: Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/32


**Answer: 1,4**


**Explanation:**


An inbound rule should be created for the relevant protocols (HTTP/HTTPS) and the source should be set to any address (

0.0.0.0/0).


The outbound rule should forward the relevant protocols (HTTP/HTTPS) and the destination should be set to the web server

security group.


Note that on the web server security group you’d want to add an Inbound rule allowing HTTP/HTTPS from the ELB security

group.


- CORRECT "Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as the web server security group"

  is a correct answer.


- CORRECT "Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/0" is also a correct answer.


- INCORRECT "Add an Outbound rule that allows ALL TCP, and specify the destination as the Internet Gateway"

  is incorrect as the relevant protocol should be specified and the destination should be the web server security group.


- INCORRECT "Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as VPC CIDR" is incorrect. Using

  the VPC CIDR would not be secure and you cannot specify an Internet Gateway in a security group (not that you’d want

  to anyway).


- INCORRECT "Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/32" is incorrect. The address

  0.0.0.0/32 is incorrect as the 32 mask means an exact match is required (0.0.0.0).


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

