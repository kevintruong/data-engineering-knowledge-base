#### Question  44


**Some Amazon ECS containers are running on a cluster using the EC2 launch type. The current configuration uses the

container instance’s IAM roles for assigning permissions to the containerized applications.**


**A Solutions Architect needs to implement more granular permissions so that some applications can be assigned more

restrictive permissions. How can this be achieved?**


1: This cannot be changed as IAM roles can only be linked to container instances


2: This can be achieved using IAM roles for tasks, and splitting the containers according to the permissions required to

different task definition profiles


3: This can be achieved by configuring a resource-based policy for each application


4: This can only be achieved using the Fargate launch type


**Answer: 2**


**Explanation:**


With IAM roles for Amazon ECS tasks, you can specify an IAM role that can be used by the containers in a task. Using

this feature, you can achieve the required outcome by using IAM roles for tasks and splitting the containers according

to the permissions required to different task profiles.


- CORRECT "This can be achieved using IAM roles for tasks, and splitting the containers according to the permissions

  required to different task definition profiles" is the correct answer.


- INCORRECT "This cannot be changed as IAM roles can only be linked to container instances" is incorrect as you can also

  link them to tasks.


- INCORRECT "This can be achieved by configuring a resource-based policy for each application" is incorrect. Amazon ECS

  does not support IAM resource-based policies.


- INCORRECT "This can only be achieved using the Fargate launch type" is incorrect. The solution can be achieved whether

  using the EC2 or Fargate launch types.


**References:**


https://docs.aws.amazon.com/AmazonECS/latest/userguide/task-iam-roles.html


https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/

