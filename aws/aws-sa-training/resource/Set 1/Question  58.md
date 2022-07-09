#### Question  58


**An organization in the health industry needs to create an application that will transmit protected health data to

thousands of service consumers in different AWS accounts. The application servers run on EC2 instances in private VPC

subnets. The routing for the application must be fault tolerant.**


**What should be done to meet these requirements?**


1: Create a virtual private gateway connection between each pair of service provider VPCs and service consumer VPCs


2: Create a proxy server in the service provider VPC to route requests from service consumers to the application servers


```

Amazon Simple Queue

Service

```


```

Queue

```


```

EC 2 instance

polls SQS

```


```

Web Tier

```


```

Auto Scaling Group

```


```

App Tier

```


```

Auto Scaling Group

Decoupled integration

```


3: Create a VPC endpoint service and grant permissions to specific service consumers to create a connection


4: Create an internal Application Load Balancer in the service provider VPC and put application servers behind it


Answer: 3


**Explanation:**


What you need to do here is offer the service through a service provider offering. This is a great use case for a VPC

endpoint service using AWS PrivateLink (referred to as an endpoint service). Other AWS principals can then create a

connection from their VPC to your endpoint service using an interface VPC endpoint.


You are acting as the service provider and offering the service to service consumers. This configuration uses a Network

Load Balancer and can be fault tolerant by configuring multiple subnets in which the EC2 instances are running.


The following diagram depicts a similar architecture:


- CORRECT "Create a VPC endpoint service and grant permissions to specific service consumers to create a connection"

  is the correct answer.


- INCORRECT "Create a virtual private gateway connection between each pair of service provider VPCs and service consumer

  VPCs" is incorrect. Creating a virtual private gateway connection between each pair of service provider VPCs and

  service consumer VPCs would be extremely cumbersome and is not the best option.


- INCORRECT "Create a proxy server in the service provider VPC to route requests from service consumers to the

  application servers" is incorrect. Using a proxy service is possible but would not scale as well and would present a

  single point of failure unless there is some load balancing to multiple proxies (not mentioned).


- INCORRECT "Create an internal Application Load Balancer in the service provider VPC and put application servers behind

  it" is incorrect. Creating an internal ALB would not work as you need consumers from outside your VPC to be able to

  connect.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/
