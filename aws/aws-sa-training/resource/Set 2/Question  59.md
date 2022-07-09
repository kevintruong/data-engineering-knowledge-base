#### Question  59


**A VPC has a fleet of EC2 instances running in a private subnet that need to connect to Internet-based hosts using the

IPv6 protocol. What needs to be configured to enable this connectivity?**


1: VPN CloudHub


2: A NAT Gateway


3: An Egress-Only Internet Gateway


4: AWS Direct Connect


Answer: 3


**Explanation:**


An egress-only Internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows

outbound communication over IPv6 from instances in your VPC to the Internet, and prevents the Internet from initiating

an IPv6 connection with your instances.


- CORRECT "An Egress-Only Internet Gateway" is the correct answer.


```

Region

```


```

VPC

```


```

Availability Zone

```


```

Each instance is located

on a separate AWS rack

```


```

Availability Zone

```


- INCORRECT "VPN CloudHub" is incorrect. VPN CloudHub enables a hub-and-spoke model for communicating between multiple

  sites over a VPN connection.


- INCORRECT "A NAT Gateway" is incorrect. A NAT Gateway is used for enabling Internet connectivity using the IPv4

  protocol only.


- INCORRECT "AWS Direct Connect" is incorrect. AWS Direct Connect is a private connection between your data center and

  an AWS VPC.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

