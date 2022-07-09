#### Question  56


**An Amazon EC2 instance behind an Elastic Load Balancer (ELB) is in the process of being de-registered. Which ELB

feature is used to allow existing connections to close cleanly?**


1: Sticky Sessions


2: Proxy Protocol


3: Deletion Protection


4: Connection Draining


**Answer: 4**


**Explanation:**


Connection draining is enabled by default and provides a period of time for existing connections to close cleanly. When

connection draining is in action an CLB will be in the status “InService: Instance deregistration currently in

progress”.


- CORRECT "Connection Draining" is the correct answer.


- INCORRECT "Sticky Sessions" is incorrect. Session stickiness uses cookies and ensures a client is bound to an

  individual back-end instance for the duration of the cookie lifetime.


- INCORRECT "Proxy Protocol" is incorrect. The Proxy Protocol header helps you identify the IP address of a client when

  you have a load balancer that uses TCP for back-end connections.


- INCORRECT "Deletion Protection" is incorrect. Deletion protection is used to protect the ELB from deletion.


**References:**


https://aws.amazon.com/about-aws/whats-new/2014/03/20/elastic-load-balancing-supports-connection-

draining/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

