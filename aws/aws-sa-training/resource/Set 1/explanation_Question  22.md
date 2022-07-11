**Explanation:**

To specify permissions for a specific task on Amazon ECS you should use IAM Roles for Tasks. The permissions policy can

be applied to tasks when creating the task definition, or by using an IAM task role override using the AWS CLI or SDKs.

The _taskRoleAr_ n parameter is used to specify the policy.

- ✅ :  "Create an IAM policy with permissions to DynamoDB and assign It to a task using the _taskRoleArn_

  parameter" is the correct answer.

- ❌ :  "Create an IAM policy with permissions to DynamoDB and attach it to the container instance" is incorrect.

  You should not apply the permissions to the container instance as they will then apply to all tasks running on the

  instance as well as the instance itself.

- ❌ :  "Use a security group to allow outbound connections to DynamoDB and assign it to the container instance"

  is incorrect. Though you will need a security group to allow outbound connections to DynamoDB, the

question is asking how to assign permissions to write data to DynamoDB and a security group cannot provide those

permissions.

- ❌ :  "Modify the _AmazonECSTaskExecutionRolePolicy_ policy to add permissions for DynamoDB" is incorrect. The _

  AmazonECSTaskExecutionRolePolicy_ policy is the Task Execution IAM Role. This is used by the container agent to be

  able to pull container images, write log file etc.

**References:**

<https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/>

----

- #task_execution_iam_role #iam_task_role_override #aws_cli #dynamodb #iam_roles
