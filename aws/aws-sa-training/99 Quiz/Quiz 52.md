## Quiz 52: The data scientists in your company are looking for a service that can process and analyze real-time, streaming data. They would like to use standard SQL queries to query the streaming data.**

**Which combination of AWS services would deliver these requirements?**

- [ ] DynamoDB and EMR
- [ ] Kinesis Data Streams and Kinesis Data Analytics
- [ ] ElastiCache and EMR
- [ ] Kinesis Data Streams and Kinesis Firehose

----
Answer: 2
**Explanation:**
Kinesis Data Streams enables you to build custom applications that process or analyze streaming data for specialized needs. The diagram below shows the architecture of a Kinesis Data Streams application:
![](aws-solution-architecture-practice-quiz-1641093566922.png)
Amazon Kinesis Data Analytics is the easiest way to process and analyze real-time, streaming data. Kinesis Data Analytics can use standard SQL queries to process Kinesis data streams and can ingest data from Kinesis Streams and Kinesis Firehose.

- ✅: "Kinesis Data Streams and Kinesis Data Analytics" is the correct answer.
- ❌: "DynamoDB and EMR" is incorrect. DynamoDB is a NoSQL database that can be used for storing data from a stream but cannot be used to process or analyze the data or to query it with SQL queries. Elastic Map Reduce (EMR) is a hosted Hadoop framework and is not used for analytics on streaming data.
- ❌: "ElastiCache and EMR" is incorrect as ElastiCache is an in-memory database cache service, it is not used for streaming data. Elastic Map Reduce (EMR) is a hosted Hadoop framework and is not used for analytics on streaming data.
- ❌: "Kinesis Data Streams and Kinesis Firehose" is incorrect. Firehose cannot be used for running SQL queries.
  **References:**
  https://aws.amazon.com/kinesis/
