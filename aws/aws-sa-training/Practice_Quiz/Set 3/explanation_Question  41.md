**Explanation:**

One shard provides a capacity of 1MB/sec data input and 2MB/sec data output. One shard can support up to 1000 PUT

records per second. The total capacity of the stream is the sum of the capacities of its shards.

In a case where multiple consumer applications have total reads exceeding the per-shard limits, you need to increase the

number of shards in the Kinesis data stream.

- ✅ :  "Increase the number of shards in the Kinesis data stream" is the correct answer.

- ❌ :  "Implement API throttling to restrict the number of requests per-shard" is incorrect. API throttling is used

  to throttle API requests it is not responsible and cannot be used for throttling Get requests in a Kinesis stream.

- ❌ :  "Increase the number of read transactions per shard" is incorrect. You cannot increase the number of read

  transactions per shard. Read throttling is enabled by default for Kinesis data streams. If you’re still experiencing

  performance issues you must increase the number of shards.

- ❌ :  "Implement read throttling for the Kinesis data stream" is incorrect

**References:**

<https://docs.aws.amazon.com/streams/latest/dev/troubleshooting-consumers.html#consumer-app-reading>- slower

<https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-additional-considerations.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/>

----

- #api_throttling #kinesis_data_stream #<https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-additional-considerations.html> #shard_limits #shards
