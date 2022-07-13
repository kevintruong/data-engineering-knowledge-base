#### GENERAL

Amazon VPC lets you provision a logically isolated section of the Amazon Web
Services (AWS) cloud where you can launch

AWS resources in a virtual network that you define.

Analogous to having your own DC inside AWS.

Provides complete control over the virtual networking environment including
selection of IP ranges, creation of subnets,

and configuration of route tables and gateways.

A VPC is logically isolated from other VPCs on AWS.

Possible to connect the corporate data center to a VPC using a hardware VPN (
site-to-site).

VPCs are region wide.

A default VPC is created in each region with a subnet in each AZ.

By default, you can create up to 5 VPCs per region.

You can define dedicated tenancy for a VPC to ensure instances are launched on
dedicated hardware (overrides the

configuration specified at launch).

A default VPC is automatically created for each AWS account the first time
Amazon EC2 resources are provisioned.

The default VPC has all-public subnets.

**Public subnets are subnets that have:**

- “Auto-assign public IPv4 address” set to “Yes”.

- The subnet route table has an attached Internet Gateway.

Instances in the default VPC always have both a public and private IP address.

AZs names are mapped to different zones for different users (i.e. the AZ
“ap-southeast-2a” may map to a different

physical zone for a different user).

**Components of a VPC:**

- **A Virtual Private Cloud:** A logically isolated virtual network in the AWS
  cloud. You define a VPC’s IP address

  space from ranges you select.

- **Subnet:** A segment of a VPC’s IP address range where you can place groups
  of isolated resources (maps to an AZ, 1:

  1).

- **Internet Gateway:** The Amazon VPC side of a connection to the public
  Internet.

- **NAT Gateway:** A highly available, managed Network Address Translation (NAT)
  service for your resources in a private

  subnet to access the Internet.

- **Hardware VPN Connection:** A hardware-based VPN connection between your
  Amazon VPC and your datacenter, home

  network, or co-location facility.


- **Virtual Private Gateway:** The Amazon VPC side of a VPN connection.

- **Customer Gateway:** Your side of a VPN connection.

- **Router:** Routers interconnect subnets and direct traffic between Internet
  gateways, virtual private gateways, NAT

  gateways, and subnets.

- **Peering Connection:** A peering connection enables you to route traffic via
  private IP addresses between two peered

  VPCs.

- **VPC Endpoints:** Enables private connectivity to services hosted in AWS,
  from within your VPC without using an an

  Internet Gateway, VPN, Network Address Translation (NAT)

  devices, or firewall proxies.

- **Egress-only Internet Gateway:** A stateful gateway to provide egress only
  access for IPv6 traffic from the VPC to

  the Internet.

**Options for connecting to a VPC are:**

- Hardware based VPN

- Direct Connect

- VPN CloudHub

- Software VPN

