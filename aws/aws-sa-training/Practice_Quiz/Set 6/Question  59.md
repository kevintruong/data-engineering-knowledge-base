#### Question  59

**An on-premise data center will be connected to an Amazon VPC by a hardware VPN that has public and VPN-only subnets.

The security team has requested that traffic hitting public subnets on AWS that’s destined to on-premise applications

must be directed over the VPN to the corporate firewall.**

**How can this be achieved?**

- [ ] :  In the VPN-only subnet route table, add a route that directs all Internet traffic to the virtual private gateway

- [ ] :  In the public subnet route table, add a route for your remote network and specify the customer gateway as the target

- [ ] :  Configure a NAT Gateway and configure all traffic to be directed via the virtual private gateway

- [x] :  In the public subnet route table, add a route for your remote network and specify the virtual private gateway as the

target

*----

- #amazon_vpc #virtual_private_gateway #nat_gateway #aws #public_subnet_route_table
- hasExplain:: [[explanation_Question  59.md]]
