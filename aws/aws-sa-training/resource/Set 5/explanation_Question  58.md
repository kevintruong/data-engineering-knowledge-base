*

**Explanation:**

The ECS container agent is included in the Amazon ECS optimized AMI and can also be installed on any EC2 instance that

supports the ECS specification (only supported on EC2 instances). Therefore, you don’t need to verify that the agent is

installed.

You need to verify that the installed agent is running and that the IAM instance profile has the necessary permissions

applied.

Troubleshooting steps for containers include:

* Verify that the Docker daemon is running on the container instance.

* Verify that the Docker Container daemon is running on the container instance.

* Verify that the container agent is running on the container instance.

* Verify that the IAM instance profile has the necessary permissions.

* ✅ :  "Verify that the IAM instance profile has the necessary permissions" is the correct answer.

* ✅ :  "Verify that the container agent is running on the container instances" is the correct answer.

* ❌ :  "Verify that the instances have the correct IAM group applied" is incorrect. You apply IAM roles

  (instance profile) to EC2 instances, not groups..

* ❌ :  "Verify that the container instances have the container agent installed" is incorrect as the ECS- optimized

  AMI has the agent included.

* ❌ :  "Verify that the container instances are using the Fargate launch type" is incorrect. This example is based

  on the EC2 launch type not the Fargate launch type. With Fargate the infrastructure is managed for you by AWS.

**References:**

<https://aws.amazon.com/premiumsupport/knowledge-center/ecs-agent-disconnected/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/>

----
* #ecs_container_agent #ec2_instances #ec2_instance #<https://aws.amazon.com/premiumsupport/knowledge-center/ecs-agent-disconnected/> #iam_instance_profile
