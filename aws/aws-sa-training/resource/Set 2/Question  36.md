#### Question  36


**You would like to grant additional permissions to an individual ECS application container on an ECS cluster that you

have deployed. You would like to do this without granting additional permissions to the other containers that are

running on the cluster.**


**How can you achieve this?**


1: Create a separate Task Definition for the application container that uses a different Task Role


2: In the same Task Definition, specify a separate Task Role for the application container


3: Use EC2 instances instead as you can assign different IAM roles on each instance


4: You cannot implement granular permissions with ECS containers


Answer: 1


**Explanation:**


You can only apply one IAM role to a Task Definition so you must create a separate Task Definition. A Task Definition is

required to run Docker containers in Amazon ECS and you can specify the IAM role (Task Role)

that the task should use for permissions.


With the EC2 launch type you can apply IAM roles at the container and task level, whereas with Fargate you can only

apply at the task level. This is depicted in the diagram below:


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


- CORRECT "Create a separate Task Definition for the application container that uses a different Task Role" is the

  correct answer.


- INCORRECT "In the same Task Definition, specify a separate Task Role for the application container" is incorrect as

  int this case a separate task definition should be created to avoid granting the permissions to other containers

  running on the cluster.


- INCORRECT "Use EC2 instances instead as you can assign different IAM roles on each instance" is incorrect. You can

  apply different IAM roles to different EC2 instances, but to grant permissions to ECS application containers you must

  use Task Definitions and Task Roles.


- INCORRECT "You cannot implement granular permissions with ECS containers" is incorrect. It is incorrect to say that

  you cannot implement granular permissions with ECS containers as IAM roles are granular and are applied through Task

  Definitions/Task Roles.


**References:**


https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/

