#### VPC PEERING


A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them

using private IPv4 addresses or IPv6 addresses.


Instances in either VPC can communicate with each other as if they are within the same network.


You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account.


The VPCs can be in different regions (also known as an inter-region VPC peering connection).


Data sent between VPCs in different regions is encrypted (traffic charges apply).


**For inter-region VPC peering there are some limitations:**


- You cannot create a security group rule that references a peer security group.

- Cannot enable DNS resolution.

- Maximum MTU is 1500 bytes (no jumbo frames support).



- Limited region support.


AWS uses the existing infrastructure of a VPC to create a VPC peering connection.


It is neither a gateway nor a VPN connection and does not rely on a separate piece of physical hardware.


There is no single point of failure for communication or a bandwidth bottleneck.


A VPC peering connection helps you to facilitate the transfer of data.


Can only have one peering connection between any two VPCs at a time.


Can peer with other accounts (within or between regions).


Cannot have overlapping CIDR ranges.


A VPC peering connection is a one to one relationship between two VPCs.


You can create multiple VPC peering connections for each VPC that you own, but transitive peering relationships are not

supported.


You do not have any peering relationship with VPCs that your VPC is not directly peered with.


Limits are 50 VPC peers per VPC, up to 125 by request.


DNS is supported.


Must update route tables to configure routing.


Must update the inbound and outbound rules for VPC security group to reference security groups in the peered VPC.


When creating a VPC peering connection with another account you need to enter the account ID and VPC ID from the other

account.


Need to accept the pending access request in the peered VPC.


The VPC peering connection can be added to route tables – shows as a target starting with “pcx-“.

