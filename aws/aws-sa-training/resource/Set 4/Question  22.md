#### Question  22


**You recently noticed that your Network Load Balancer (NLB) in one of your VPCs is not distributing traffic evenly

between EC2 instances in your AZs. There are an odd number of EC2 instances spread across two AZs. The NLB is configured

with a TCP listener on port 80 and is using active health checks.**


**What is the most likely problem?**


1: There is no HTTP listener


2: Health checks are failing in one AZ due to latency


3: NLB can only load balance within a single AZ


4: Cross-zone load balancing is disabled


**Answer: 4**


**Explanation:**


Without cross-zone load balancing enabled, the NLB will distribute traffic 50/50 between AZs. As there are an odd number

of instances across the two AZs some instances will not receive any traffic. Therefore enabling cross-zone load

balancing will ensure traffic is distributed evenly between available instances in all AZs.


The diagram below shows an ELB with cross-zone load balancing enabled:


- CORRECT "Cross-zone load balancing is disabled" is the correct answer.


- INCORRECT "There is no HTTP listener" is incorrect. Listeners are used to receive incoming connections. An NLB listens

  on TCP not on HTTP therefore having no HTTP listener is not the issue here.


- INCORRECT "Health checks are failing in one AZ due to latency" is incorrect. If health checks fail this will cause the

  NLB to stop sending traffic to these instances. However, the health check packets are very small and it is unlikely

  that latency would be the issue within a region.


```

VPC

```


```

Availability Zone A

Public subnet

```


```

Internet Client

```


```

ELB Node

```


```

Elastic Load Balancing

```


```

Availability Zone B

Public subnet

```


```

ELB Node

```


```

60 %

```


```

40 %

```


```

20 %

```


```

20 %

```


```

20 %

```


```

20 %

```


```

20 %

```


- INCORRECT "NLB can only load balance within a single AZ" is incorrect. An NLB can load balance across multiple AZs

  just like the other ELB types.


**References:**


https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

