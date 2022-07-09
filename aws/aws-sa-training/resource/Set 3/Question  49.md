#### Question  49


**You have implemented API Gateway and enabled a cache for a specific stage. How can you control the cache to enhance

performance and reduce load on back-end services?**


1: Configure the throttling feature


2: Enable bursting


3: Using time-to-live (TTL) settings


4: Using CloudFront controls


Answer: 3


**Explanation:**


You can enable API caching in Amazon API Gateway to cache your endpoint's responses. With caching, you can reduce the

number of calls made to your endpoint and also improve the latency of requests to your API.


When you enable caching for a stage, API Gateway caches responses from your endpoint for a specified time- to-live (TTL)

period, in seconds. API Gateway then responds to the request by looking up the endpoint response from the cache instead

of making a request to your endpoint. The default TTL value for API caching is 300 seconds. The maximum TTL value is

3600 seconds. TTL=0 means caching is disabled.


- CORRECT "Using time-to-live (TTL) settings" is the correct answer.


- INCORRECT "Configure the throttling feature" is incorrect. You can throttle and monitor requests to protect your

  back-end, but the cache is used to reduce the load on the back-end.


- INCORRECT "Enable bursting" is incorrect. Bursting isn’t an API Gateway feature that you can enable or disable.


- INCORRECT "Using CloudFront controls" is incorrect. CloudFront is a bogus answer as even though it does have a cache

  of its own it won’t help you to enhance the performance of the API Gateway cache.


**References:**


https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-api-gateway/

