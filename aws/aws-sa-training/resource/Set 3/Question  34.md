#### Question  34


**A Solutions Architect is designing a solution for a financial application that will receive trading data in large

volumes. What is the best solution for ingesting and processing a very large number of data streams in near real time?**


1: Amazon Redshift


2: Amazon Kinesis Firehose


3: Amazon EMR


4: Amazon Kinesis Data Streams


Answer: 4


**Explanation:**


Kinesis Data Streams enables you to build custom applications that process or analyze streaming data for specialized

needs. It enables real-time processing of streaming big data and can be used for rapidly moving data off data producers

and then continuously processing the data. Kinesis Data Streams stores data for later processing by applications (key

difference with Firehose which delivers data directly to AWS services).


- CORRECT "Amazon Kinesis Data Streams" is the correct answer.


- INCORRECT "Amazon Redshift" is incorrect. RedShift is a data warehouse solution used for analyzing data.


- INCORRECT "Amazon Kinesis Firehose" is incorrect. Kinesis Firehose can allow transformation of data and it then

  delivers data to supported services.


- INCORRECT "Amazon EMR" is incorrect. EMR is a hosted Hadoop framework that is used for analytics.


**References:**


https://docs.aws.amazon.com/streams/latest/dev/introduction.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-kinesis/

