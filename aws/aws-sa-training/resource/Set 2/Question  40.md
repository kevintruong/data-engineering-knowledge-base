#### Question  40


**A mobile client requires data from several application-layer services to populate its user interface. What can the

application team use to decouple the client interface from the underlying services behind them?**


1: AWS Device Farm


2: Amazon Cognito


3: Amazon API Gateway


4: Application Load Balancer


Answer: 3


**Explanation:**


Amazon API Gateway decouples the client application from the back-end application-layer services by providing a single

endpoint for API requests.


The architecture of API Gateway is depicted in the diagram below:


- CORRECT "Amazon API Gateway" is the correct answer.


- INCORRECT "AWS Device Farm" is incorrect. AWS Device farm is an app testing service for Android, iOS and web apps.


- INCORRECT "Amazon Cognito" is incorrect. Amazon Cognito is used for adding sign-up, sign-in and access control to

  mobile apps.


- INCORRECT "Application Load Balancer" is incorrect. An application load balancer distributes incoming connection

  requests to back-end EC2 instances. It is not used for decoupling application-layer services from mobile clients.


**References:**


https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-api-gateway/

