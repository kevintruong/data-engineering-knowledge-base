#### Question  59


**An on-premise data center will be connected to an Amazon VPC by a hardware VPN that has public and VPN-only subnets.

The security team has requested that traffic hitting public subnets on AWS that’s destined to on-premise applications

must be directed over the VPN to the corporate firewall.**


**How can this be achieved?**


1: In the VPN-only subnet route table, add a route that directs all Internet traffic to the virtual private gateway


2: In the public subnet route table, add a route for your remote network and specify the customer gateway as the target


3: Configure a NAT Gateway and configure all traffic to be directed via the virtual private gateway


4: In the public subnet route table, add a route for your remote network and specify the virtual private gateway as the

target


**Answer: 4**


**Explanation:**


Route tables determine where network traffic is directed. In your route table, you must add a route for your remote

network and specify the virtual private gateway as the target. This enables traffic from your VPC that’s destined for

your remote network to route via the virtual private gateway and over one of the VPN tunnels. You can enable route

propagation for your route table to automatically propagate your network routes to the table for you.


- CORRECT "In the public subnet route table, add a route for your remote network and specify the virtual private gateway

  as the target" is the correct answer.


- INCORRECT "In the VPN-only subnet route table, add a route that directs all Internet traffic to the virtual private

  gateway" is incorrect. You must create the route table rule in the route table attached to the public subnet, not the

  VPN-only subnet.


- INCORRECT "In the public subnet route table, add a route for your remote network and specify the customer gateway as

  the target" is incorrect. You must select the virtual private gateway (AWS side of the VPN) not the customer gateway (

  customer side of the VPN) in the target in the route table.


- INCORRECT "Configure a NAT Gateway and configure all traffic to be directed via the virtual private gateway"

  is incorrect. NAT Gateways are used to enable Internet access for EC2 instances in private subnets, they cannot be

  used to direct traffic to VPG.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_VPN.html


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario3.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

