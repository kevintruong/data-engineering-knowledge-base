#### Question  2


**To increase performance and redundancy for an application a company has decided to run multiple implementations in

different AWS Regions behind network load balancers. The company currently advertise the application using two public IP

addresses from separate /24 address ranges and would prefer not to change these. Users should be directed to the closest

available application endpoint.**


**Which actions should a solutions architect take? (Select TWO)**


1: Create an Amazon Route 53 geolocation based routing policy


2: Create an AWS Global Accelerator and attach endpoints in each AWS Region


3: Assign new static anycast IP addresses and modify any existing pointers


4: Migrate both public IP addresses to the AWS Global Accelerator


5: Create PTR records to map existing public IP addresses to an Alias


Answer: 2,4


**Explanation:**


AWS Global Accelerator uses static IP addresses as fixed entry points for your application. You can migrate up to two

/24 IPv4 address ranges and choose which /32 IP addresses to use when you create your accelerator.


This solution ensures the company can continue using the same IP addresses and they are able to direct traffic to the

application endpoint in the AWS Region closest to the end user. Traffic is sent over the AWS global network for

consistent performance.


- CORRECT "Create an AWS Global Accelerator and attach endpoints in each AWS Region" is a correct answer.


- CORRECT "Migrate both public IP addresses to the AWS Global Accelerator" is also a correct answer.


- INCORRECT "Create an Amazon Route 53 geolocation based routing policy" is incorrect. With this solution new IP

  addresses will be required as there will be application endpoints in different regions.


- INCORRECT "Assign new static anycast IP addresses and modify any existing pointers" is incorrect. This is unnecessary

  as you can bring your own IP addresses to AWS Global Accelerator and this is preferred in this scenario.


- INCORRECT "Create PTR records to map existing public IP addresses to an Alias" is incorrect. This is not a workable

  solution for mapping existing IP addresses to an Amazon Route 53 Alias.


**References:**


https://aws.amazon.com/global-accelerator/features/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/aws-global-accelerator/

