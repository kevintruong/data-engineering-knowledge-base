#### Question  62


**An Amazon CloudWatch alarm recently notified a Solutions Architect that the load on an Amazon DynamoDB table is

getting close to the provisioned capacity for writes. The DynamoDB table is part of a two-tier customer-facing

application and is configured using provisioned capacity.**


**What will happen if the limit for the provisioned capacity for writes is reached?**


1: The requests will be throttled, and fail with an HTTP 503 code (Service Unavailable)


2: DynamoDB scales automatically so there’s no need to worry


3: The requests will be throttled, and fail with an HTTP 400 code (Bad Request) and a

ProvisionedThroughputExceededException


4: The requests will succeed, and an HTTP 200 status code will be returned


**Answer: 3**


**Explanation:**


Amazon DynamoDB can throttle requests that exceed the provisioned throughput for a table. When a request is throttled it

fails with an HTTP 400 code (Bad Request) and a ProvisionedThroughputExceeded exception (not a 503 or 200 status code).


When using the provisioned capacity pricing model DynamoDB does not automatically scale. DynamoDB can automatically

scale when using the new on-demand capacity mode, however this is not configured for this database.


- CORRECT "The requests will be throttled, and fail with an HTTP 400 code (Bad Request) and a

  ProvisionedThroughputExceededException" is the correct answer.


- INCORRECT "The requests will be throttled, and fail with an HTTP 503 code (Service Unavailable)" is incorrect as this

  is not the code that is used (see above).


- INCORRECT "DynamoDB scales automatically so there’s no need to worry" is incorrect as provisioned capacity mode does

  not automatically scale.


- INCORRECT "The requests will succeed, and an HTTP 200 status code will be returned" is incorrect as the request will

  fail as described above.


**References:**


https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-

dynamodb/

