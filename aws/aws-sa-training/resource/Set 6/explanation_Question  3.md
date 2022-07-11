**Explanation:**

AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.

Lambda has a maximum execution time of 900 seconds and memory can be allocated up to 3008 MB. Therefore, the most

cost-effective solution will be AWS Lambda.

- ✅ :  "AWS Lambda functions" is the correct answer.

- ❌ :  "AWS Fargate tasks" is incorrect. Fargate runs Docker containers and is serverless. However, you do pay for

  the running time of the tasks so it will not be as cost-effective.

- ❌ :  "Amazon EC2 spot instances" is incorrect. EC2 instances must run continually waiting for jobs to process so

  even with spot this would be less cost-effective (and subject to termination).

- ❌ :  "Amazon Elastic Beanstalk" is incorrect. This services also relies on Amazon EC2 instances so would not be

  as cost-effective.

**References:**

<https://aws.amazon.com/lambda/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/>

----

- #aws_lambda #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/> #aws_lambda_functions #aws_fargate_tasks #amazon_ec2_spot_instances
