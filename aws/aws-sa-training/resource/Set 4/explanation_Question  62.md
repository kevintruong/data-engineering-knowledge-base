*

**Explanation:**

Amazon DynamoDB can throttle requests that exceed the provisioned throughput for a table. When a request is throttled it

fails with an HTTP 400 code (Bad Request) and a ProvisionedThroughputExceeded exception (not a 503 or 200 status code).

When using the provisioned capacity pricing model DynamoDB does not automatically scale. DynamoDB can automatically

scale when using the new on-demand capacity mode, however this is not configured for this database.

* ✅ :  "The requests will be throttled, and fail with an HTTP 400 code (Bad Request) and a

  ProvisionedThroughputExceededException" is the correct answer.

* ❌ :  "The requests will be throttled, and fail with an HTTP 503 code (Service Unavailable)" is incorrect as this

  is not the code that is used (see above).

* ❌ :  "DynamoDB scales automatically so there’s no need to worry" is incorrect as provisioned capacity mode does

  not automatically scale.

* ❌ :  "The requests will succeed, and an HTTP 200 status code will be returned" is incorrect as the request will

  fail as described above.

**References:**

<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- dynamodb/

----
* #capacity_pricing_model_dynamodb #amazon_dynamodb #dynamodb #<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming.errors.html> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>>-
