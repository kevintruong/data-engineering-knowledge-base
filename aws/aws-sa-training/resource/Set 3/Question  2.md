#### Question  2


**A company operates a production web application that uses an Amazon RDS MySQL database. The database has automated,

non-encrypted daily backups. To increase the security of the data, it has been recommended that encryption should be

enabled for backups. Unencrypted backups will be destroyed after the first encrypted backup has been completed.**


**What should be done to enable encryption for future backups?**


1: Enable default encryption for the Amazon S3 bucket where backups are stored


2: Modify the backup section of the database configuration to toggle the Enable encryption check box


3: Create a snapshot of the database. Copy it to an encrypted snapshot. Restore the database from the encrypted snapshot


4: Enable an encrypted read replica on RDS for MySQL. Promote the encrypted read replica to primary. Remove the original

database instance


Answer: 3


**Explanation:**


Amazon RDS uses snapshots for backup. Snapshots are encrypted when created only if the database is encrypted and you can

only select encryption for the database when you first create it. In this case the database, and hence the snapshots, ad

unencrypted.


However, you can create an encrypted copy of a snapshot. You can restore using that snapshot which creates a new DB

instance that has encryption enabled. From that point on encryption will be enabled for all snapshots.


- CORRECT "Create a snapshot of the database. Copy it to an encrypted snapshot. Restore the database from the encrypted

  snapshot" is the correct answer.


- INCORRECT "Enable an encrypted read replica on RDS for MySQL. Promote the encrypted read replica to primary. Remove

  the original database instance" is incorrect as you cannot create an encrypted read replica from an unencrypted

  master.


- INCORRECT "Modify the backup section of the database configuration to toggle the Enable encryption check box" is

  incorrect as you cannot add encryption for an existing database.


- INCORRECT "Enable default encryption for the Amazon S3 bucket where backups are stored" is incorrect because you do

  not have access to the S3 bucket in which snapshots are stored.


**References:**


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-rds/

