#### MULTI-AZ


Multi-AZ RDS creates a replica in another AZ and synchronously replicates to it (DR only).


There is an option to choose multi-AZ during the launch wizard.


AWS recommends the use of provisioned IOPS storage for multi-AZ RDS DB instances.


Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable.


You cannot choose which AZ in the region will be chosen to create the standby DB instance.


You can view which AZ the standby DB instance is created in.


**A failover may be triggered in the following circumstances:**


- Loss of primary AZ or primary DB instance failure.

- Loss of network connectivity on primary.

- Compute (EC2) unit failure on primary.

- Storage (EBS) unit failure on primary.

- The primary DB instance is changed.

- Patching of the OS on the primary DB instance.

- Manual failover (reboot with failover selected on primary).


During failover RDS automatically updates configuration (including DNS endpoint) to use the second node.


Depending on the instance class it can take 1 to a few minutes to failover to a standby DB instance.


It is recommended to implement DB connection retries in your application.


Recommended to use the endpoint rather than the IP address to point applications to the RDS DB.


The method to initiate a manual RDS DB instance failover is to reboot selecting the option to failover.


A DB instance reboot is required for changes to take effect when you change the DB parameter group or when you change a

static DB parameter.


The DB parameter group is a configuration container for the DB engine configuration.


You will be alerted by a DB instance event when a failover occurs.


There is no charge for data transfer between primary and secondary RDS instances.


Multi-AZ deployments for the MySQL, MariaDB, Oracle and PostgreSQL engines use Amazon’s failover technology.


Multi-AZ deployments for the SQL Server engine use SQL Server Database Mirroring (DBM).


System upgrades like OS patching, DB Instance scaling and system upgrades, are applied first on the standby, before

failing over and modifying the other DB Instance.


In multi-AZ configurations snapshots and automated backups are performed on the standby to avoid I/O suspension on the

primary instance.


**Read Replica Support for Multi-AZ:**


- Amazon RDS Read Replicas for MySQL and MariaDB support Multi-AZ deployments.

- Combining Read Replicas with Multi-AZ enables you to build a resilient disaster recovery


```

strategy and simplify your database engine upgrade process.

```


- A Read Replica in a different region than the source database can be used as a standby database and promoted to become

  the new production database in case of a regional disruption.

- This allows you to scale reads whilst also having multi-AZ for DR.

- Note that RDS for PostgreSQL does not yet support this feature.


**The process for implementing maintenance activities is as follows:**


- Perform operations on standby.

- Promote standby to primary.

- Perform operations on new standby (demoted primary).


You can manually upgrade a DB instance to a supported DB engine version from the AWS Console.


By default, upgrades will take effect during the next maintenance window.


You can optionally force an immediate upgrade.


In multi-AZ deployments version upgrades will be conducted on both the primary and standby at the same time causing an

outage of both DB instance.


Ensure security groups and NACLs will allow your application servers to communicate with both the primary and standby

instances.

