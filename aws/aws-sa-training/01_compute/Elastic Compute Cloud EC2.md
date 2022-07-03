---
title: Elastic Compute Cloud EC2 
hash_tag:
  - ec2
  - compute
up: [[AWS SA Training]]
---

Next:: [[Elastic Block Store EBS]]

# Elastic Compute Cloud EC2
	 
## **PLACEMENT GROUPS**

<!-- ec2_placement_group -->

Placement groups are a logical grouping of instances in one of the following configurations.

**Cluster** – clusters instances into a low-latency group in a single AZ:
- A cluster placement group is a logical grouping of instances within a single Availability Zone.
- Cluster placement groups are recommended for applications that benefit from low network latency, high network throughput, or both, and if the majority of the network traffic is between the instances in the group.
  
  **Spread** – spreads instances across underlying hardware (can span AZs):
- A spread placement group is a group of instances that are each placed on distinct underlying hardware.
- Spread placement groups are recommended for applications that have a small number of critical instances that should be kept separate from each other.
  
  **Partition** — divides each group into logical segments called partitions:
- Amazon EC2 ensures that each partition within a placement group has its own set of racks.
- Each rack has its own network and power source. No two partitions within a placement group share the same racks, allowing you to isolate the impact of hardware failure within your application.
- Partition placement groups can be used to deploy large distributed and replicated workloads, such as HDFS, HBase, and Cassandra, across distinct racks.
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


## **EC2 IAM ROLES**

<!-- #ec2_iam -->

IAM roles are more secure than storing access keys and secret access keys on EC2 instances.

IAM roles are easier to manage.

You can attach an IAM role to an instance at launch time or at any time after by using the AWS CLI, SDK, or the EC2 console.

IAM roles can be attached, modified, or replaced at any time.

Only one IAM role can be attached to an EC2 instance at a time.

IAM roles are universal and can be used in any region.

## **BASTION/JUMP HOSTS**

<!-- #ec2_bastion #ec2_jump  -->

You can configure EC2 instances as bastion hosts (aka jump boxes) in order to access your VPC instances for management.

Can use the SSH or RDP protocols to connect to your bastion host.

Need to configure a security group with the relevant permissions.

Can use auto-assigned public IPs or Elastic IPs.

Can use security groups to restrict the IP addresses/CIDRs that can access the bastion host.

Use auto-scaling groups for HA (set to 1 instance to just replace if it fails).

Best practice is to deploy Linux bastion hosts in two AZs, use auto-scaling and Elastic IP addresses.
## **EC2 MIGRATION**

<!-- #ec2_migration -->

VM Import/Export is a tool for migrating VMware, Microsoft, XEN VMs to the Cloud.

Can also be used to convert EC2 instances to VMware, Microsoft or XEN VMs.

---- 

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
## **MONITORING**

<!-- #ec2_monitoring -->

EC2 status checks are performed every minute and each returns a pass or a fail status.

If all checks pass, the overall status of the instance is **OK.**

If one or more checks fail, the overall status is **impaired.**

System status checks detect (StatusCheckFailed_System) problems with your instance that require **AWS** involvement to repair.

Instance status checks (StatusCheckFailed_Instance) detect problems that require **your** involvement to repair.

Status checks are built into Amazon EC2, so they cannot be disabled or deleted.

You can, however, create or delete alarms that are triggered based on the result of the status checks.

You can create Amazon CloudWatch alarms that monitor Amazon EC2 instances and automatically perform an action if the status check fails.

**Actions can include:**
- Recover the instance (only supported on specific instance types and can be used only with StatusCheckFailed_System).
- Stop the instance (only applicable to EBS-backed volumes).
- Terminate the instance (cannot terminate if termination protection is enabled).
- Reboot the instance.
  
  It is a best practice to use EC2 to reboot instance rather than the OS (create a CloudWatch record).
  
  **CloudWatch Monitoring frequency:**
- Standard monitoring = 5 mins
- Detailed monitoring = 1 min (chargeable)
## **TAGS**

<!-- #aws_tags -->

A tag is a label that you assign to an AWS resource.

Used to manage AWS ../assets.
- Tags are just arbitrary name/value pairs that you can assign to virtually all AWS ../assets to serve as metadata.
- Each tag consists of a key and an optional value, both of which you define.
- Tagging strategies can be used for cost allocation, security, automation, and many other uses. 
  
  For example, you can use a tag in an IAM policy to implement access control.
- Enforcing standardized tagging can be done via AWS Config rules or custom scripts. 
  
  For example, EC2 instances not properly tagged are stopped or terminated daily.
  
  Most resources can have up to 50 tags.
## **RESOURCE GROUPS**

<!-- #aws_resource_groups -->

Resource groups are mappings of AWS ../assets defined by tags.

Create custom consoles to consolidate metrics, alarms and config details around given tags.
### **HIGH AVAILABILITY APPROACHES FOR COMPUTE**

<!-- #compute_high_availability -->

Up-to-date AMIs are critical for rapid fail-over.

AMIs can be copied to other regions for safety or DR staging.

Horizontally scalable architectures are preferred because risk can be spread across multiple smaller machines versus one large machine.

Reserved instances are the only way to guarantee that resources will be available when needed.

Auto Scaling and Elastic Load Balancing work together to provide automated recovery by maintaining minimum instances.

Route 53 health checks also provide “self-healing” redirection of traffic.
## **EC2 MIGRATION**

<!-- #ec2_migration -->

AWS Server Migration Service (SMS) is an agent-less service which makes it easier and faster for you to migrate thousands of on-premises workloads to AWS.

AWS SMS allows you to automate, schedule, and track incremental replications of live server volumes, making it easier for you to coordinate large-scale server migrations.

Automates migration of on-premises VMware vSphere or Microsoft Hyper-V/SCVMM virtual machines to AWS.

Replicates VMs to AWS, syncing volumes and creating periodic AMIs.

Minimizes cut over downtime by syncing VMs incrementally.

Supports Windows and Linux VMs only (just like AWS).

The Server Migration Connector is downloaded as a virtual appliance into your on-premises vSphere or Hyper-V environments.