#### PLACEMENT GROUPS


Placement groups are a logical grouping of instances in one of the following configurations.


**Cluster** – clusters instances into a low-latency group in a single AZ:


- A cluster placement group is a logical grouping of instances within a single Availability Zone.

- Cluster placement groups are recommended for applications that benefit from low network latency, high network

  throughput, or both, and if the majority of the network traffic is between the instances in the group.


**Spread** – spreads instances across underlying hardware (can span AZs):


- A spread placement group is a group of instances that are each placed on distinct underlying hardware.

- Spread placement groups are recommended for applications that have a small number of critical instances that should be

  kept separate from each other.


**Partition** — divides each group into logical segments called partitions:


- Amazon EC2 ensures that each partition within a placement group has its own set of racks.

- Each rack has its own network and power source. No two partitions within a placement group share the same racks,

  allowing you to isolate the impact of hardware failure within your application.

- Partition placement groups can be used to deploy large distributed and replicated workloads, such as HDFS, HBase, and

  Cassandra, across distinct racks.


The table below describes some key differences between clustered and spread placement groups:


Launching instances in a spread placement group reduces the risk of simultaneous failures that might occur when

instances share the same underlying hardware.


Recommended for applications that benefit from low latency and high bandwidth.


Recommended to use an instance type that supports enhanced networking.


Instances within a placement group can communicate with each other using private or public IP addresses.


Best performance is achieved when using private IP addresses.


Using public IP addresses, the performance is limited to 5Gbps or less.


Low-latency 10 Gbps or 25 Gbps network.


Recommended to keep instance types homogenous within a placement group.


Can use reserved instances at an instance level but cannot reserve capacity for the placement group.


The name you specify for a placement group must be unique within your AWS account for the Region.


You can’t merge placement groups.


An instance can be launched in one placement group at a time; it cannot span multiple placement groups.


On-Demand Capacity Reservation and zonal Reserved Instances provide a capacity reservation for EC2 instances in a

specific Availability Zone. The capacity reservation can be used by instances in a placement group. However, it is not

possible to explicitly reserve capacity for a placement group.


Instances with a tenancy of host cannot be launched in placement groups.

