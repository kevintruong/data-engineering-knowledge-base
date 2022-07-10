#### Question  20


**A company has multiple Amazon VPCs that are peered with each other. The company would like to use a single Elastic

Load Balancer (ELB) to route traffic to multiple EC2 instances in peered VPCs within the same region. How can this be

achieved?**


- [ ] This is not possible, the instances that an ELB routes traffic to must be in the same VPC


- [ ] This is possible using the Classic Load Balancer (CLB) if using Instance IDs


- [x] This is possible using the Network Load Balancer (NLB) and Application Load Balancer (ALB) if using IP addresses as

targets


- [ ] This is not possible with ELB, you would need to use Route 53


*

- hasExplain:: [[explanation_Question  20.md]]

#elb #ec2 #routes #vpc #elastic 