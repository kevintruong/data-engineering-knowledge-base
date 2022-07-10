#### Question  2


**To increase performance and redundancy for an application a company has decided to run multiple implementations in

different AWS Regions behind network load balancers. The company currently advertise the application using two public IP

addresses from separate /24 address ranges and would prefer not to change these. Users should be directed to the closest

available application endpoint.**


**Which actions should a solutions architect take? (Select TWO)**


- [ ] Create an Amazon Route 53 geolocation based routing policy


- [x] Create an AWS Global Accelerator and attach endpoints in each AWS Region


- [ ] Assign new static anycast IP addresses and modify any existing pointers


- [x] Migrate both public IP addresses to the AWS Global Accelerator


- [ ] Create PTR records to map existing public IP addresses to an Alias



- hasExplain:: [[explanation_Question  2.md]]