#### Question  39


**A Solutions Architect is designing a mobile application that will capture receipt images to track expenses. The

Architect wants to store the images on Amazon S3. However, uploading the images through the web server will create too

much traffic.**


**What is the MOST efficient method to store images from a mobile application on Amazon S3?**


1: Expand the web server fleet with Spot instances to provide the resources to handle the images


2: Upload to a second bucket, and have a Lambda event copy the image to the primary bucket


3: Upload to a separate Auto Scaling Group of server behind an ELB Classic Load Balancer, and have the server instances

write to the Amazon S3 bucket


4: Upload directly to S3 using a pre-signed URL


Answer: 4


**Explanation:**


Uploading using a pre-signed URL allows you to upload the object without having any AWS security

credentials/permissions. Pre-signed URLs can be generated programmatically and anyone who receives a valid pre-signed

URL can then programmatically upload an object. This solution bypasses the web server avoiding any performance

bottlenecks.


- CORRECT "Upload directly to S3 using a pre-signed URL" is the correct answer.


- INCORRECT "Expand the web server fleet with Spot instances to provide the resources to handle the images"

  is incorrect as this is not the most efficient solution.


- INCORRECT "Upload to a second bucket, and have a Lambda event copy the image to the primary bucket" is incorrect.

  Uploading to a second bucket (through the web server) does not solve the issue of the web server being the bottleneck.


- INCORRECT "Upload to a separate Auto Scaling Group of server behind an ELB Classic Load Balancer, and have the server

  instances write to the Amazon S3 bucket" is incorrect as this is not the most efficient solution.


**References:**


https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/

