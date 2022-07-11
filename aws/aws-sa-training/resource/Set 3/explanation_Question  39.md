**Explanation:**

Uploading using a pre-signed URL allows you to upload the object without having any AWS security

credentials/permissions. Pre-signed URLs can be generated programmatically and anyone who receives a valid pre-signed

URL can then programmatically upload an object. This solution bypasses the web server avoiding any performance

bottlenecks.

- ✅ :  "Upload directly to S3 using a pre-signed URL" is the correct answer.

- ❌ :  "Expand the web server fleet with Spot instances to provide the resources to handle the images"

  is incorrect as this is not the most efficient solution.

- ❌ :  "Upload to a second bucket, and have a Lambda event copy the image to the primary bucket" is incorrect.

  Uploading to a second bucket (through the web server) does not solve the issue of the web server being the bottleneck.

- ❌ :  "Upload to a separate Auto Scaling Group of server behind an ELB Classic Load Balancer, and have the server

  instances write to the Amazon S3 bucket" is incorrect as this is not the most efficient solution.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #amazon_s3_bucket #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/> #aws_security #primary_bucket #s3
