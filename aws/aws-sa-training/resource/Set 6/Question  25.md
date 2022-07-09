#### Question  25


**An Amazon EC2 instance has been launched into an Amazon VPC. A Solutions Architect needs to ensure that instances have

both a private and public DNS hostnames. Assuming settings were not changed during creation of the VPC, how will DNS

hostnames be assigned by default? (Select TWO)**


1: In all VPCs instances no DNS hostnames will be assigned


2: In a non-default VPC instances will be assigned a public and private DNS hostname


3: In a default VPC instances will be assigned a public and private DNS hostname


4: In a non-default VPC instances will be assigned a private but not a public DNS hostname


5: In a default VPC instances will be assigned a private but not a public DNS hostname


**Answer: 3,4**


**Explanation:**


When you launch an instance into a default VPC, we provide the instance with public and private DNS hostnames that

correspond to the public IPv4 and private IPv4 addresses for the instance.


When you launch an instance into a nondefault VPC, we provide the instance with a private DNS hostname and we might

provide a public DNS hostname, depending on the DNS attributes you specify for the VPC and if your instance has a public

IPv4 address.


All other statements are incorrect with default settings.


- CORRECT "In a default VPC instances will be assigned a public and private DNS hostname" is the correct answer.


- CORRECT "In a non-default VPC instances will be assigned a private but not a public DNS hostname" is the correct

  answer.


- INCORRECT "In all VPCs instances no DNS hostnames will be assigned" is incorrect as explained above.


- INCORRECT "In a non-default VPC instances will be assigned a public and private DNS hostname" is incorrect as

  explained above.


- INCORRECT "In a default VPC instances will be assigned a private but not a public DNS hostname" is incorrect as

  explained above.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

