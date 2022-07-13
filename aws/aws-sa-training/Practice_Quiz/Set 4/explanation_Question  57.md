*

**Explanation:**

You can throttle and monitor requests to protect your backend. Resiliency through throttling rules based on the number

of requests per second for each HTTP method (GET, PUT). Throttling can be configured at multiple levels including Global

and Service Call.

When request submissions exceed the steady-state request rate and burst limits, API Gateway fails the limit- exceeding

requests and returns 429 Too Many Requests error responses to the client.

* ✅ :  "API Gateway fails the limit-exceeding requests and returns “429 Too Many Requests” error responses to the

  client" is the correct answer.

* ❌ :  "The requests will be buffered in a cache until the load reduces" is incorrect as the requests are actually

  failed.

* ❌ :  "API Gateway drops the requests and does not return a response to the client" is incorrect as it does return

  a response as detailed above.

* ❌ :  "API Gateway fails the limit-exceeding requests and returns “500 Internal Server Error” error responses to

  the client" is incorrect as a 429 error is returned.

**References:**

<https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-api-gateway/

----
* #<https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html> #api_gateway #many_requests_error_responses #many_requests #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>-
