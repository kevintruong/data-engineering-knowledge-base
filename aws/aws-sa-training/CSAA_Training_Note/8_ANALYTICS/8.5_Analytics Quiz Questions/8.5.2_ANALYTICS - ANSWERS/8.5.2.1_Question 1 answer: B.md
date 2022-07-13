##### Question 1 answer: B


Explanation:


```

What we need here is a service that can streaming collect streaming data. The only option

available is Kinesis Firehose which captures, transforms, and loads streaming data into

“destinations” such as S3, RedShift, Elasticsearch and Splunk.

Amazon EC2 is not suitable for collecting streaming data.

EBS is a block-storage service in which you attach volumes to EC2 instances, this does not assist

with collecting streaming data (see previous point).

Amazon API Gateway is used for hosting and managing APIs not for receiving streaming data.

```

