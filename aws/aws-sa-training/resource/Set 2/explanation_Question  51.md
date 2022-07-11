**Explanation:**

DynamoDB offers consistent single-digit millisecond latency. However, DynamoDB + DAX further increases performance with

response times in microseconds for millions of requests per second for read-heavy workloads.

The DAX cache uses cluster nodes running on Amazon EC2 instances and sits in front of the DynamoDB table as you can see

in the diagram below:

- ✅ :  "Enable DynamoDB DAX" is the correct answer.

- ❌ :  "Create DynamoDB read replicas" is incorrect. There’s no such thing as DynamoDB Read Replicas

  (Read Replicas are an RDS concept).

- ❌ :  "Enable EC2 Auto Scaling for DynamoDB" is incorrect. You cannot use EC2 Auto Scaling with DynamoDB. You can

  use Application Auto Scaling to scales DynamoDB but as the spikes in read traffic are random and Auto Scaling needs

  time to adjust the capacity of the DB it wouldn’t be as responsive as using DynamoDB DAX.

- ❌ :  "Create an ElastiCache cluster in front of DynamoDB" is incorrect. ElastiCache in front of DynamoDB is not

  the best answer as DynamoDB DAX is a simpler implementation and provides the required performance improvements.

**References:**

<https://aws.amazon.com/dynamodb/dax/>

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

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- dynamodb/

----

- #scales_dynamodb #dynamodb_dax #dynamodb_read_replicas #amazon_dynamodb #<https://aws.amazon.com/dynamodb/dax/>
