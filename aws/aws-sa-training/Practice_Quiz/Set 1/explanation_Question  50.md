**Explanation:**

In this scenario you need to connect the EC2 instances to the SaaS application with a source address of one of two

whitelisted public IP addresses to ensure authentication works.

A NAT Gateway is created in a specific AZ and can have a single Elastic IP address associated with it. NAT Gateways are

deployed in public subnets and the route tables of the private subnets where the EC2 instances reside are configured to

forward Internet-bound traffic to the NAT Gateway. You do pay for using a NAT Gateway based on hourly usage and data

processing, however this is still a cost-effective solution.

The diagram below depicts an instance in a private subnet using a NAT gateway to connect out to the internet via an

internet gateway.

- ✅ :  "Configure a NAT Gateway for each AZ with an Elastic IP address" is the correct answer.

- ❌ :  "Use a Network Load Balancer and configure a static IP for each AZ" is incorrect. A Network Load Balancer

  can be configured with a single static IP address (the other types of ELB cannot) for each AZ. However, using a NLB is

  not an appropriate solution as the connections are being made outbound from the EC2 instances to the SaaS app and ELBs

  are used for distributing inbound connection requests to EC2 instances

  (only return traffic goes back through the ELB).

- ❌ :  "Use multiple Internet-facing Application Load Balancers with Elastic IP addresses" is incorrect. An ALB

  does not support static IP addresses and is not suitable for a proxy function.

- ❌ :  "Configure redundant Internet Gateways and update the routing tables for each subnet" is incorrect as you

  cannot create multiple Internet Gateways. An IGW is already redundant.

```

Region

```

```

VPC

```

```

Availability Zone

Public subnet

```

```

Internet

gateway

```

```

EC 2 Instance

```

```

Private subnet

```

```

Destination Target

172.31.0.0/ 16 Local

0.0.0.0/ 0 igw-id

```

```

Public Subnet Route Table

```

```

Private Subnet Route Table

```

```

NAT gateway

```

```

Destination Target

172.31.0.0/ 16 Local

0.0.0.0/ 0 nat-gateway-id

```

```

Private-IP

```

```

Private-IP

```

```

Elastic-IP

```

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----

- #single_elastic_ip_address #elastic_ip_addresses #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>>- #elastic_ip_address #ec2_instances
