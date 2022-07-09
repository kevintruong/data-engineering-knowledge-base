#### Question  28


**A distribution method is required for some static files. The requests will mainly be GET requests and a high volume of

GETs is expected, often exceeding 2000 per second. The files are currently stored in an S3 bucket. According to AWS best

practices, how can performance be optimized?**


- [ ] Use cross-region replication to spread the load across regions


- [ ] Use ElastiCache to cache the content


- [x] Integrate CloudFront with S3 to cache the content


- [ ] Use S3 Transfer Acceleration


*