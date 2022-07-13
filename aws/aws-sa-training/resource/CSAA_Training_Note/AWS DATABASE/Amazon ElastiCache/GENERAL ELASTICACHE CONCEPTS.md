#### GENERAL ELASTICACHE CONCEPTS

Fully managed implementations of two popular in-memory data stores – Redis and
Memcached.

ElastiCache is a web service that makes it easy to deploy and run Memcached or
Redis protocol- compliant server nodes in

the cloud.

The in-memory caching provided by ElastiCache can be used to significantly
improve latency and throughput for many

read-heavy application workloads or compute-intensive workloads.

Best for scenarios where the DB load is based on Online Analytics Processing (
OLAP) transactions.

Push-button scalability for memory, writes and reads.

In-memory key/value store – not persistent in the traditional sense.

Billed by node size and hours of use.

Elasticache EC2 nodes cannot be accessed from the Internet, nor can they be
accessed by EC2 instances in other VPCs.

Cached information may include the results of I/O-intensive database queries or
the results of computationally-intensive

calculations.

Can be on-demand or reserved instances too (but not Spot instances).

Elasticache can be used for storing session state.

A node is a fixed-sized chunk of secure, network-attached RAM and is the
smallest building block.

Each node runs an instance of the Memcached or Redis protocol-compliant service
and has its own DNS name and port.

Failed nodes are automatically replaced.

Access to Elasticache nodes is controlled by VPC security groups and subnet
groups (when deployed in a VPC).

Subnet groups are a collection of subnets designated for your Amazon ElastiCache
Cluster.

You cannot move an existing Amazon ElastiCache Cluster from outside VPC into a
VPC.

You need to configure subnet groups for Elasticache for the VPC that hosts the
EC2 instances and the Elasticache

cluster.

When not using a VPC, Amazon ElastiCache allows you to control access to your
clusters through

Cache Security Groups (you need to link the corresponding EC2 Security Groups).

Elasticache nodes are deployed in clusters and can span more than one subnet of
the same subnet group.

A cluster is a collection of one or more nodes using the same caching engine.

Applications connect to Elasticache clusters using endpoints.

An endpoint is a node or cluster’s unique address.

Maintenance windows can be defined and allow software patching to occur.

**There are two types of ElastiCache engine:**

- Memcached – simplest model, can run large nodes with multiple cores/threads,
  can be scaled in and out, can cache

  objects such as DBs.

- Redis – complex model, supports encryption, master / slave replication, cross
  AZ (HA), automatic failover and

  backup/restore.

