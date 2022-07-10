#### Question  6


**A website runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The website has a mix of dynamic and

static content. Customers around the world are reporting performance issues with the website.**


**Which set of actions will improve website performance for users worldwide?**


- [x] Create an Amazon CloudFront distribution and configure the ALB as an origin. Then update the Amazon Route 53 record

to point to the CloudFront distribution


- [ ] Create a latency-based Amazon Route 53 record for the ALB. Then launch new EC2 instances with larger instance sizes

and register the instances with the ALB


- [ ] Launch new EC2 instances hosting the same web application in different Regions closer to the users. Use an AWS

Transit Gateway to connect customers to the closest region


- [ ] Migrate the website to an Amazon S3 bucket in the Regions closest to the users. Then create an Amazon Route 53

geolocation record to point to the S3 buckets



- hasExplain:: [[explanation_Question  6.md]]

#cloudfront #aws #ec2 #amazon #performance 