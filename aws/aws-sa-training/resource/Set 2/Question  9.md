#### Question  9


**A multi-tier application runs with eight front-end web servers in an Amazon EC2 Auto Scaling group in a single

Availability Zone behind an Application Load Balancer. A solutions architect needs to modify the infrastructure to be

highly available without modifying the application.**


**Which architecture should the solutions architect choose that provides high availability?**


1: Create an Auto Scaling group that uses four instances across each of two Regions


2: Modify the Auto Scaling group to use four instances across each of two Availability Zones


3: Create an Auto Scaling template that can be used to quickly create more instances in another Region


4: Create an Auto Scaling group that uses four instances across each of two subnets


Answer: 2


**Explanation:**


High availability can be enabled for this architecture quite simply by modifying the existing Auto Scaling group to use

multiple availability zones. The ASG will automatically balance the load so you don’t actually need to specify the

instances per AZ.


The architecture for the web tier will look like the one below:


- CORRECT "Modify the Auto Scaling group to use four instances across each of two Availability Zones" is the correct

  answer.


- INCORRECT "Create an Auto Scaling group that uses four instances across each of two Regions" is incorrect as EC2 Auto

  Scaling does not support multiple regions.


- INCORRECT "Create an Auto Scaling template that can be used to quickly create more instances in another Region" is

  incorrect as EC2 Auto Scaling does not support multiple regions.


- INCORRECT "Create an Auto Scaling group that uses four instances across each of two subnets" is incorrect as the

  subnets could be in the same AZ.


**References:**


https://aws.amazon.com/ec2/autoscaling/


**Save time with our exam-specific cheat sheets:**


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

Private subnet

```


```

Internet Client

HTTP, HTTPS

Availability Zone

Private subnet Public^ subnet

```


```

Application

Load

Balancer

```


```

Auto Scaling

group

```


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

