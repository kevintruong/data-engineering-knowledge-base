## Quiz 64: The website for a new application received around 50,000 requests each second and the company wants to use multiple applications to analyze the navigation patterns of the users on their website so they can personalize the user experience.**

**What can a Solutions Architect use to collect page clicks for the website and process them sequentially for each user?**

- [ ] Amazon Kinesis Data Streams
- [ ] Amazon SQS FIFO queue
- [ ] AWS CloudTrail trail
- [ ] Amazon SQS standard queue

----
Answer: 1
**Explanation:**
This is a good use case for Amazon Kinesis streams as it is able to scale to the required load, allow multiple applications to access the records and process them sequentially. Amazon Kinesis Data Streams enables real-time processing of streaming big data. It provides ordering of records, as well as the ability to read and/or replay records in the same order to multiple Amazon Kinesis Applications. Amazon Kinesis streams allows up to 1 MiB of data per second or 1,000 records per second for writes per shard. There is no limit on the number of shards so you can easily scale Kinesis Streams to accept 50,000 per second. The Amazon Kinesis Client Library (KCL) delivers all records for a given partition key to the same record processor, making it easier to build multiple applications reading from the same Amazon Kinesis data stream.

- ✅: "Amazon Kinesis Streams" is the correct answer.
- ❌: "Amazon SQS FIFO queue" is incorrect as SQS is not best suited to streaming data and Kinesis is a better solution.
- ❌: "AWS CloudTrail trail" is incorrect. CloudTrail is used for auditing and is not useful here.
- ❌: "Amazon SQS standard queue" is incorrect. Standard SQS queues do not ensure that messages are processed sequentially and FIFO SQS queues do not scale to the required number of transactions a second.
  **References:**
  https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html
  https://aws.amazon.com/kinesis/data-streams/faqs/
