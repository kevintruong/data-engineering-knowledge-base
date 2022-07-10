#### Question  15

**An application uses Amazon EC2 instances and an Amazon RDS MySQL database. The database is not currently encrypted. A

solutions architect needs to apply encryption to the database for all new and existing data. How should this be

accomplished?**

- [ ] Create an Amazon ElastiCache cluster and encrypt data using the cache nodes

- [ ] Enable encryption for the database using the API. Take a full snapshot of the database. Delete old snapshots

- [x] Take a snapshot of the RDS instance. Create an encrypted copy of the snapshot. Restore the RDS instance from the

encrypted snapshot

- [ ] Create an RDS read replica with encryption at rest enabled. Promote the read replica to master and switch the

application over to the new master. Delete the old RDS instance

- hasExplain:: [[explanation_Question  15.md]]

# amazon_rds_mysql_database #amazon_elasticache_cluster #old_rds_instance #rds_instance #encryption
