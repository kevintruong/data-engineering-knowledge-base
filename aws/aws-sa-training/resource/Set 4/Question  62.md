#### Question  62


**An Amazon CloudWatch alarm recently notified a Solutions Architect that the load on an Amazon DynamoDB table is

getting close to the provisioned capacity for writes. The DynamoDB table is part of a two-tier customer-facing

application and is configured using provisioned capacity.**


**What will happen if the limit for the provisioned capacity for writes is reached?**


- [ ] The requests will be throttled, and fail with an HTTP 503 code (Service Unavailable)


- [ ] DynamoDB scales automatically so there’s no need to worry


- [x] The requests will be throttled, and fail with an HTTP 400 code (Bad Request) and a

ProvisionedThroughputExceededException


- [ ] The requests will succeed, and an HTTP 200 status code will be returned


*