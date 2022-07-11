**Explanation:**

Per-client throttling limits are applied to clients that use API keys associated with your usage policy as client

identifier. This can be applied to the single customer that is issuing excessive API requests. This is the best option

to ensure that only one customer is affected.

In the diagram below, per-client throttling limits are set in a usage plan:

- ✅ :  "Configure per-client throttling limits" is the correct answer.

- ❌ :  "Configure a server-side throttling limit" is incorrect. Server-side throttling limits are applied across

  all clients. These limit settings exist to prevent your API—and your account—from being overwhelmed by too many

  requests. In this case, the solutions architect need to apply the throttling to a single client.

- ❌ :  "Configure the per-method throttling limits" is incorrect. Per-method throttling limits apply to all

  customers using the same method. This will affect all customers who are using the API.

- ❌ :  "Configure the account-level throttling limits" is incorrect. Account-level throttling limits define the

  maximum steady-state request rate and burst limits for the account. This does not apply to individual customers.

**References:**

<https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-api-gateway/

```

THROTTLING: ENABLED

```

- RATE 10000

- BURST 5000 QUOTA: ENABLED

- REQUESTS/M 1 , 000 , 000

```

MyAPI

```

```

Premium Users Endpoint

```

```

Can also configure per-

method throttling limits

```

```

Usage Plans

```

```

Basic

```

```

Premium

```

```

THROTTLING: ENABLED

```

- RATE 5000

- BURST 2500 QUOTA: ENABLED

- REQUESTS/M 500 , 000

```

API Key

```

```

Production v 2 Stage

```

```

Production v 1 Stage

```

```

Endpoint

```

```

Users connect to

specific public endpoint

with API key that is

configured in a usage

plan

```

```

Basic Users

```

```

API Key

```

----

- #client_throttling_limits #<https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html> #level_throttling_limits #side_throttling_limits #throttling_limits
