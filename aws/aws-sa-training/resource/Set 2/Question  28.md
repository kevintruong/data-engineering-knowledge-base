#### Question  28


**An application running on Amazon EC2 needs to regularly download large objects from Amazon S3. How can performance be

optimized for high-throughput use cases?**


1: Issue parallel requests and use byte-range fetches


2: Use Amazon S3 Transfer acceleration


3: Use Amazon CloudFront to cache the content


4: Use AWS Global Accelerator


Answer: 1


**Explanation:**


Using the Range HTTP header in a GET Object request, you can fetch a byte-range from an object, transferring only the

specified portion. You can use concurrent connections to Amazon S3 to fetch different byte ranges from within the same

object. This helps you achieve higher aggregate throughput versus a single whole-object request. Fetching smaller ranges

of a large object also allows your application to improve retry times when requests are interrupted.


- CORRECT "Issue parallel requests and use byte-range fetches" is the correct answer.


- INCORRECT "Use Amazon S3 Transfer acceleration" is incorrect. Amazon S3 Transfer Acceleration is used for speeding up

  uploads of data to Amazon S3 by using the CloudFront network. It is not used for downloading data.


- INCORRECT "Use Amazon CloudFront to cache the content" is incorrect. Amazon CloudFront is used for caching content

  closer to users. In this case the EC2 instance needs to access the data so CloudFront is not a good solution (the edge

  location used by CloudFront may not be closer than the EC2 instance is to the S3 endpoint.


- INCORRECT "Use AWS Global Accelerator" is incorrect. AWS Global Accelerator is used for improving availability and

  performance for Amazon EC2 instances or Elastic Load Balancers (ALB and NLB). It is not used for improving Amazon S3

  performance.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/optimizing-performance-guidelines.html


https://docs.aws.amazon.com/AmazonS3/latest/dev/optimizing-performance-design-patterns.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

