#### Question  2

**A company operates a production web application that uses an Amazon RDS MySQL database. The database has automated,

non-encrypted daily backups. To increase the security of the data, it has been recommended that encryption should be

enabled for backups. Unencrypted backups will be destroyed after the first encrypted backup has been completed.**

**What should be done to enable encryption for future backups?**

- [ ] :  Enable default encryption for the Amazon S3 bucket where backups are stored

- [ ] :  Modify the backup section of the database configuration to toggle the Enable encryption check box

- [x] :  Create a snapshot of the database. Copy it to an encrypted snapshot. Restore the database from the encrypted snapshot

- [ ] :  Enable an encrypted read replica on RDS for MySQL. Promote the encrypted read replica to primary. Remove the original

database instance

----

- #non_-_encrypted_daily_backups #unencrypted_backups #enable_default_encryption #encryption #amazon_rds_mysql_database
- hasExplain:: [[explanation_Question  2.md]]
