**Explanation:**

IAM roles for ECS tasks enabled you to secure your infrastructure by assigning an IAM role directly to the ECS task

rather than to the EC2 container instance. This means you can have one task that uses a specific IAM role for access to

S3 and one task that uses an IAM role to access DynamoDB.

IAM roles can be specified at the container and task level on EC2 launch type and the task level on Fargate launch type.

- ✅ :  "IAM roles for tasks" is the correct answer.

- ❌ :  "IAM roles for EC2 instances" is incorrect. With IAM roles for EC2 instances you assign all of the IAM

  policies required by tasks in the cluster to the EC2 instances that host the cluster. This does not allow the secure

  separation requested.

- ❌ :  "IAM Instance Profile for EC2 instances" is incorrect. An instance profile is a container for an IAM role

  that you can use to pass role information to an EC2 instance when the instance starts. Again, this does not allow the

  secure separation requested.

- ❌ :  "Network ACL" is incorrect. Network ACLs are applied at the subnet level and would not assist here.

**References:**

```

ECS Service

ECS Container instance

```

```

ECS EC 2 Cluster

```

```

IAM Task Role

```

```

Task

```

```

IAM Instance Role

```

```

ECS Service

```

```

ECS Fargate Cluster

```

```

IAM Task Role

```

```

Task

```

<https://aws.amazon.com/blogs/compute/help-secure-container-enabled-applications-with-iam-roles-for-ecs>- tasks/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/>

----

- #<https://aws.amazon.com/blogs/compute/help-secure-container-enabled-applications-with-iam-roles-for-ecs>-_tasks/> #iam_instance_role #ecs_tasks #specific_iam_role #iam_task_role
