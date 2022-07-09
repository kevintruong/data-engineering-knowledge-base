#### Question  47


**A pharmaceutical company uses a strict process for release automation that involves building and testing services in 3

separate VPCs. A peering topology is configured with VPC-A peered with VPC-B and VPC-B peered with VPC-C. The

development team wants to modify the process so that they can release code directly from VPC-A to VPC-C.**


**How can this be accomplished?**


1: Update VPC-Bs route table with peering targets for VPC-A and VPC-C and enable route propagation


2: Create a new VPC peering connection between VPC-A and VPC-C


3: Update the CIDR blocks to match to enable inter-VPC routing


4: Update VPC-As route table with an entry using the VPC peering as a target


**Answer: 2**


**Explanation:**


A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them

using private IPv4 addresses or IPv6 addresses. Instances in either VPC can communicate with each other as if they are

within the same network.


You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account. The VPCs can be in

different regions (also known as an inter-region VPC peering connection).


It is not possible to use transitive peering relationships with VPC peering and therefore you must create an additional

VPC peering connection between VPC-A and VPC-C.


- CORRECT "Create a new VPC peering connection between VPC-A and VPC-C" is the correct answer.


- INCORRECT "Update VPC-Bs route table with peering targets for VPC-A and VPC-C and enable route propagation" is

  incorrect. Route propagation cannot be used to extend VPC peering connections.


- INCORRECT "Update the CIDR blocks to match to enable inter-VPC routing" is incorrect. You cannot have matching (

  overlapping) CIDR blocks with VPC peering.


- INCORRECT "Update VPC-As route table with an entry using the VPC peering as a target" is incorrect. You must update

  route tables to configure routing however updating VPC-As route table alone will not lead to the desired result

  without first creating the additional peering connection.


**References:**


https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

