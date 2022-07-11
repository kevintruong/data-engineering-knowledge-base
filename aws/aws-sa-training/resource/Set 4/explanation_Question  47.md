*

**Explanation:**

A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them

using private IPv4 addresses or IPv6 addresses. Instances in either VPC can communicate with each other as if they are

within the same network.

You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account. The VPCs can be in

different regions (also known as an inter-region VPC peering connection).

It is not possible to use transitive peering relationships with VPC peering and therefore you must create an additional

VPC peering connection between VPC-A and VPC-C.

* ✅ :  "Create a new VPC peering connection between VPC-A and VPC-C" is the correct answer.

* ❌ :  "Update VPC-Bs route table with peering targets for VPC-A and VPC-C and enable route propagation" is

  incorrect. Route propagation cannot be used to extend VPC peering connections.

* ❌ :  "Update the CIDR blocks to match to enable inter-VPC routing" is incorrect. You cannot have matching (

  overlapping) CIDR blocks with VPC peering.

* ❌ :  "Update VPC-As route table with an entry using the VPC peering as a target" is incorrect. You must update

  route tables to configure routing however updating VPC-As route table alone will not lead to the desired result

  without first creating the additional peering connection.

**References:**

<https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #<https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html> #inter_-_vpc_routing #update_vpc #vpc #inter_-_region_vpc
