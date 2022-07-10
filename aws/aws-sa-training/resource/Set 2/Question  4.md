#### Question  4


**A website runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The website’s DNS records are hosted

in Amazon Route 53 with the domain name pointing to the ALB. A solution is required for displaying a static error page

if the website becomes unavailable.**


**Which configuration should a solutions architect use to meet these requirements with the LEAST operational overhead?**


- [x] Create a Route 53 alias record for an Amazon CloudFront distribution and specify the ALB as the origin. Create custom

error pages for the distribution


- [ ] Create a Route 53 active-passive failover configuration. Create a static website using an Amazon S3 bucket that hosts

a static error page. Configure the static website as the passive record for failover


- [ ] Create a Route 53 weighted routing policy. Create a static website using an Amazon S3 bucket that hosts a static

error page. Configure the record for the S3 static website with a weighting of zero. When an issue occurs increase the

weighting


- [ ] Set up a Route 53 active-active configuration with the ALB and an Amazon EC2 instance hosting a static error page as

endpoints. Route 53 will only send requests to the instance if the health checks fail for the ALB



- hasExplain:: [[explanation_Question  4.md]]

#failover #passive_failover_configuration #application_load_balancer #amazon_route #amazon_cloudfront_distribution 