#### Question  43


**A new application runs on Amazon EC2 instances and uses API Gateway and AWS Lambda. The company is planning on running

an advertising campaign that will likely result in significant hits to the application after each ad is run.**


**A Solutions Architect is concerned about the impact this may have on the application and would like to put in place

some controls to limit the number of requests per second that hit the application.**


**What controls should the Solutions Architect implement?**


1: Implement throttling rules on the API Gateway


2: Enable caching on the API Gateway and specify a size in gigabytes


3: Enable Lambda continuous scaling


4: API Gateway and Lambda scale automatically to handle any load so there’s no need to implement controls


**Answer: 1**


**Explanation:**


The key requirement is to limit the number of requests per second that hit the application. This can only be done by

implementing throttling rules on the API Gateway. Throttling enables you to throttle the number of requests to your API

which in turn means less traffic will be forwarded to your application server.


- CORRECT "Implement throttling rules on the API Gateway" is the correct answer.


- INCORRECT "Enable caching on the API Gateway and specify a size in gigabytes" is incorrect. Caching can improve

  performance but does not limit the amount of requests coming in.


- INCORRECT "Enable Lambda continuous scaling" is incorrect. Lambda continuous scaling does not resolve the scalability

  concerns with the EC2 application server.


- INCORRECT "API Gateway and Lambda scale automatically to handle any load so there’s no need to implement controls"

  is incorrect. API Gateway and Lambda both scale up to their default limits however the


bottleneck is with the application server running on EC2 which may not be able to scale to keep up with demand.


**References:**


https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-api-gateway/

