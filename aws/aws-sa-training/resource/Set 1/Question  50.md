#### Question  50


**An application runs on two EC2 instances in private subnets split between two AZs. The application needs to connect to

a CRM SaaS application running on the Internet. The vendor of the SaaS application restricts authentication to a

whitelist of source IP addresses and only 2 IP addresses can be configured per customer.**


**What is the most appropriate and cost-effective solution to enable authentication to the SaaS application?**


- [ ] Use a Network Load Balancer and configure a static IP for each AZ


- [ ] Use multiple Internet-facing Application Load Balancers with Elastic IP addresses


- [ ] Configure redundant Internet Gateways and update the routing tables for each subnet


- [x] Configure a NAT Gateway for each AZ with an Elastic IP address

