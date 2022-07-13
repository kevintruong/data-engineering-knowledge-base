#### S3 CLOUDWATCH METRICS

You can use the AWS Management Console to enable the generation of 1 - minute
CloudWatch request metrics for your S3

bucket or configure filters for the metrics using a prefix or object tag.

Alternatively, you can call the S3 PUT Bucket Metrics API to enable and
configure publication of S3 storage metrics.

CloudWatch Request Metrics will be available in CloudWatch within 15 minutes
after they are enabled.

CloudWatch Storage Metrics are enabled by default for all buckets and reported
once per day.

**The S3 metrics that can be monitored include:**

- S3 requests

- Bucket storage

- Bucket size

- All requests

- HTTP 4XX/5XX errors

