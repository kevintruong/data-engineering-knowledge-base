#### MULTI MASTER

Amazon Aurora Multi-Master is a new feature of the Aurora MySQL-compatible
edition that adds the ability to scale out

write performance across multiple Availability Zones, allowing applications to
direct read/write workloads to multiple

instances in a database cluster and operate with higher availability.

Aurora Multi-Master is designed to achieve high availability and ACID
transactions across a cluster of database nodes

with configurable read after write consistency.

**Architecture:**

- An Aurora cluster consists of a set of compute (database) nodes and a shared
  storage volume.

- The storage volume consists of six storage nodes placed in three Availability
  Zones for high availability and

  durability of user data.

- Every database node in the cluster is a writer node that can run read and
  write statements.

There is no single point of failure in the cluster.

Applications can use any writer node for their read/write and DDL needs.

A database change made by a writer node is written to six storage nodes in three
Availability Zones, providing data

durability and resiliency against storage node and Availability Zone failures.

The writer nodes are all functionally equal, and a failure of one writer node
does not affect the availability of the

other writer nodes in the cluster.

**High Availability:**

Aurora Multi-Master improves upon the high availability of the single-master
version of Amazon Aurora because all of the

nodes in the cluster are read/write nodes.

With single-master Aurora, a failure of the single writer node requires the
promotion of a read replica to be the new

writer.

In the case of Aurora Multi-Master, the failure of a writer node merely requires
the application using the writer to

open connections to another writer.

