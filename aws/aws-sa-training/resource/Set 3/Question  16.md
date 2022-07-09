#### Question  16


**A company has experienced malicious traffic from some suspicious IP addresses. The security team discovered the

requests are from different IP addresses under the same CIDR range.**


**What should a solutions architect recommend to the team?**


1: Add a rule in the inbound table of the security group to deny the traffic from that CIDR range


2: Add a rule in the outbound table of the security group to deny the traffic from that CIDR range


3: Add a deny rule in the inbound table of the network ACL with a lower rule number than other rules


4: Add a deny rule in the outbound table of the network ACL with a lower rule number than other rules


Answer: 3


**Explanation:**


You can only create deny rules with network ACLs, it is not possible with security groups. Network ACLs process rules in

order from the lowest numbered rules to the highest until they reach and allow or deny. The following table describes

some of the differences between security groups and network ACLs:


```

Region A

```


```

Availability Zone A

```


```

Shard

```


```

Replica 1

```


```

Availability Zone B

```


```

Replica 2

```


```

Primary

```


```

ElastiCache Redis Cluster

```


```

Shard

```


```

Replica 1 Replica^2

```


```

Primary

```


```

Shard

```


```

Replica 1 Replica 2

```


```

Primary

```


Therefore, the solutions architect should add a deny rule in the inbound table of the network ACL with a lower rule

number than other rules.


- CORRECT "Add a deny rule in the inbound table of the network ACL with a lower rule number than other rules" is the

  correct answer.


- INCORRECT "Add a deny rule in the outbound table of the network ACL with a lower rule number than other rules" is

  incorrect as this will only block outbound traffic.


- INCORRECT "Add a rule in the inbound table of the security group to deny the traffic from that CIDR range" is

  incorrect as you cannot create a deny rule with a security group.


- INCORRECT "Add a rule in the outbound table of the security group to deny the traffic from that CIDR range"

  is incorrect as you cannot create a deny rule with a security group.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

