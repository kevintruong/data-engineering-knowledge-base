---
up: [[EC2 NETWORKING]]
---
### **Elastic Network Interfaces**

An elastic network interface (referred to as a network interface in this documentation) is a logical networking component in a VPC that represents a virtual network card.

**A network interface can include the following attributes:**

<!-- #eni_attribute -->
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