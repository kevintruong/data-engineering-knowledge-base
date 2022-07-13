#### Question  35

**A Solutions Architect has setup a VPC with a public subnet and a VPN-only subnet. The public subnet is associated with

a custom route table that has a route to an Internet Gateway. The VPN-only subnet is associated with the main route

table and has a route to a virtual private gateway.**

**The Architect has created a new subnet in the VPC and launched an EC2 instance in it. However, the instance cannot

connect to the Internet. What is the MOST likely reason?**

- [x] :  The subnet has been automatically associated with the main route table which does not have a route to the Internet

- [ ] :  The new subnet has not been associated with a route table

- [ ] :  The Internet Gateway is experiencing connectivity problems

- [ ] :  There is no NAT Gateway available in the new subnet so Internet connectivity is not possible

*----

- #virtual_private_gateway #new_subnet #nat_gateway #subnet #internet_gateway
- hasExplain:: [[explanation_Question  35.md]]
