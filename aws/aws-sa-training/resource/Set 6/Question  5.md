#### Question  5


**An application runs on EC2 instances in a private subnet behind an Application Load Balancer in a public subnet. The

application is highly available and distributed across multiple AZs. The EC2 instances must make API calls to an

internet-based service. How can the Solutions Architect enable highly available internet connectivity?**


- [ ] Create a NAT gateway and attach it to the VPC. Add a route to the gateway to each private subnet route table


- [ ] Configure an internet gateway. Add a route to the gateway to each private subnet route table


- [ ] Create a NAT instance in the private subnet of each AZ. Update the route tables for each private subnet to direct

internet-bound traffic to the NAT instance


- [x] Create a NAT gateway in the public subnet of each AZ. Update the route tables for each private subnet to direct

internet-bound traffic to the NAT gateway

