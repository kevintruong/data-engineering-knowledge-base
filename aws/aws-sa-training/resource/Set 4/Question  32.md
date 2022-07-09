#### Question  32


1:


2:


3:


**A website uses web servers behind an Internet-facing Elastic Load Balancer. What record set should be created to point

the customer’s DNS zone apex record at the ELB?**


1: Create a PTR record pointing to the DNS name of the load balancer


2: Create an A record pointing to the DNS name of the load balancer


3: Create a CNAME record that is an Alias, and select the ELB DNS as a target


4: Create an A record that is an Alias, and select the ELB DNS as a target


**Answer: 4**


**Explanation:**


An Alias record can be used for resolving apex or naked domain names (e.g. example.com). You can create an A record that

is an Alias that uses the customer’s website zone apex domain name and map it to the ELB DNS name.


- CORRECT "Create an A record that is an Alias, and select the ELB DNS as a target" is the correct answer.


- INCORRECT "Create a PTR record pointing to the DNS name of the load balancer" is incorrect. PTR records are reverse

  lookup records where you use the IP to find the DNS name.


- INCORRECT "Create an A record pointing to the DNS name of the load balancer" is incorrect. A standard A record maps

  the DNS domain name to the IP address of a resource. You cannot obtain the IP of the ELB so you must use an Alias

  record which maps the DNS domain name of the customer’s website to the ELB DNS name

  (rather than its IP).


- INCORRECT "Create a CNAME record that is an Alias, and select the ELB DNS as a target" is incorrect. A CNAME record

  can’t be used for resolving apex or naked domain names.


**References:**


https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-route-53/

