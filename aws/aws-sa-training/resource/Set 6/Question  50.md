#### Question  50


**A company requires an Elastic Load Balancer (ELB) for an application they are planning to deploy on AWS. The

application requires extremely high throughput and extremely low latencies. The connections will be made using the TCP

protocol and the ELB must support load balancing to multiple ports on an instance. Which ELB would should the company

use?**


1: Classic Load Balancer


2: Application Load Balancer


3: Network Load Balancer


4: Route 53


**Answer: 3**


**Explanation:**


**The Network Load Balancer operates at the connection level (Layer 4), routing connections to targets – Amazon EC2

instances, containers and IP addresses based on IP protocol data. It is architected to handle millions of requests/sec,

sudden volatile traffic patterns and provides extremely low latencies.**


**The NLB provides high throughput and extremely low latencies and is designed to handle traffic as it grows and can

load balance millions of requests/second. NLB also supports load balancing to multiple ports on an instance.**


- CORRECT "Network Load Balancer" is the correct answer.


- INCORRECT "Classic Load Balancer" is incorrect. The CLB operates using the TCP, SSL, HTTP and HTTPS protocols. It is

  not the best choice for requirements of extremely high throughput and low latency and does not support load balancing

  to multiple ports on an instance.


- INCORRECT "Application Load Balancer" is incorrect. The ALB operates at the HTTP and HTTPS level only (does not

  support TCP load balancing).


- INCORRECT "Route 53" is incorrect. Route 53 is a DNS service, it is not a type of ELB (though you can do some types of

  load balancing with it).


**References:**


https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

