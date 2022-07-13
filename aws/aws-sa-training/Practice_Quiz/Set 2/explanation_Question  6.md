**Explanation:**

Amazon CloudFront is a content delivery network (CDN) that improves website performance by caching content at edge

locations around the world. It can serve both dynamic and static content. This is the best solution for improving the

performance of the website.

- ✅ :  "Create an Amazon CloudFront distribution and configure the ALB as an origin. Then update the Amazon Route 53

  record to point to the CloudFront distribution" is the correct answer.

- ❌ :  "Create a latency-based Amazon Route 53 record for the ALB. Then launch new EC2 instances with larger

  instance sizes and register the instances with the ALB" is incorrect. Latency routing routes based on the latency

  between the client and AWS. There is no mention in the answer about creating the new instances in another region

  therefore the only advantage is in using larger instance sizes. For a dynamic site this adds complexity in keeping the

  instances in sync.

- ❌ :  "Launch new EC2 instances hosting the same web application in different Regions closer to the users. Use an

  AWS Transit Gateway to connect customers to the closest region" is incorrect as Transit Gateway is a service for

  connecting on-premises networks and VPCs to a single gateway.

- ❌ :  "Migrate the website to an Amazon S3 bucket in the Regions closest to the users. Then create an Amazon Route

  53 geolocation record to point to the S3 buckets" is incorrect as with S3 you can only host static websites, not

  dynamic websites.

**References:**

<https://aws.amazon.com/cloudfront/dynamic-content/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #amazon_cloudfront #amazon_cloudfront_distribution #cloudfront_distribution #aws #amazon_route
