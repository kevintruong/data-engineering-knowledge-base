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

- ✅ :  "Configure the security group for the web tier to allow inbound traffic on port 443 from 0.0.0.0/0" is a

  correct answer.

- ✅ :  "Configure the security group for the database tier to allow inbound traffic on port 1433 from the security

  group for the web tier" is also a correct answer.

- ❌ :  "Configure the security group for the web tier to allow outbound traffic on port 443 from 0.0.0.0/0" is

  incorrect as this is configured backwards.

- ❌ :  "Configure the security group for the database tier to allow outbound traffic on ports 443 and 1433 to the

  security group for the web tier" is incorrect as the MySQL database instance does not need to send outbound traffic on

  either of these ports.

- ❌ :  "Configure the security group for the database tier to allow inbound traffic on ports 443 and 1433 from the

  security group for the web tier" is incorrect as the database tier does not need to allow inbound traffic on port

443.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #private_ec2_security_group #ec2_security_group #public_ec2_security_group #port_https #mysql_database_instance
