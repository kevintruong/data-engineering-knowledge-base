#### Question  18


**A solutions architect is designing a two-tier web application. The application consists of a public-facing web tier

hosted on Amazon EC2 in public subnets. The database tier consists of Microsoft SQL Server running on Amazon EC2 in a

private subnet. Security is a high priority for the company.**


**How should security groups be configured in this situation? (Select TWO)**


1: Configure the security group for the web tier to allow inbound traffic on port 443 from 0.0.0.0/0


2: Configure the security group for the web tier to allow outbound traffic on port 443 from 0.0.0.0/0


3: Configure the security group for the database tier to allow inbound traffic on port 1433 from the security group for

the web tier


4: Configure the security group for the database tier to allow outbound traffic on ports 443 and 1433 to the security

group for the web tier


5: Configure the security group for the database tier to allow inbound traffic on ports 443 and 1433 from the security

group for the web tier


Answer: 1, 3


**Explanation:**


In this scenario an inbound rule is required to allow traffic from any internet client to the web front end on SSL/TLS

port 443. The source should therefore be set to 0.0.0.0/0 to allow any inbound traffic.


To secure the connection from the web frontend to the database tier, an outbound rule should be created from the public

EC2 security group with a destination of the private EC2 security group. The port should be set to 1433 for MySQL. The

private EC2 security group will also need to allow inbound traffic on 1433 from the public EC2 security group.


This configuration can be seen in the diagram:


```

Private subnet(s)

```


```

VPC Public subnet(s)

```


```

Inbound: Protocol/Port HTTP/ 443 Source: 0. 0. 0. 0 / 0

Outbound: Protocol/Port HTTPS: 1433 Destination: PrivateEC 2

```


```

Security group – PublicEC 2

```


```

Security group – PrivateEC 2

Inbound: Protocol/Port HTTP/ 1433 Source: PublicALB

Web Front-End

```


```

Web Front-End

```


- CORRECT "Configure the security group for the web tier to allow inbound traffic on port 443 from 0.0.0.0/0" is a

  correct answer.


- CORRECT "Configure the security group for the database tier to allow inbound traffic on port 1433 from the security

  group for the web tier" is also a correct answer.


- INCORRECT "Configure the security group for the web tier to allow outbound traffic on port 443 from 0.0.0.0/0" is

  incorrect as this is configured backwards.


- INCORRECT "Configure the security group for the database tier to allow outbound traffic on ports 443 and 1433 to the

  security group for the web tier" is incorrect as the MySQL database instance does not need to send outbound traffic on

  either of these ports.


- INCORRECT "Configure the security group for the database tier to allow inbound traffic on ports 443 and 1433 from the

  security group for the web tier" is incorrect as the database tier does not need to allow inbound traffic on port


443.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

