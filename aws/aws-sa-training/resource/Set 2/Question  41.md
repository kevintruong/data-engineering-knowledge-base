#### Question  41


**A Solutions Architect is designing a web application that runs on Amazon EC2 instances behind an Elastic Load

Balancer. All data in transit must be encrypted.**


**Which solution options meet the encryption requirement? (Select TWO)**


1: Use a Network Load Balancer (NLB) with a TCP listener, then terminate SSL on EC2 instances


2: Use an Application Load Balancer (ALB) with an HTTPS listener, then install SSL certificates on the ALB and EC2

instances


3: Use an Application Load Balancer (ALB) in passthrough mode, then terminate SSL on EC2 instances


```

AWS Lambda

```


```

Region

```


```

Amazon API Gateway

```


```

Mobile

client

```


```

Service

```


```

Website

```


```

Internet

```


```

VPC

```


```

Any other AWS service

```


```

REST API over

HTTPS

```


```

Public subnet

```


```

Private subnet

```


```

Lambda function

```


```

EC 2 Instance

```


```

Application Load Balancer

```


```

EC 2 Instance

```


```

Any public endpoint

```


4: Use a Network Load Balancer (NLB) with an HTTPS listener, then install SSL certificates on the NLB and EC2 instances


5: Use an Application Load Balancer (ALB) with a TCP listener, then terminate SSL on EC2 instances


Answer: 1,2


**Explanation:**


You can passthrough encrypted traffic with an NLB and terminate the SSL on the EC2 instances, so this is a valid answer.


You can use a HTTPS listener with an ALB and install certificates on both the ALB and EC2 instances. This does not use

passthrough, instead it will terminate the first SSL connection on the ALB and then re-encrypt the traffic and connect

to the EC2 instances.


- CORRECT "Use a Network Load Balancer (NLB) with a TCP listener, then terminate SSL on EC2 instances" is the correct

  answer.


- CORRECT "Use an Application Load Balancer (ALB) with an HTTPS listener, then install SSL certificates on the ALB and

  EC2 instances" is the correct answer.


- INCORRECT "Use an Application Load Balancer (ALB) in passthrough mode, then terminate SSL on EC2 instances" is

  incorrect. You cannot use passthrough mode with an ALB and terminate SSL on the EC2 instances.


- INCORRECT "Use a Network Load Balancer (NLB) with an HTTPS listener, then install SSL certificates on the NLB and EC2

  instances" is incorrect. You cannot use a HTTPS listener with an NLB.


- INCORRECT "Use an Application Load Balancer (ALB) with a TCP listener, then terminate SSL on EC2 instances"

  is incorrect. You cannot use a TCP listener with an ALB.


**References:**


https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

