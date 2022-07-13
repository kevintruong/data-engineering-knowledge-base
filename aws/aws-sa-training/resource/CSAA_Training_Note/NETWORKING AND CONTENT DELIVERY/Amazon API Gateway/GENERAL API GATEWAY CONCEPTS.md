#### GENERAL API GATEWAY CONCEPTS


An Amazon API Gateway is a collection of resources and methods that are integrated with back-end HTTP endpoints, Lambda

functions or other AWS services.


API Gateway is a fully managed service that makes it easy for developers to publish, maintain, monitor, and secure APIs

at any scale.


API Gateway provides developers with a simple, flexible, fully managed, pay-as-you-go service that handles all aspects

of creating and operating robust APIs for application back ends.


API Gateway handles all of the tasks involved in accepting and processing up to hundreds of thousands of concurrent API

calls.


API calls include traffic management, authorization and access control, monitoring, and API version management.


Together with Lambda, API Gateway forms the app-facing part of the AWS serverless infrastructure.


Back-end services include Amazon EC2, AWS Lambda or any web application (public or private endpoints).


CloudFront is used as the public endpoint for API Gateway.


Supports API keys and Usage Plans for user identification, throttling or quota management.


Using CloudFront behind the scenes, custom domains, and SNI are supported.


Can be published as products and monetized on AWS Marketplace.


Collections can be deployed in stages.


Permissions to invoke a method are granted using IAM roles and policies or API Gateway custom authorizers.


An API can present a certificate to be authenticated by the back-end.


All of the APIs created with Amazon API Gateway expose HTTPS endpoints only (does not support unencrypted endpoints).


By default, API Gateway assigns an internal domain that automatically uses the API Gateway certificates.


When configuring your APIs to run under a custom domain name you can provide your own certificate.


Supported data formats include JSON, XML, query string parameters, and request headers.


**Can enable Cross Origin Resource Sharing (CORS) for multiple domain use with Javascript/AJAX:**


- Can be used to enable requests from domains other than the APIs domain.

- Allows the sharing of resources between different domains.



- The method (GET, PUT, POST etc) for which you will enable CORS must be available in the API Gateway API before you

  enable CORS.

- If CORS is not enabled and an API resource received requests from another domain the request will be blocked.

- Enable CORS on the APIs resources using the selected methods under the API Gateway.


**Data types used with API Gateway:**


- Any payload sent over HTTP (always encrypted over HTTPS).

- Data formats include JSON, XML, query string parameters and request headers.

- You can declare any content type for your APIs responses, and then use the transform templates to change the back-end

  response into your desired format.


You can add caching to API calls by provisioning an Amazon API Gateway cache and specifying its size in gigabytes.

