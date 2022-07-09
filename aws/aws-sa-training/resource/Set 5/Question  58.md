#### Question  58


**An application you manage runs a number of components using a micro-services architecture. Several ECS container

instances in your ECS cluster are displaying as disconnected. The ECS instances were created from the Amazon

ECS-Optimized AMI. What steps might you take to troubleshoot the issue? (Select TWO)**


1: Verify that the instances have the correct IAM group applied


2: Verify that the container instances have the container agent installed


3: Verify that the IAM instance profile has the necessary permissions


4: Verify that the container agent is running on the container instances


5: Verify that the container instances are using the Fargate launch type


**Answer: 3,4**


**Explanation:**


The ECS container agent is included in the Amazon ECS optimized AMI and can also be installed on any EC2 instance that

supports the ECS specification (only supported on EC2 instances). Therefore, you don’t need to verify that the agent is

installed.


You need to verify that the installed agent is running and that the IAM instance profile has the necessary permissions

applied.


Troubleshooting steps for containers include:


- Verify that the Docker daemon is running on the container instance.

- Verify that the Docker Container daemon is running on the container instance.

- Verify that the container agent is running on the container instance.

- Verify that the IAM instance profile has the necessary permissions.


- CORRECT "Verify that the IAM instance profile has the necessary permissions" is the correct answer.


- CORRECT "Verify that the container agent is running on the container instances" is the correct answer.


- INCORRECT "Verify that the instances have the correct IAM group applied" is incorrect. You apply IAM roles

  (instance profile) to EC2 instances, not groups..


- INCORRECT "Verify that the container instances have the container agent installed" is incorrect as the ECS- optimized

  AMI has the agent included.


- INCORRECT "Verify that the container instances are using the Fargate launch type" is incorrect. This example is based

  on the EC2 launch type not the Fargate launch type. With Fargate the infrastructure is managed for you by AWS.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/ecs-agent-disconnected/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/

