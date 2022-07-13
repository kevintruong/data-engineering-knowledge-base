#### Question  54

**A three-tier web application that is deployed in an Amazon VPC has been experiencing heavy load on the database layer.

The database layer uses an Amazon RDS MySQL instance in a multi-AZ configuration. Customers have been complaining about

poor response times. During troubleshooting it has been noted that the database layer is experiencing high read

contention during peak hours of the day.**

**What are two possible options that could be used to offload some of the read traffic from the database to resolve the

performance issues? (Select TWO)**

- [x] :  Add RDS read replicas in each AZ

- [ ] :  Use an ELB to distribute load between RDS instances

- [ ] :  Migrate to DynamoDB

- [ ] :  Use a larger RDS instance size

- [x] :  Deploy ElastiCache in each AZ

*----

- #dynamodb #amazon_rds #rds_instances #larger_rds_instance_size #amazon_vpc
- hasExplain:: [[explanation_Question  54.md]]
