**Explanation:**

Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache for DynamoDB that delivers up to

a 10x performance improvement – from milliseconds to microseconds – even at millions of requests per second. You can

enable DAX for a DynamoDB database with a few clicks.

```

ECS Service

```

```

ECS Container

instance

```

```

ECS Container

instance

```

```

Task Task Task Task

```

```

ECS EC 2 Cluster

ECS Service

```

```

Task Task Task Task

```

```

ECS Fargate Cluster

```

```

Registry:

ECR, Docker Hub, Self-hosted

Registry:

ECR, Docker Hub

```

```

EC 2 Launch Type

```

- You explicitly provision EC 2 instances

- You’re responsible for managing EC 2 instances

- Charged per running EC 2 instance

- EFS and EBS integration

- You handle cluster optimization

- More granular control over infrastructure

```

Fargate Launch Type

```

- Fargate automatically provisions resources

- Fargate provisions and manages compute

- Charged for running tasks

- No EFS and EBS integration

- Fargate handles cluster optimization

- Limited control, infrastructure is automated

- ✅ :  "Configure Amazon DAX" is the correct answer.

- ❌ :  "Enable read replicas" is incorrect. There is no such thing as read replicas with DynamoDB.

- ❌ :  "Configure DynamoDB Auto Scaling" is incorrect. DynamoDB auto scaling actively manages throughput capacity

  for tables and global secondary indexes so like provisioned throughput it does not provide the speed or in-memory

  capabilities requested.

- ❌ :  "Increase the provisioned throughput" is incorrect. Provisioned throughput is the maximum amount of capacity

  that an application can consume from a table or index, it doesn’t improve the speed of the database or add in-memory

  capabilities.

**References:**

<https://aws.amazon.com/dynamodb/dax/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- dynamodb/

----

- #amazon_dynamodb_accelerator #<https://aws.amazon.com/dynamodb/dax/> #dynamodb #configure_amazon_dax #dynamodb_database
