#### Question  17


**A solutions architect is designing the infrastructure to run an application on Amazon EC2 instances. The application

requires high availability and must dynamically scale based on demand to be cost efficient.**


**What should the solutions architect do to meet these requirements?**


1: Configure an Application Load Balancer in front of an Auto Scaling group to deploy instances to multiple Regions


2: Configure an Amazon CloudFront distribution in front of an Auto Scaling group to deploy instances to multiple Regions


3: Configure an Application Load Balancer in front of an Auto Scaling group to deploy instances to multiple Availability

Zones


```

VPC

```


```

Private subnet

```


```

Public subnet

```


```

Default VPC

```


```

EC 2 Instance

```


```

Destination Target

pl-6ca 54005 (com.amazonaws.ap-southeast-2.s3, 54.231.248.0/22, 54.231.252.0/24, 52.95.128.0/21) vpce-ID

```


```

Route Table

```


```

DynamoDB Gateway

Endpoint

```


```

EC 2 Instance

Amazon DynamoDB

```


4: Configure an Amazon API Gateway API in front of an Auto Scaling group to deploy instances to multiple Availability

Zones


Answer: 3


**Explanation:**


The Amazon EC2-based application must be highly available and elastically scalable. Auto Scaling can provide the

elasticity by dynamically launching and terminating instances based on demand. This can take place across availability

zones for high availability.


Incoming connections can be distributed to the instances by using an Application Load Balancer (ALB).


- CORRECT "Configure an Application Load Balancer in front of an Auto Scaling group to deploy instances to multiple

  Availability Zones" is the correct answer.


- INCORRECT "Configure an Amazon API Gateway API in front of an Auto Scaling group to deploy instances to multiple

  Availability Zones" is incorrect as API gateway is not used for load balancing connections to Amazon EC2 instances.


- INCORRECT "Configure an Application Load Balancer in front of an Auto Scaling group to deploy instances to multiple

  Regions" is incorrect as you cannot launch instances in multiple Regions from a single Auto Scaling group.


- INCORRECT "Configure an Amazon CloudFront distribution in front of an Auto Scaling group to deploy instances to

  multiple Regions" is incorrect as you cannot launch instances in multiple Regions from a single Auto Scaling group.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html


https://aws.amazon.com/elasticloadbalancing/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

