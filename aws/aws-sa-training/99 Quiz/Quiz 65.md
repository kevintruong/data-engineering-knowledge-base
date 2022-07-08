## Quiz 65: You are building an application that will collect information about user behavior. The application will rapidly ingest large amounts of dynamic data and requires very low latency. The database must be scalable without incurring downtime. Which database would you recommend for this scenario?**

- [ ] RDS with MySQL
- [ ] DynamoDB
- [ ] RedShift
- [ ] RDS with Microsoft SQL

----
Answer: 2
**Explanation:**
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. Push button scaling means that you can scale the DB at any time without incurring downtime. DynamoDB provides low read and write latency.

- ✅: "DynamoDB" is the correct answer.
- ❌: "RDS with MySQL" is incorrect. RDS uses EC2 instances so you have to change your instance type/size in order to scale compute vertically.
- ❌: "RedShift" is incorrect. RedShift uses EC2 instances as well, so you need to choose your instance type/size for scaling compute vertically, but you can also scale horizontally by adding more nodes to the cluster.
- ❌: "RDS with Microsoft SQL" is incorrect. Rapid ingestion of dynamic data is not an ideal use case for RDS or RedShift.
  **References:**
  https://aws.amazon.com/dynamodb/
  dynamodb/
