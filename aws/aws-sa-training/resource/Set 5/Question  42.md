#### Question  42


**A new financial platform has been re-architected to use Docker containers in a micro-services architecture. The new

architecture will be implemented on AWS and a Solutions Architect must recommend the solution configuration. For

operational reasons, it will be necessary to access the operating system of the instances on which the containers run.**


**Which solution delivery option should the Architect select?**


1: ECS with the EC2 launch type


2: EKS with Kubernetes managed infrastructure


3: ECS with the Fargate launch type


4: ECS with a default cluster


**Answer: 1**


**Explanation:**


Amazon Elastic Container Service (ECS) is a highly scalable, high performance container management service that supports

Docker containers and allows you to easily run applications on a managed cluster of Amazon EC2 instances


The EC2 Launch Type allows you to run containers on EC2 instances that you manage so you will be able to access the

operating system instances.


- CORRECT "ECS with the EC2 launch type" is the correct answer.


- INCORRECT "EKS with Kubernetes managed infrastructure" is incorrect. The EKS service is a managed Kubernetes service

  that provides a fully-managed control plane so you would not have access to the EC2 instances that the platform runs

  on.


- INCORRECT "ECS with the Fargate launch type" is incorrect. The Fargate Launch Type is a serverless infrastructure

  managed by AWS so you do not have access to the operating system of the EC2 instances that the container platform runs

  on.


- INCORRECT "ECS with a default cluster" is incorrect. You need to choose the launch type to ensure you get the access

  required, not the cluster configuration.


**References:**


https://aws.amazon.com/ecs/features/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/

