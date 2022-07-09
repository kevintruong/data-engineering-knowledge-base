#### Question  26


**A Solutions Architect is building a new Amazon Elastic Container Service (ECS) cluster. The ECS instances are running

the EC2 launch type and load balancing is required to distribute connections to the tasks. It is required that the

mapping of ports is performed dynamically and connections are routed to different groups of servers based on the path in

the URL.**


**Which AWS service should the Solutions Architect choose to fulfil these requirements?**


1: An Amazon ECS Service


2: Application Load Balancer


3: Network Load Balancer


4: Classic Load Balancer


**Answer: 2**


**Explanation:**


An ALB allows containers to use dynamic host port mapping so that multiple tasks from the same service are allowed on

the same container host. An ALB can also route requests based on the content of the request in the host field:

host-based or path-based.


The NLB and CLB types of Elastic Load Balancer do not support path-based routing or host-based routing so they cannot be

used for this use case.


- CORRECT "Application Load Balancer" is the correct answer.


- INCORRECT "ECS Services" is incorrect. An Amazon ECS service enables you to run and maintain a specified number of

  instances of a task definition simultaneously in an Amazon ECS cluster. It does not distributed connections to tasks.


- INCORRECT "Network Load Balancer" is incorrect as described above.


- INCORRECT "Classic Load Balancer" is incorrect as described above.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/dynamic-port-mapping-ecs/


https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-load-balancer-routing.html


**Save time with our exam-specific cheat sheets:**


```

Internet Client

```


```

HTTP, HTTPS

```


```

Application Load Balancer

```


```

Target Group 1 Target Group 2

```


```

Listener

```


```

Rule (default) Rule (/orders)

```


```

Instance 1 Instance 2 Instance 3 Instance 4

```


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

