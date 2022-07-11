**Explanation:**

If you do not want to manage EC2 instances you must use the AWS Fargate launch type which is a serverless infrastructure

managed by AWS. Fargate only supports container images hosted on Elastic Container Registry

(ECR) or Docker Hub.

The following image articulates the key differences between EC2 Launch Type and Fargate:

- ✅ :  "Use the Elastic Container Service (ECS) with the Fargate Launch Type" is the correct answer.

- ✅ :  "Put your container images in the Elastic Container Registry (ECR)" is the correct answer.

- ❌ :  "Put your container images in a private repository" is incorrect. Private repositories are only supported by

  the EC2 Launch Type. The EC2 Launch Type allows you to run containers on EC2 instances that you manage.

- ❌ :  "Use the Elastic Container Service (ECS) with the EC2 Launch Type" is incorrect

- ❌ :  "Use CloudFront to deploy Docker on EC2" is incorrect. You cannot use CloudFront (a CDN) to deploy Docker on

  EC2.

**References:**

<https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ecs/>

----

- #<https://docs.aws.amazon.com/amazonecs/latest/developerguide/aws_fargate.html> #ec2_instances #elastic_container_service #aws_fargate_launch_type #elastic_container_registry
