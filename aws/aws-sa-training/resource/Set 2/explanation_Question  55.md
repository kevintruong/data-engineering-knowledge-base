**Explanation:**

The API does not receive a high volume of traffic or require extremely low latency. It would not be cost efficient to

use multiple EC2 instances and Elastic Load Balancers. Instead the best course of action would be to recreate the API

using API Gateway which will allow the customer to only pay for what they use. AWS Lambda can likewise be used for the

back-end processing reducing cost by utilizing a pay for what you use serverless service.

- ✅ :  "Recreate the API using API Gateway and use AWS Lambda as the service back-end" is the correct answer.

- ❌ :  "Create an Auto Scaling group with a minimum of one instance and a maximum of two instances, then use an

  Application Load Balancer to balance the traffic" is incorrect. Using Application Load Balancers with multiple EC2

  instances would not be cost effective.

- ❌ :  "Create an Auto Scaling group with a maximum of two instances, then use an Application Load Balancer to

  balance the traffic" is incorrect as this is not the lowest cost option.

- ❌ :  "Recreate the API using API Gateway and integrate the API with the existing back-end" is incorrect. If the

  architect recreates the API using API Gateway but integrates the API with the existing back-end this is not highly

  available and is not the lowest cost option.

**References:**

<https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda>- integration.html

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-api-gateway/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-lambda/>

----

- #aws_lambda #<https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda>-_integration.html> #elastic_load_balancers #multiple_ec2 #multiple_ec2_instances
