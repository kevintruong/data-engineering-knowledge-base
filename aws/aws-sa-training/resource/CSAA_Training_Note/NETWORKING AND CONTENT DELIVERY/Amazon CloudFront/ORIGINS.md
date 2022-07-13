#### ORIGINS

An origin is the origin of the files that the CDN will distribute.

Origins can be either an S3 bucket, an EC2 instance, an Elastic Load Balancer,
or Route 53 – can also be external (

non-AWS).

When using Amazon S3 as an origin you place all of your objects within the
bucket.

You can use an existing bucket and the bucket is not modified in any way.

By default, all newly created buckets are private.

**You can setup access control to your buckets using:**

- Bucket policies.

- Access Control Lists.

You can make objects publicly available or use CloudFront signed URLs.

A custom origin server is a HTTP server which can be an EC2 instance or an
on-premise/non-AWS based web server.

When using an on-premise or non-AWS based web server you must specify the DNS
name, ports and protocols that you want

CloudFront to use when fetching objects from your origin.

Most CloudFront features are supported for custom origins except RTMP
distributions (must be an S3 bucket).

**When using EC2 for custom origins Amazon recommend:**

- Use an AMI that automatically installs the software for a web server.

- Use ELB to handle traffic across multiple EC2 instances.

- Specify the URL of your load balancer as the domain name of the origin server.

**S3 static website:**

- Enter the S3 static website hosting endpoint for your bucket in the
  configuration.

-

Example: [http://<bucketname>.s3-website-<region>.amazonaws.com.](http://<bucketname>.s3-website-<region>.amazonaws.com.)

Objects are cached for 24 hours by default.

The expiration time is controlled through the TTL.

The minimum expiration time is 0.

Static websites on Amazon S3 are considered custom origins.

AWS origins are Amazon S3 buckets (not a static website).

CloudFront keeps persistent connections open with origin servers.

Files can also be uploaded to CloudFront.

**High availability with Origin Failover:**

- Can set up CloudFront with origin failover for scenarios that require high
  availability.

- Uses an origin group in which you designate a primary origin for CloudFront
  plus a second origin that CloudFront

  automatically switches to when the primary origin returns specific HTTP status
  code failure responses.

- Also works with Lambda@Edge functions.

