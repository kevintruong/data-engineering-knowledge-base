#### Question  60


**A Solutions Architect is building a small web application running on Amazon EC2 that will be serving static content.

The user base is spread out globally and speed is important. Which AWS service can deliver the best user experience

cost-effectively and reduce the load on the web server?**


1: Amazon RedShift


2: Amazon S3


3: Amazon CloudFront


4: Amazon EBS volume


**Answer: 3**


**Explanation:**


This is a good use case for Amazon CloudFront as the user base is spread out globally and CloudFront can cache the

content closer to users and also reduce the load on the web server running on EC2.


- CORRECT "Amazon CloudFront" is the correct answer.


- INCORRECT "Amazon RedShift" is incorrect. Amazon RedShift is a data warehouse and is not suitable in this solution.


- INCORRECT "Amazon S3" is incorrect. Amazon S3 is very cost-effective however a bucket is located in a single region

  and therefore performance is not so great for users a long distance from the bucket.


- INCORRECT "Amazon EBS volume" is incorrect. EBS is not the most cost-effective storage solution and the data would be

  located in a single region to latency could be an issue.


**References:**


https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

