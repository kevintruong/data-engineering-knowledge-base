**Explanation:**

Amazon Redshift is an enterprise-level, petabyte scale, fully managed data warehousing service. An Amazon Redshift data

warehouse is an enterprise-class relational database query and management system. Redshift supports client connections

with many types of applications, including business intelligence (BI), reporting, data, and analytics tools.

Using Amazon Redshift Spectrum, you can efficiently query and retrieve structured and semistructured data from files in

Amazon S3 without having to load the data into Amazon Redshift tables. Redshift Spectrum queries employ massive

parallelism to execute very fast against large datasets.

Used together, RedShift and RedShift spectrum are suitable for running massive analytics jobs on both the structured (

RedShift data warehouse) and unstructured (Amazon S3) data.

- ✅ :  "Amazon Redshift with Amazon Redshift Spectrum" is the correct answer.

- ❌ :  "Amazon RDS MariaDB with Amazon Athena" is incorrect. Amazon RDS is not suitable for analytics (OLAP) use

  cases as it is designed for transactional (OLTP) use cases. Athena can however be used for running SQL queries on data

  on S3.

- ❌ :  "Amazon DynamoDB with Amazon DynamoDB Accelerator (DAX)" is incorrect. This is an example of a

  non-relational DB with a caching layer and is not suitable for an OLAP use case.

- ❌ :  "Amazon ElastiCache for Redis with cluster mode enabled" is incorrect. This is an example of an in-memory

  caching service. It is good for performance for transactional use cases.

**References:**

<https://docs.aws.amazon.com/redshift/latest/dg/c_redshift_system_overview.html>

<https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- redshift/

----

- #redshift_data_warehouse #amazon_redshift_data #amazon_redshift_spectrum #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>-_redshift/> #amazon_redshift
