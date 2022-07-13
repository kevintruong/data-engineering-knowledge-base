**Explanation:**

You can enable API caching in Amazon API Gateway to cache your endpoint's responses. With caching, you can reduce the

number of calls made to your endpoint and also improve the latency of requests to your API.

When you enable caching for a stage, API Gateway caches responses from your endpoint for a specified time- to-live (TTL)

period, in seconds. API Gateway then responds to the request by looking up the endpoint response from the cache instead

of making a request to your endpoint. The default TTL value for API caching is 300 seconds. The maximum TTL value is

3600 seconds. TTL=0 means caching is disabled.

- ✅ :  "Create a cache for a stage and configure a TTL" is the correct answer.

- ❌ :  "Create a cache for a method and configure a TTL" is incorrect. An API cache is not enabled for a method, it

  is enabled for a stage.

- ❌ :  "Configure an edge-optimized endpoint with CloudFront" is incorrect. This is the default endpoint type with

  API Gateway so there’s no reason to believe the solution architect needs to configure this. Users are

```

MyAPI

```

```

API Cache

```

```

Users Endpoint

```

```

CacheHitCountand

CacheMissCount

monitor the

optimization of the

cache

```

```

Latency measures the

overall responsiveness of

the API IntegrationLatency

measures the

responsiveness of the

backend

```

routed to the nearest CloudFront point of presence (POP). However, caching still takes place within API gateway using a

stage cache.

- ❌ :  "Configure a private endpoint place ElastiCache in front" is incorrect. You cannot use Amazon ElastiCache to

  cache API requests.

**References:**

<https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-api-gateway/

----

- #<https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html> #api_caching #api_cache #cache_api_requests #amazon_api_gateway
