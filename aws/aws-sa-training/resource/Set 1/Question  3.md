#### Question  3


**A company delivers content to subscribers distributed globally from an application running on AWS. The application

uses a fleet of Amazon EC2 instance in a private subnet behind an Application Load Balancer

(ALB). Due to an update in copyright restrictions, it is necessary to block access for specific countries.**


**What is the EASIEST method to meet this requirement?**


- [ ] Modify the ALB security group to deny incoming traffic from blocked countries


- [ ] Modify the security group for EC2 instances to deny incoming traffic from blocked countries


- [x] Use Amazon CloudFront to serve the application and deny access to blocked countries


- [ ] Use a network ACL to block the IP address ranges associated with the specific countries



- hasExplain:: [[explanation_Question  3.md]]

#network_acl #amazon_cloudfront #alb_security_group #aws #private_subnet 