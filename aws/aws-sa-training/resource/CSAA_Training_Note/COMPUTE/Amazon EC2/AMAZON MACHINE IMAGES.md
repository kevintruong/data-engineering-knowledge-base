#### AMAZON MACHINE IMAGES


An Amazon Machine Image (AMI) provides the information required to launch an instance.


An AMI includes the following:


- A template for the root volume for the instance (for example, an operating system, an application server, and

  applications).

- Launch permissions that control which AWS accounts can use the AMI to launch instances.

- A block device mapping that specifies the volumes to attach to the instance when it’s launched.


AMIs are regional. You can only launch an AMI from the region in which it is stored. However, you can copy AMI’s to

other regions using the console, command line, or the API.


Volumes attached to the instance are either EBS or Instance store:


- Amazon Elastic Block Store (EBS) provides persistent storage. EBS snapshots, which reside on Amazon S3, are used to

  create the volume.

- Instance store volumes are ephemeral (non-persistent). That means data is lost if the instance is shut down. A

  template stored on Amazon S3 is used to create the volume.


**NETWORKING**


Networking Limits (per Region or as Specified):


**IP Addresses**


There are three types of IP address that can be assigned to an Amazon EC2 instance:


- Public – public address that is assigned automatically to instances in public subnets and reassigned if instance is

  stopped/started.

- Private – private address assigned automatically to all instances.

- Elastic IP – public address that is static.


Public IPv4 addresses are lost when the instance is stopped but private addresses (IPv4 and IPv6)

are retained.


Public IPv4 addresses are retained if you restart the instance.


Elastic IPs are retained when the instance is stopped.


Elastic IP addresses are static public IP addresses that can be remapped (moved) between instances.


All accounts are limited to 5 elastic IP’s per region by default.


AWS charge for elastic IP’s when they’re not being used.


An Elastic IP address is for use in a specific region only.


You can assign custom tags to your Elastic IP addresses to categorize them.


By default, EC2 instances come with a private IP assigned to the primary network interface (eth0).


Public IP addresses are assigned for instances in public subnets (VPC).


Public IP addresses are always assigned for instances in EC2-Classic.


DNS records for elastic IP’s can be configured by filling out a form.


Secondary IP addresses can be useful for hosting multiple websites on a server or redirecting traffic to a standby EC2

instance for HA.


You can choose whether secondary IP addresses can be reassigned.


You can associate a single private IPv4 address with a single Elastic IP address and vice versa.


When reassigned the IPv4 to Elastic IP association is maintained.


When a secondary private address is unassigned from an interface, the associated Elastic IP address is disassociated.


You can assign or remove IP addresses from EC2 instances while they are running or stopped.


All IP addresses (IPv4 and IPv6) remain attached to the network interface when detached or reassigned to another

instance.


You can attach a network interface to an instance in a different subnet as long as it’s within the same AZ.


The following table compares the different types of IP address available in Amazon EC2:


**Elastic Network Interfaces**


An elastic network interface (referred to as a network interface in this documentation) is a logical networking

component in a VPC that represents a virtual network card.


**A network interface can include the following attributes:**


- A primary private IPv4 address from the IPv4 address range of your VPC

- One or more secondary private IPv4 addresses from the IPv4 address range of your VPC

- One Elastic IP address (IPv4) per private IPv4 address

- One public IPv4 address

- One or more IPv6 addresses

- One or more security groups

- A MAC address

- A source/destination check flag

- A description


You can create and configure network interfaces in your account and attach them to instances in your VPC.


You cannot team by adding ENIs to an instance.


eth0 is the primary network interface and cannot be moved or detached.


By default, eth0 is the only Elastic Network Interface (ENI) created with an EC2 instance when launched.


You can add additional interfaces to EC2 instances (number dependent on instances family/type).


An ENI is bound to an AZ and you can specify which subnet/AZ you want the ENI to be added in.


You can specify which IP address within the subnet to configure or leave it be auto-assigned.


You can only add one extra ENI when launching but more can be attached later.


ENIs can be “hot attached” to running instances.


ENIs can be “warm-attached” when the instance is stopped.


ENIs can be “cold-attached” when the instance is launched.


If you add a second interface AWS will not assign a public IP address to eth0 (you would need to add an Elastic IP).


Default interfaces are terminated with instance termination.


Manually added interfaces are not terminated by default.


You can change the termination behavior.


**ENHANCED NETWORKING – ELASTIC NETWORK ADAPTER (ENA)**


Enhanced networking provides higher bandwidth, higher packet-per-second (PPS) performance, and consistently lower

inter-instance latencies.


Enhanced networking is enabled using an Elastic Network Adapter (ENA).


If your packets-per-second rate appears to have reached its ceiling, you should consider moving to enhanced networking

because you have likely reached the upper thresholds of the VIF driver.


AWS currently supports enhanced networking capabilities using SR-IOV.


SR-IOV provides direct access to network adapters, provides higher performance (packets-per- second) and lower latency.


Must launch an HVM AMI with the appropriate drivers.


Only available for certain instance types.


Only supported in VPC.


**ELASTIC FABRIC ADAPTER (EFA)**


An Elastic Fabric Adapter is an AWS Elastic Network Adapter (ENA) with added capabilities.


An EFA can still handle IP traffic, but also supports an important access model commonly called OS bypass.


This model allows the application (most commonly through some user-space middleware) access the network interface

without having to get the operating system involved with each message.


Elastic Fabric Adapter (EFA) is a network interface for Amazon EC2 instances that enables customers to run applications

requiring high levels of inter-node communications at scale on AWS.


Its custom-built operating system (OS) bypass hardware interface enhances the performance of inter-instance

