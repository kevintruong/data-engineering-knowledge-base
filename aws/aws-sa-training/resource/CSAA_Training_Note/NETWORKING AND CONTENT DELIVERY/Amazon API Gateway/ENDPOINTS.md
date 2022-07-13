#### ENDPOINTS


An _API endpoint_ type refers to the hostname of the API.


The API endpoint type can be _edge-optimized_ , _regional_ , or _private_ , depending on where the majority of your API

traffic originates from.


**Edge-Optimized Endpoint:**


- An edge-optimized API endpoint is best for geographically distributed clients. API requests are routed to the nearest

  CloudFront Point of Presence (POP). This is the default endpoint type for API Gateway REST APIs.

- Edge-optimized APIs capitalize the names of HTTP headers (for example, Cookie).

- CloudFront sorts HTTP cookies in natural order by cookie name before forwarding the request to your origin. For more

  information about the way CloudFront processes cookies, see Caching Content Based on Cookies.

- Any custom domain name that you use for an edge-optimized API applies across all regions.


**Regional Endpoint:**


- A regional API endpoint is intended for clients in the same region.

- When a client running on an EC2 instance calls an API in the same region, or when an API is intended to serve a small

  number of clients with high demands, a regional API reduces connection overhead.

- For a regional API, any custom domain name that you use is specific to the region where the API is deployed.

- If you deploy a regional API in multiple regions, it can have the same custom domain name in all regions.

- You can use custom domains together with Amazon Route 53 to perform tasks such as latency-based routing.

- Regional API endpoints pass all header names through as-is.


**Private Endpoint:**


- A private API endpoint is an API endpoint that can only be accessed from your Amazon


```

Virtual Private Cloud (VPC) using an interface VPC endpoint, which is an endpoint network

interface (ENI) that you create in your VPC.

```


- Private API endpoints pass all header names through as-is.


The following diagram depicts the three different Amazon API Gateway endpoint types:

