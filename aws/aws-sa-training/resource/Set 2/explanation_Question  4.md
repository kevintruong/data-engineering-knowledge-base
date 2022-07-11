**Explanation:**

Using Amazon CloudFront as the front-end provides the option to specify a custom message instead of the default message.

To specify the specific file that you want to return and the errors for which the file should be returned, you update

your CloudFront distribution to specify those values.

For example, the following is a customized error message:

The CloudFront distribution can use the ALB as the origin, which will cause the website content to be cached on the

CloudFront edge caches.

This solution represents the most operationally efficient choice as no action is required in the event of an issue,

other than troubleshooting the root cause.

- ✅ :  "Create a Route 53 alias record for an Amazon CloudFront distribution and specify the ALB as the origin.

  Create custom error pages for the distribution" is the correct answer.

- ❌ :  "Create a Route 53 active-passive failover configuration. Create a static website using an Amazon S3 bucket

  that hosts a static error page. Configure the static website as the passive record for failover" is incorrect. This

  option does not represent the lowest operational overhead as manual intervention would be required to cause a

  fail-back to the main website.

- ❌ :  "Create a Route 53 weighted routing policy. Create a static website using an Amazon S3 bucket that hosts a

  static error page. Configure the record for the S3 static website with a weighting of zero. When an issue occurs

  increase the weighting" is incorrect. This option requires manual intervention and there would be a delay from the

  issue arising before an administrative action could make the changes.

- ❌ :  "Set up a Route 53 active-active configuration with the ALB and an Amazon EC2 instance hosting a static

  error page as endpoints. Route 53 will only send requests to the instance if the health checks fail for the ALB" is

  incorrect. With an active-active configuration traffic would be split between the website and the error page.

**References:**

<https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-cloudfront/

----

- #amazon_cloudfront #amazon_cloudfront_distribution #cloudfront_distribution #cloudfront_edge_caches #create_custom_error_pages
