#### TIME RESTORE

Amazon Aurora’s backup capability enables point-in-time recovery for your
instance.

This allows you to restore your database to any second during your retention
period, up to the last five minutes.

Your automatic backup retention period can be configured up to thirty-five days.

Automated backups are stored in Amazon S3, which is designed for 99.999999999%
durability. Amazon Aurora backups are

automatic, incremental, and continuous and have no impact on database
performance.

When automated backups are turned on for your DB Instance, Amazon RDS
automatically performs a full daily snapshot of

your data (during your preferred backup window) and captures transaction logs (
as updates to your DB Instance are made).

Automated backups are enabled by default and data is stored on S3 and is equal
to the size of the DB.

Amazon RDS retains backups of a DB Instance for a limited, user-specified period
of time called the retention period,

which by default is 7 days but can be up to 35 days.

**There are two methods to backup and restore RDS DB instances:**

- Amazon RDS automated backups.

- User initiated manual backups.

Both options back up the entire DB instance and not just the individual DBs.

Both options create a storage volume snapshot of the entire DB instance.

You can make copies of automated backups and manual snapshots.

Automated backups backup data to multiple AZs to provide for data durability.

Multi-AZ backups are taken from the standby instance (for MariaDB, MySQL, Oracle
and PostgresSQL).

The DB instance must be in an Active state for automated backups to happen.

Only automated backups can be used for point-in-time DB instance recovery.

The granularity of point-in-time recovery is 5 minutes.

Amazon RDS creates a daily full storage volume snapshot and also captures
transaction logs regularly.

You can choose the backup window.

There is no additional charge for backups but you will pay for storage costs on
S3.

You can disable automated backups by setting the retention period to zero (0).

An outage occurs if you change the backup retention period from zero to a
non-zero value or the other way around.

The retention period is the period AWS keeps the automated backups before
deleting them.

**Retention periods:**

- By default the retention period is 7 days if configured from the console for
  all DB engines except Aurora.

- The default retention period is 1 day if configured from the API or CLI.

- The retention period for Aurora is 1 day regardless of how it is configured.

- You can increase the retention period up to 35 days.

During the backup window I/O may be suspended.

Automated backups are deleted when you delete the RDS DB instance.

Automated backups are only supported for InnoDB storage engine for MySQL (not
for myISAM).

When you restore a DB instance the default DB parameters and security groups are
applied – you must then apply the

custom DB parameters and security groups.

You cannot restore from a DB snapshot into an existing DB instance.

Following a restore the new DB instance will have a new endpoint.

The storage type can be changed when restoring a snapshot.

