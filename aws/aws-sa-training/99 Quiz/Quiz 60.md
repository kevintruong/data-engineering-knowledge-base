## Quiz 60: A research company is developing a data lake solution in Amazon S3 to analyze huge datasets. The solution makes infrequent SQL queries only. In addition, the company wants to minimize infrastructure costs.**

**Which AWS service should be used to meet these requirements?**

- [ ] Amazon Aurora
- [ ] Amazon RDS for MySQL
- [ ] Amazon Athena
- [ ] Amazon Redshift Spectrum

----
Answer: 3
**Explanation:**
Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run – this satisfies the requirement to minimize infrastructure costs for infrequent queries.

- ✅: "Amazon Athena" is the correct answer.

- ❌: "Amazon Aurora" is incorrect. Amazon RDS and Aurora are not suitable solutions for analyzing datasets on S3 – these are both relational databases typically used for transactional (not analytical) workloads.

- ❌: "Amazon RDS for MySQL" is incorrect as per the previous explanation.

- ❌: "Amazon Redshift Spectrum" is incorrect. Amazon RedShift Spectrum is a feature of Amazon Redshift that enables you to run queries against exabytes of unstructured data in Amazon S3, with no loading or ETL required. However, RedShift nodes run on EC2 instances, so for infrequent queries this will not minimize infrastructure costs.
  **References:**
  https://docs.aws.amazon.com/athena/latest/ug/what-is.html
