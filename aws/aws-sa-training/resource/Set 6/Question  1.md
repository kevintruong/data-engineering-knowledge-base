#### Question  1


**A company runs a streaming media service and the content is stored on Amazon S3. The media catalog server pulls

updated content from S3 and can issue over 1 million read operations per second for short periods. Latency must be kept

under 5ms for these updates. Which solution will provide the BEST performance for the media catalog updates?**


- [x] Update the application code to use an Amazon ElastiCache for Redis cluster


- [ ] Implement Amazon CloudFront and cache the content at Edge Locations


- [ ] Update the application code to use an Amazon DynamoDB Accelerator cluster


- [ ] Implement an Instance store volume on the media catalog server

