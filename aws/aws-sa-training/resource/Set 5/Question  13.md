#### Question  13


**A company runs an API on a Linux server in their on-premises data center. The company are planning to migrate the API

to the AWS cloud. The company require a highly available, scalable and cost-effective solution. What should a Solutions

Architect recommend?**


1: Migrate the API to Amazon API Gateway and migrate the backend to Amazon EC2


2: Migrate the API server to Amazon EC2 instances in an Auto Scaling group and attach an Application Load Balancer


```

VPC

```


```

Private subnet

```


```

Public subnet

```


```

Customer

gateway

```


```

VPN gateway VPN connection

```


```

Corporate data center

```


```

Destination Target

192.168.0.0/ 16 vgw-id

```


```

Route Table

```


```

CIDR: 10. 0. 0. 0 / 16

```


```

CIDR: 192. 168. 0. 0 / 16

```


3: Migrate the API to Amazon API Gateway and use AWS Lambda as the backend


4: Migrate the API to Amazon CloudFront and use AWS Lambda as the origin


Answer: 3


**Explanation:**


The best option is to use a fully serverless solution. This will provide high availability, scalability and be cost-

effective. The components for this would be Amazon API Gateway for hosting the API and AWS Lambda for running the

backend.


As you can see in the image below, API Gateway can be the frontend for multiple backend services:


- CORRECT "Migrate the API to Amazon API Gateway and use AWS Lambda as the backend" is the correct answer.


- INCORRECT "Migrate the API to Amazon API Gateway and migrate the backend to Amazon EC2" is incorrect. This is a less

  available and cost-effective solution for the backend compared to AWS Lambda.


- INCORRECT "Migrate the API server to Amazon EC2 instances in an Auto Scaling group and attach an Application Load

  Balancer" is incorrect. Firstly, it may be difficult to load balance to an API. Additionally, this is a less

  cost-effective solution.


- INCORRECT "Migrate the API to Amazon CloudFront and use AWS Lambda as the origin" is incorrect. You cannot migrate an

  API to CloudFront. You can use CloudFront in front of API Gateway but that is not what this answer specifies.


**References:**


https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-

integration.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/

