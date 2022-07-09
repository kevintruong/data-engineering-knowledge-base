#### Question  39


**A company is deploying a new two-tier web application that uses EC2 web servers and a DynamoDB database backend. An

Internet facing ELB distributes connections between the web servers.**


**The Solutions Architect has created a security group for the web servers and needs to create a security group for the

ELB. What rules should be added? (Select TWO)**


- [x] Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as the web server security group


- [ ] Add an Outbound rule that allows ALL TCP, and specify the destination as the Internet Gateway


- [ ] Add an Outbound rule that allows HTTP/HTTPS, and specify the destination as VPC CIDR


- [x] Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/0


- [ ] Add an Inbound rule that allows HTTP/HTTPS, and specify the source as 0.0.0.0/32


*