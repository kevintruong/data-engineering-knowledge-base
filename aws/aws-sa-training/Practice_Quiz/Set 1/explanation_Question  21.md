**Explanation:**

```

Region

```

```

Availability

Zone

```

```

Availability

Zone

```

```

Availability

Zone

```

```

Writes Writes

```

```

Region

```

```

Availability

Zone

```

```

Availability

Zone

```

```

Availability

Zone

```

```

Asynchronous Reads Reads

replication

```

```

Primary Region Secondary Region

```

```

Aurora Global Database:

```

- Uses physical replication

- One secondary AWS region

- Uses dedicated infrastructure

- No impact on DB performance

- Good for disaster recovery

To add high availability to this architecture both the web tier and database tier require changes. For the web tier an

Auto Scaling group across multiple AZs with an ALB will ensure there are always instances running and traffic is being

distributed to them.

The database tier should be migrated from the EC2 instances to Amazon RDS to take advantage of a managed database with

Multi-AZ functionality. This will ensure that if there is an issue preventing access to the primary database a secondary

database can take over.

- ✅ :  "Create an Amazon EC2 Auto Scaling group and Application Load Balancer (ALB) spanning multiple AZs" is the

  correct answer.

- ✅ :  "Create new public and private subnets in the same VPC, each in a new AZ. Migrate the database to an Amazon

  RDS multi-AZ deployment" is the correct answer.

- ❌ :  "Create new public and private subnets in the same AZ for high availability" is incorrect as this would not

  add high availability.

- ❌ :  "Add the existing web application instances to an Auto Scaling group behind an Application Load Balancer (

  ALB)" is incorrect because the existing servers are in a single subnet. For HA we need to instances in multiple

  subnets.

- ❌ :  "Create new public and private subnets in a new AZ. Create a database using Amazon EC2 in one AZ" is

  incorrect because we also need HA for the database layer.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html>

<https://aws.amazon.com/rds/features/multi-az/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/>

----

- #secondary_aws_region #aurora_global_database #database_tier #<https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html> #high_availability
