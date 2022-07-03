### Differences between clustered and spread placement groups


![img.png](placement_grou_diffenreces.png)

Launching instances in a spread placement group reduces the risk of simultaneous failures that might occur when instances share the same underlying hardware.

Recommended for applications that benefit from low latency and high bandwidth.

Recommended using an instance type that supports enhanced networking.

Instances within a placement group can communicate with each other using private or public IP addresses.


Best performance is achieved when using private IP addresses.

Using public IP addresses, the performance is limited to 5Gbps or less.

Low-latency 10 Gbps or 25 Gbps network.

Recommended to keep instance types homogenous within a placement group.

Can use reserved instances at an instance level but cannot reserve capacity for the placement group.

The name you specify for a placement group must be unique within your AWS account for the Region.

You can’t merge placement groups.

An instance can be launched in one placement group at a time; it cannot span multiple placement groups.

On-Demand Capacity Reservation and zonal Reserved Instances provide a capacity reservation for EC2 instances in a specific Availability Zone. The capacity reservation can be used by instances in a placement group. However, it is not possible to explicitly reserve capacity for a placement group.

Instances with a tenancy of host cannot be launched in placement groups.

---- 
- up:: [[PLACEMENT GROUPS]]