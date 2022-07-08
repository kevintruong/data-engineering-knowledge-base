## Quiz 32: A new relational database is being deployed on AWS. The performance requirements are unknown. Which database service does not require you to make capacity decisions upfront?**

- [ ] Amazon DynamoDB
- [ ] Amazon Aurora Serverless
- [ ] Amazon ElastiCache
- [ ] Amazon RDS

----
Answer:

- [ ] Amazon Aurora Serverless
  **Explanation:**
  If you don’t know the performance requirements it will be difficult to determine the correct instance type to use. Amazon Aurora Serverless does not require you to make capacity decisions upfront as you do not select an instance type. As a serverless service it will automatically scale as needed.
- ✅: "Amazon Aurora Serverless" is the correct answer.

- ❌: "Amazon DynamoDB" is incorrect. Amazon DynamoDB is not a relational database, it is a NoSQL database.

- ❌: "Amazon ElastiCache" is incorrect. Amazon ElastiCache is more suitable for caching and also requires an instance type to be selected.

- ❌: "Amazon RDS" is incorrect. Amazon RDS requires an instance type to be selected.
  **References:**
  https://aws.amazon.com/rds/aurora/serverless/


----
#quiz 
- relateTo:: [[Domain 1 Design Resilient Architectures]]