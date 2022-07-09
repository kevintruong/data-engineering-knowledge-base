#### Question  51


**A DynamoDB database you manage is randomly experiencing heavy read requests that are causing latency. What is the

simplest way to alleviate the performance issues?**


1: Create DynamoDB read replicas


2: Enable EC2 Auto Scaling for DynamoDB


3: Create an ElastiCache cluster in front of DynamoDB


4: Enable DynamoDB DAX


Answer: 4


**Explanation:**


DynamoDB offers consistent single-digit millisecond latency. However, DynamoDB + DAX further increases performance with

response times in microseconds for millions of requests per second for read-heavy workloads.


The DAX cache uses cluster nodes running on Amazon EC2 instances and sits in front of the DynamoDB table as you can see

in the diagram below:


- CORRECT "Enable DynamoDB DAX" is the correct answer.


- INCORRECT "Create DynamoDB read replicas" is incorrect. There’s no such thing as DynamoDB Read Replicas

  (Read Replicas are an RDS concept).


- INCORRECT "Enable EC2 Auto Scaling for DynamoDB" is incorrect. You cannot use EC2 Auto Scaling with DynamoDB. You can

  use Application Auto Scaling to scales DynamoDB but as the spikes in read traffic are random and Auto Scaling needs

  time to adjust the capacity of the DB it wouldn’t be as responsive as using DynamoDB DAX.


- INCORRECT "Create an ElastiCache cluster in front of DynamoDB" is incorrect. ElastiCache in front of DynamoDB is not

  the best answer as DynamoDB DAX is a simpler implementation and provides the required performance improvements.


**References:**


https://aws.amazon.com/dynamodb/dax/


**Save time with our exam-specific cheat sheets:**


```

Amazon DynamoDB

```


```

DAX EC 2 Instance

```


```

IAM Role

```


```

VPC

```


```

IAM Role

```


```

Permissions:

```


- Access DynamoDB + DAX


```

Permissions:

```


- Access DynamoDB


```

Security group

```


```

Inbound rules:

```


- TCP 8000 (DynamoDB) from 0. 0. 0. 0 / 0

- TCP 8111 (DAX) from 0. 0. 0. 0 / 0


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/

