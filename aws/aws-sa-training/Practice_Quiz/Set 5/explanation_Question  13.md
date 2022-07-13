**Explanation:**

The best option is to use a fully serverless solution. This will provide high availability, scalability and be cost-

effective. The components for this would be Amazon API Gateway for hosting the API and AWS Lambda for running the

backend.

As you can see in the image below, API Gateway can be the frontend for multiple backend services:

- ✅ :  "Migrate the API to Amazon API Gateway and use AWS Lambda as the backend" is the correct answer.

- ❌ :  "Migrate the API to Amazon API Gateway and migrate the backend to Amazon EC2" is incorrect. This is a less

  available and cost-effective solution for the backend compared to AWS Lambda.

- ❌ :  "Migrate the API server to Amazon EC2 instances in an Auto Scaling group and attach an Application Load

  Balancer" is incorrect. Firstly, it may be difficult to load balance to an API. Additionally, this is a less

  cost-effective solution.

- ❌ :  "Migrate the API to Amazon CloudFront and use AWS Lambda as the origin" is incorrect. You cannot migrate an

  API to CloudFront. You can use CloudFront in front of API Gateway but that is not what this answer specifies.

**References:**

<https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda>- integration.html

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/>

----

- #<https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda>-_integration.html> #aws_lambda #amazon_api_gateway #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/> #api_gateway
