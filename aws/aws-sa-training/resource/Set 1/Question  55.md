#### Question  55


**An application running on an external website is attempting to initiate a request to your company’s website using API

calls to Amazon API Gateway. A problem has been reported in which the requests are failing with an error that includes

the following text:**


**“Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource”**


**You have been asked to resolve the problem, what is the most likely solution?**


1: The IAM policy does not allow access to the API


2: The ACL on the API needs to be updated


3: The request is not secured with SSL/TLS


4: Enable CORS on the APIs resources using the selected methods under the API Gateway


Answer: 4


**Explanation:**


Cross-origin resource sharing (CORS) is a browser security feature that restricts cross-origin HTTP requests that are

initiated from scripts running in the browser. If your REST API's resources receive non-simple cross-origin HTTP

requests, you need to enable CORS support.


A _cross-origin_ HTTP request is one that is made to:


- A different _domain_ (for example, from example.com to amazondomains.com)

- A different _subdomain_ (for example, from example.com to petstore.example.com)

- A different _port_ (for example, from example.com to example.com:10777)

- A different _protocol_ (for example, from https://example.com to [http://example.com)](http://example.com))


To support CORS, therefore, a REST API resource needs to implement an OPTIONS method that can respond to the OPTIONS

preflight request with at least the following response headers mandated by the Fetch standard:


- Access-Control-Allow-Methods

- Access-Control-Allow-Headers

- Access-Control-Allow-Origin


- CORRECT "Enable CORS on the APIs resources using the selected methods under the API Gateway" is the correct answer.


- INCORRECT "The IAM policy does not allow access to the API" is incorrect. IAM policies are not used to control CORS

  and there is no ACL on the API to update.


- INCORRECT "The ACL on the API needs to be updated" is incorrect. There is no ACL on an API.


- INCORRECT "The request is not secured with SSL/TLS" is incorrect. This error would display whether using SSL/TLS or

  not.


**References:**


https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-api-gateway/

