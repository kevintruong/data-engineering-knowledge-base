**Explanation:**

This is a good use case for CloudFront. CloudFront is a content delivery network (CDN) that caches content closer to

users. You can cache the static content on CloudFront using the EC2 instances as origins for the content. This will

improve performance (as the content is closer to the users) and reduce the need for the ASG to scale (as you don’t need

the processing power of the EC2 instances to serve the static content).

- ✅ :  "Create an Amazon CloudFront distribution for the site and redirect user traffic to the distribution"

  is the correct answer.

- ❌ :  "Store the contents on Amazon EFS instead of the EC2 root volume" is incorrect. Using EFS instead of the EC2

  root volume does not solve either problem.

- ❌ :  "Implement Amazon Redshift to create a repository of the content closer to the users" is incorrect. RedShift

  cannot be used to create content repositories to get content closer to users, it’s a data warehouse used for

  analytics.

- ❌ :  "Re-deploy the application in a new VPC that is closer to the users making the requests" is incorrect.

  Re-deploying the application in a VPC closer to the users may reduce latency (and therefore improve performance), but

  it doesn’t solve the problem of reducing the need for the ASG to scale.

**References:**

<https://aws.amazon.com/caching/cdn/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #amazon_cloudfront_distribution #cloudfront #amazon_efs #ec2_instances #<https://aws.amazon.com/caching/cdn/>
