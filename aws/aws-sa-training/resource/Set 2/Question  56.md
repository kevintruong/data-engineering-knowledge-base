#### Question  56


**A large media site has multiple applications running on Amazon ECS. A Solutions Architect needs to use content

metadata to route traffic to specific services.**


**What is the MOST efficient method to fulfil this requirement?**


1: Use an AWS Classic Load Balancer with a host-based routing rule to route traffic to the correct service


2: Use the AWS CLI to update an Amazon Route 53 hosted zone to route traffic as services get updated


3: Use an AWS Application Load Balancer with a path-based routing rule to route traffic to the correct service


4: Use Amazon CloudFront to manage and route traffic to the correct service


Answer: 3


**Explanation:**


The ELB Application Load Balancer can route traffic based on data included in the request including the host name

portion of the URL as well as the path in the URL. Creating a rule to route traffic based on information in the path

will work for this solution and ALB works well with Amazon ECS.


The diagram below depicts a configuration where a listener directs traffic that comes in with /orders in the URL to the

second target group and all other traffic to the first target group:


- CORRECT "Use an AWS Application Load Balancer with a path-based routing rule to route traffic to the correct service"

  is the correct answer.


- INCORRECT "Use an AWS Classic Load Balancer with a host-based routing rule to route traffic to the correct service"

  is incorrect. The ELB Classic Load Balancer does not support any content-based routing including host or path-based.


- INCORRECT "Use the AWS CLI to update an Amazon Route 53 hosted zone to route traffic as services get updated" is

  incorrect. Using the AWS CLI to update Route 53 as to how to route traffic may work, but it is definitely not the most

  efficient way to solve this challenge.


- INCORRECT "Use Amazon CloudFront to manage and route traffic to the correct service" is incorrect. Amazon CloudFront

  does not have the capability to route traffic to different Amazon ECS services based on content metadata.


**References:**


https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-load-balancer-routing.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

