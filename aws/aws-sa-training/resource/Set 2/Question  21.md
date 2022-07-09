#### Question  21


**A solutions architect is optimizing a website for real-time streaming and on-demand videos. The website’s users are

located around the world and the solutions architect needs to optimize the performance for both the real-time and

on-demand streaming.**


**Which service should the solutions architect choose?**


1: Amazon CloudFront


2: AWS Global Accelerator


3: Amazon Route 53


4: Amazon S3 Transfer Acceleration


Answer: 1


**Explanation:**


Amazon CloudFront can be used to stream video to users across the globe using a wide variety of protocols that are

layered on top of HTTP. This can include both on-demand video as well as real time streaming video.


- CORRECT "Amazon CloudFront" is the correct answer.


- INCORRECT "AWS Global Accelerator" is incorrect as this would be an expensive way of getting the content closer to

  users compared to using CloudFront. As this is a use case for CloudFront and there are so many edge locations it is

  the better option.


- INCORRECT "Amazon Route 53" is incorrect as you still need a solution for getting the content closer to users.


- INCORRECT "Amazon S3 Transfer Acceleration" is incorrect as this is used to accelerate uploads of data to Amazon S3

  buckets.


**References:**


https://aws.amazon.com/cloudfront/streaming/


https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/on-demand-streaming-video.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

