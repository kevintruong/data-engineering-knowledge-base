#### AVAILABILITY AND DURABILITY

RedShift uses replication and continuous backups to enhance availability and
improve durability and can automatically

recover from component and node failures.

Only available in one AZ but you can restore snapshots into another AZ.

Alternatively, you can run data warehouse clusters in multiple AZ’s by loading
data into two Amazon Redshift data

warehouse clusters in separate AZs from the same set of Amazon S3 input files.

Redshift replicates your data within your data warehouse cluster and
continuously backs up your data to Amazon S3.

**RedShift always keeps three copies of your data:**

- The original

- A replica on compute nodes (within the cluster)

- A backup copy on S3

**RedShift provides continuous/incremental backups:**

- Multiple copies within a cluster.

- Continuous and incremental backups to S3.

- Continuous and incremental backups across regions.

- Streaming restore.

**RedShift provides fault tolerance for the following failures:**

- Disk failures.

- Nodes failures.

- Network failures.


- AZ/region level disasters.

For nodes failures the data warehouse cluster will be unavailable for queries
and updates until a replacement node is

provisioned and added to the DB.

**High availability for RedShift:**

- Currently, RedShift does not support Multi-AZ deployments.

- The best HA option is to use multi-node cluster which supports data
  replication and node recovery.

- A single node RedShift cluster does not support data replication and you’ll
  have to restore from a snapshot on S3 if a

  drive fails.

RedShift can asynchronously replicate your snapshots to S3 in another region for
DR.

Single-node clusters do not support data replication (in a failure scenario you
would need to restore from a snapshot).

Scaling requires a period of unavailability of a few minutes (typically during
the maintenance window).

During scaling operations RedShift moves data in parallel from the compute nodes
in your existing data warehouse cluster

to the compute nodes in your new cluster.

By default, Amazon Redshift retains backups for 1 day. You can configure this to
be as long as 35 days.

If you delete the cluster you can choose to have a final snapshot taken and
retained.

Manual backups are not automatically deleted when you delete a cluster.

