#### Question  10


**A Solutions Architect needs to capture information about the traffic that reaches an Amazon Elastic Load Balancer. The

information should include the source, destination, and protocol.**


**What is the most secure and reliable method for gathering this data?**


1 : Create a VPC flow log for each network interface associated with the ELB


2: Enable Amazon CloudTrail logging and configure packet capturing


3: Use Amazon CloudWatch Logs to review detailed logging information


4: Create a VPC flow log for the subnets in which the ELB is running


Answer: 1


**Explanation:**


You can use VPC Flow Logs to capture detailed information about the traffic going to and from your Elastic Load

Balancer. Create a flow log for each network interface for your load balancer. There is one network interface per load

balancer subnet.


- CORRECT "Create a VPC flow log for each network interface associated with the ELB" is the correct answer.


- INCORRECT "Enable Amazon CloudTrail logging and configure packet capturing" is incorrect. CloudTrail performs auditing

  of API actions, it does not do packet capturing.


- INCORRECT "Use Amazon CloudWatch Logs to review detailed logging information" is incorrect as this service does not

  record this information in CloudWatch logs.


- INCORRECT "Create a VPC flow log for the subnets in which the ELB is running" is incorrect as the more secure option

  is to use the ELB network interfaces.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-monitoring.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

