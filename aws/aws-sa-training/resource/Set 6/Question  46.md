#### Question  46


**A company is transitioning their web presence into the AWS cloud. As part of the migration the company will be running

a web application both on-premises and in AWS for a period of time. During the period of co- existence, the client would

like 80% of the traffic to hit the AWS-based web servers and 20% to be directed to the on-premises web servers.**


**What method can a Solutions Architect use to distribute traffic as requested?**


1: Use Route 53 with a weighted routing policy and configure the respective weights


2: Use Route 53 with a simple routing policy


3: Use an Application Load Balancer to distribute traffic based on IP address


4: Use a Network Load Balancer to distribute traffic based on Instance ID


**Answer: 1**


**Explanation:**


Route 53 weighted routing policy is similar to simple but you can specify a weight per IP address. You create records

that have the same name and type and assign each record a relative weight which is a numerical value that favors one IP

over another (values must total 100). To stop sending traffic to a resource you can change the weight of the record to


0.


- CORRECT "Use Route 53 with a weighted routing policy and configure the respective weights" is the correct answer.


- INCORRECT "Use Route 53 with a simple routing policy" is incorrect as this will not split traffic based on weights as

  required.


- INCORRECT "Use an Application Load Balancer to distribute traffic based on IP address" is incorrect. Application Load

  Balancer can distribute traffic to AWS and on-premise resources using IP addresses but cannot be used to distribute

  traffic in a weighted manner.


- INCORRECT "Use a Network Load Balancer to distribute traffic based on Instance ID" is incorrect. Network Load Balancer

  can distribute traffic to AWS and on-premise resources using IP addresses (not Instance IDs).


**References:**


https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-route-53/

