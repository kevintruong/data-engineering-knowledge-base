#### Question  40


**A Solutions Architect is considering the best approach to enabling Internet access for EC2 instances in a private

subnet. What advantages do NAT Gateways have over NAT Instances? (Select TWO)**


1: Can be assigned to security groups


2: Can be used as a bastion host


3: Managed for you by AWS


4: Highly available within each AZ


5: Can be scaled up manually


**Answer: 3,4**


**Explanation:**


NAT gateways are managed for you by AWS. NAT gateways are highly available in each AZ into which they are deployed. They

are not associated with any security groups and can scale automatically up to 45Gbps


NAT instances are managed by you. They must be scaled manually and do not provide HA. NAT Instances can be used as

bastion hosts and can be assigned to security groups.


- CORRECT "Managed for you by AWS" is a correct answer.


- CORRECT "Highly available within each AZ" is also a correct answer.


- INCORRECT "Can be assigned to security groups" is incorrect as you cannot assign security groups to NAT gateways but

  you can to NAT instances.


- INCORRECT "Can be used as a bastion host" is incorrect, only a NAT instance can be used as a bastion host.


- INCORRECT "Can be scaled up manually" is incorrect, though automatic is better anyway!


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

