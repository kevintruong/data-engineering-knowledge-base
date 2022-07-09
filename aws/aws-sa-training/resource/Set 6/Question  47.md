#### Question  47


**A Solutions Architect has created a new Network ACL in an Amazon VPC. No rules have been created. Which of the

statements below are correct regarding the default state of the Network ACL? (Select TWO)**


1: There is a default inbound rule allowing traffic from the VPC CIDR block


2: There is a default outbound rule allowing traffic to the Internet Gateway


3: There is a default outbound rule allowing all traffic


4: There is a default inbound rule denying all traffic


5: There is a default outbound rule denying all traffic


**Answer: 4,5**


**Explanation:**


A VPC automatically comes with a default network ACL which allows all inbound/outbound traffic. A custom NACL denies all

traffic both inbound and outbound by default.


Network ACL’s function at the subnet level and you can have permit and deny rules. Network ACLs have separate inbound

and outbound rules and each rule can allow or deny traffic.


Network ACLs are stateless so responses are subject to the rules for the direction of traffic. NACLs only apply to

traffic that is ingress or egress to the subnet not to traffic within the subnet.


- CORRECT "There is a default inbound rule denying all traffic" is a correct answer.


- CORRECT "There is a default outbound rule denying all traffic" is also a correct answer.


- INCORRECT "There is a default inbound rule allowing traffic from the VPC CIDR block" is incorrect as inbound traffic

  is not allowed from anywhere by default.


- INCORRECT "There is a default outbound rule allowing traffic to the Internet Gateway" is incorrect as outbound traffic

  is not allowed to anywhere by default.


- INCORRECT "There is a default outbound rule allowing all traffic" is incorrect as all traffic is denied.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

