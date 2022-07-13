*

**Explanation:**

With IAM roles for Amazon ECS tasks, you can specify an IAM role that can be used by the containers in a task. Using

this feature, you can achieve the required outcome by using IAM roles for tasks and splitting the containers according

to the permissions required to different task profiles.

* ✅ :  "This can be achieved using IAM roles for tasks, and splitting the containers according to the permissions

  required to different task definition profiles" is the correct answer.

* ❌ :  "This cannot be changed as IAM roles can only be linked to container instances" is incorrect as you can also

  link them to tasks.

* ❌ :  "This can be achieved by configuring a resource-based policy for each application" is incorrect. Amazon ECS

  does not support IAM resource-based policies.

* ❌ :  "This can only be achieved using the Fargate launch type" is incorrect. The solution can be achieved whether

  using the EC2 or Fargate launch types.

**References:**

<https://docs.aws.amazon.com/AmazonECS/latest/userguide/task-iam-roles.html>

<https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/>

----
* #<https://docs.aws.amazon.com/amazonecs/latest/userguide/task-iam-roles.html> #amazon_ecs_tasks #<https://docs.aws.amazon.com/iam/latest/userguide/reference_aws-services-that-work-with-iam.html_>> #iam_roles #iam_role
