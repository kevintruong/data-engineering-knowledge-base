#### Question  37


**The development team in your company has created a new application that you plan to deploy on AWS which runs multiple

components in Docker containers. You would prefer to use AWS managed infrastructure for running the containers as you do

not want to manage EC2 instances.**


**Which of the below solution options would deliver these requirements? (Select TWO)**


1: Use the Elastic Container Service (ECS) with the Fargate Launch Type


2: Put your container images in a private repository


3: Use the Elastic Container Service (ECS) with the EC2 Launch Type


4: Use CloudFront to deploy Docker on EC2


5: Put your container images in the Elastic Container Registry (ECR)


Answer: 1,5


**Explanation:**


If you do not want to manage EC2 instances you must use the AWS Fargate launch type which is a serverless infrastructure

managed by AWS. Fargate only supports container images hosted on Elastic Container Registry

(ECR) or Docker Hub.


The following image articulates the key differences between EC2 Launch Type and Fargate:


- CORRECT "Use the Elastic Container Service (ECS) with the Fargate Launch Type" is the correct answer.


- CORRECT "Put your container images in the Elastic Container Registry (ECR)" is the correct answer.


- INCORRECT "Put your container images in a private repository" is incorrect. Private repositories are only supported by

  the EC2 Launch Type. The EC2 Launch Type allows you to run containers on EC2 instances that you manage.


- INCORRECT "Use the Elastic Container Service (ECS) with the EC2 Launch Type" is incorrect


- INCORRECT "Use CloudFront to deploy Docker on EC2" is incorrect. You cannot use CloudFront (a CDN) to deploy Docker on

  EC2.


**References:**


https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/