communications, which is critical to scaling these applications.


With EFA, High Performance Computing (HPC) applications using the Message Passing Interface

(MPI) and Machine Learning (ML) applications using NVIDIA Collective Communications Library

(NCCL) can scale to thousands of CPUs or GPUs.


As a result, you get the application performance of on-premises HPC clusters with the on-demand elasticity and

flexibility of the AWS cloud.


EFA is available as an optional EC2 networking feature that you can enable on any supported EC2 instance at no

additional cost.


**ENI VS ENA VS EFA**


**When to use ENI:**


- This is the basic adapter type for when you don't have any high performance requirements.

- Can use with all instance types.


**When to use ENA:**


- Good for use cases that require higher bandwidth and lower inter-instance latency.

- Supported for limited instance types (HVM only).


**When to use EFA:**


- High Performance Computing.

- MPI and ML use cases.

- Tightly coupled applications.

- Can use with all instance types.


**PLACEMENT GROUPS**


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


**IAM ROLES**


IAM roles are more secure than storing access keys and secret access keys on EC2 instances.


IAM roles are easier to manage.


You can attach an IAM role to an instance at launch time or at any time after by using the AWS CLI, SDK, or the EC2

console.


IAM roles can be attached, modified, or replaced at any time.


Only one IAM role can be attached to an EC2 instance at a time.


IAM roles are universal and can be used in any region.


**BASTION/JUMP HOSTS**


You can configure EC2 instances as bastion hosts (aka jump boxes) in order to access your VPC instances for management.


Can use the SSH or RDP protocols to connect to your bastion host.


Need to configure a security group with the relevant permissions.


Can use auto-assigned public IPs or Elastic IPs.


Can use security groups to restrict the IP addresses/CIDRs that can access the bastion host.


Use auto-scaling groups for HA (set to 1 instance to just replace if it fails).


Best practice is to deploy Linux bastion hosts in two AZs, use auto-scaling and Elastic IP addresses.


**EC2 MIGRATION**


VM Import/Export is a tool for migrating VMware, Microsoft, XEN VMs to the Cloud.


Can also be used to convert EC2 instances to VMware, Microsoft or XEN VMs.


**Supported for:**


- Windows and Linux.

- VMware ESX VMDKs and (OVA images for export only).

- Citrix XEN VHD.

- Microsoft Hyper-V VHD.


Can only be used via the API or CLI (not the console).


Stop the VM before generating VMDK or VHD images.


**AWS has a VM connector plugin for vCenter:**


- Allows migration of VMs to S3.

- Then converts into a EC2 AMI.

- Progress can be tracked in vCenter.


**MONITORING**


EC2 status checks are performed every minute and each returns a pass or a fail status.


If all checks pass, the overall status of the instance is **OK.**


If one or more checks fail, the overall status is **impaired.**


System status checks detect (StatusCheckFailed_System) problems with your instance that require

**AWS** involvement to repair.


Instance status checks (StatusCheckFailed_Instance) detect problems that require **your** involvement to repair.


Status checks are built into Amazon EC2, so they cannot be disabled or deleted.


You can, however, create or delete alarms that are triggered based on the result of the status checks.


You can create Amazon CloudWatch alarms that monitor Amazon EC2 instances and automatically perform an action if the

status check fails.


**Actions can include:**


- Recover the instance (only supported on specific instance types and can be used only with StatusCheckFailed_System).

- Stop the instance (only applicable to EBS-backed volumes).

- Terminate the instance (cannot terminate if termination protection is enabled).

- Reboot the instance.


It is a best practice to use EC2 to reboot instance rather than the OS (create a CloudWatch record).


**CloudWatch Monitoring frequency:**


- Standard monitoring = 5 mins

- Detailed monitoring = 1 min (chargeable)


**TAGS**


A tag is a label that you assign to an AWS resource.


Used to manage AWS assets.


Tags are just arbitrary name/value pairs that you can assign to virtually all AWS assets to serve as metadata.


Each tag consists of a key and an optional value, both of which you define.


Tagging strategies can be used for cost allocation, security, automation, and many other uses. For example, you can use

a tag in an IAM policy to implement access control.


Enforcing standardized tagging can be done via AWS Config rules or custom scripts. For example, EC2 instances not

properly tagged are stopped or terminated daily.


Most resources can have up to 50 tags.


**RESOURCE GROUPS**


Resource groups are mappings of AWS assets defined by tags.


Create custom consoles to consolidate metrics, alarms and config details around given tags.


**HIGH AVAILABILITY APPROACHES FOR COMPUTE**


Up-to-date AMIs are critical for rapid fail-over.


AMIs can be copied to other regions for safety or DR staging.


Horizontally scalable architectures are preferred because risk can be spread across multiple smaller machines versus one

large machine.


Reserved instances are the only way to guarantee that resources will be available when needed.


Auto Scaling and Elastic Load Balancing work together to provide automated recovery by maintaining minimum instances.


Route 53 health checks also provide “self-healing” redirection of traffic.


**MIGRATION**


AWS Server Migration Service (SMS) is an agent-less service which makes it easier and faster for you to migrate

thousands of on-premises workloads to AWS.


AWS SMS allows you to automate, schedule, and track incremental replications of live server volumes, making it easier

for you to coordinate large-scale server migrations.


Automates migration of on-premises VMware vSphere or Microsoft Hyper-V/SCVMM virtual machines to AWS.


Replicates VMs to AWS, syncing volumes and creating periodic AMIs.


Minimizes cutover downtime by syncing VMs incrementally.


Supports Windows and Linux VMs only (just like AWS).


The Server Migration Connector is downloaded as a virtual appliance into your on-premises vSphere or Hyper-V

environments.

