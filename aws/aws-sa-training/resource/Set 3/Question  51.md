#### Question  51


**A company is serving videos to their customers from us-east-1 from an Amazon S3 bucket. The company’s customers are

located around the world and there is high demand during peak hours. Customers in Asia complain about slow download

speeds during peak hours and customers in all locations have reported experiencing HTTP 500 errors.**


**How can a Solutions Architect address the issues?**


- [ ] Use an Amazon Route 53 weighted routing policy for the CloudFront domain name to distribute GET requests between

CloudFront and the S3 bucket


- [ ] Replicate the bucket in us-east-1 and use Amazon Route 53 failover routing to determine which bucket to serve the

content from


- [x] Cache the web content using Amazon CloudFront and use all Edge locations for content delivery


- [ ] Place an Amazon ElastiCache cluster in front of the S3 bucket



- hasExplain:: [[explanation_Question  51.md]]