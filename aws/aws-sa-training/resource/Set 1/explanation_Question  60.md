**Explanation:**

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena

is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run – this satisfies

the requirement to minimize infrastructure costs for infrequent queries.

- ✅ :  "Amazon Athena" is the correct answer.

- ❌ :  "Amazon Aurora" is incorrect. Amazon RDS and Aurora are not suitable solutions for analyzing datasets on S3

  – these are both relational databases typically used for transactional (not analytical) workloads.

- ❌ :  "Amazon RDS for MySQL" is incorrect as per the previous explanation.

- ❌ :  "Amazon Redshift Spectrum" is incorrect. Amazon RedShift Spectrum is a feature of Amazon Redshift that

  enables you to run queries against exabytes of unstructured data in Amazon S3, with no loading or ETL required.

  However, RedShift nodes run on EC2 instances, so for infrequent queries this will not minimize infrastructure costs.

**References:**

<https://docs.aws.amazon.com/athena/latest/ug/what-is.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/>

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/> #amazon_athena #amazon_aurora #amazon_redshift_spectrum #amazon_redshift
