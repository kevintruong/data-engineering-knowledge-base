## Quiz 20: An insurance company has a web application that serves users in the United Kingdom and Australia. The application includes a database tier using a MySQL database hosted in eu-west-2. The web tier runs from eu- west-2 and ap-southeast-2. Amazon Route 53 geoproximity routing is used to direct users to the closest web tier. It has been noted that Australian users receive slow response times to queries.**

**Which changes should be made to the database tier to improve performance?**

- [ ] Migrate the database to Amazon RDS for MySQL. Configure Multi-AZ in the Australian Region
- [ ] Migrate the database to Amazon DynamoDB. Use DynamoDB global tables to enable replication to additional Regions
- [ ] Deploy MySQL instances in each Region. Deploy an Application Load Balancer in front of MySQL to reduce the load on the primary instance
- [x] Migrate the database to an Amazon Aurora global database in MySQL compatibility mode. Configure read replicas in ap-southeast- 2

----
Answer:

- [x] Migrate the database to an Amazon Aurora global database in MySQL compatibility mode. Configure read replicas in ap-southeast- 2
  **Explanation:**
  The issue here is latency with read queries being directed from Australia to UK which is great physical distance. A solution is required for improving read performance in Australia. An Aurora global database consists of one primary AWS Region where your data is mastered, and up to five read-only, secondary AWS Regions. Aurora replicates data to the secondary AWS Regions with typical latency of under a second. You issue write operations directly to the primary DB instance in the primary AWS Region.
  ![](aws-solution-architecture-practice-quiz-1641092668258.png)
  This solution will provide better performance for users in the Australia Region for queries. Writes must still take place in the UK Region but read performance will be greatly improved.
- ✅: "Migrate the database to an Amazon Aurora global database in MySQL compatibility mode. Configure read replicas in ap-southeast-2" is the correct answer.
- ❌: "Migrate the database to Amazon RDS for MySQL. Configure Multi-AZ in the Australian Region" is incorrect. The database is located in UK. If the database is migrated to Australia then the reverse problem will occur. Multi-AZ does not assist with improving query performance across Regions.
- ❌: "Migrate the database to Amazon DynamoDB. Use DynamoDB global tables to enable replication to additional Regions" is incorrect as a relational database running on MySQL is unlikely to be compatible with DynamoDB.
- ❌: "Deploy MySQL instances in each Region. Deploy an Application Load Balancer in front of MySQL to reduce the load on the primary instance" is incorrect as you can only put ALBs in front of the web tier, not the DB tier.
  **References:**
  https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html



----
#quiz 
- relateTo:: [[Domain 2 Design High-Performing Architectures]]