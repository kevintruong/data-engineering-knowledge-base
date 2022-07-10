#### Question  20


**An insurance company has a web application that serves users in the United Kingdom and Australia. The application

includes a database tier using a MySQL database hosted in eu-west-2. The web tier runs from eu- west-2 and

ap-southeast-2. Amazon Route 53 geoproximity routing is used to direct users to the closest web tier. It has been noted

that Australian users receive slow response times to queries.**


**Which changes should be made to the database tier to improve performance?**


- [ ] Migrate the database to Amazon RDS for MySQL. Configure Multi-AZ in the Australian Region


- [ ] Migrate the database to Amazon DynamoDB. Use DynamoDB global tables to enable replication to additional Regions


- [ ] Deploy MySQL instances in each Region. Deploy an Application Load Balancer in front of MySQL to reduce the load on

the primary instance


- [x] Migrate the database to an Amazon Aurora global database in MySQL compatibility mode. Configure read replicas in

ap-southeast- 2



- hasExplain:: [[explanation_Question  20.md]]

#amazon_dynamodb #database_tier #amazon_route #amazon_rds #global_database 