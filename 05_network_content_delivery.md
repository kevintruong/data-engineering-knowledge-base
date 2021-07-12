
## NETWORKING AND CONTENT DELIVERY

### Amazon VPC

**GENERAL**

Amazon VPC lets you provision a logically isolated section of the Amazon Web Services (AWS) cloud where you can launch AWS resources in a virtual network that you define.

Analogous to having your own DC inside AWS.

Provides complete control over the virtual networking environment including selection of IP ranges, creation of subnets, and configuration of route tables and gateways.

A VPC is logically isolated from other VPCs on AWS.

Possible to connect the corporate data center to a VPC using a hardware VPN (site-to-site).

VPCs are region wide.

A default VPC is created in each region with a subnet in each AZ.

By default, you can create up to 5 VPCs per region.

You can define dedicated tenancy for a VPC to ensure instances are launched on dedicated hardware (overrides the configuration specified at launch).

A default VPC is automatically created for each AWS account the first time Amazon EC2 resources are provisioned.

The default VPC has all-public subnets.

**Public subnets are subnets that have:**

- “Auto-assign public IPv4 address” set to “Yes”.
- The subnet route table has an attached Internet Gateway.

Instances in the default VPC always have both a public and private IP address.

AZs names are mapped to different zones for different users (i.e. the AZ “ap-southeast-2a” may map to a different physical zone for a different user).

**Components of a VPC:**

- **A Virtual Private Cloud:** A logically isolated virtual network in the AWS cloud. You define a VPC’s IP address space from ranges you select.
- **Subnet:** A segment of a VPC’s IP address range where you can place groups of isolated resources (maps to an AZ, 1:1).
- **Internet Gateway:** The Amazon VPC side of a connection to the public Internet.
- **NAT Gateway:** A highly available, managed Network Address Translation (NAT) service for your resources in a private subnet to access the Internet.
- **Hardware VPN Connection:** A hardware-based VPN connection between your Amazon VPC and your datacenter, home network, or co-location facility.

- **Virtual Private Gateway:** The Amazon VPC side of a VPN connection.
- **Customer Gateway:** Your side of a VPN connection.
- **Router:** Routers interconnect subnets and direct traffic between Internet gateways, virtual
    private gateways, NAT gateways, and subnets.
- **Peering Connection:** A peering connection enables you to route traffic via private IP addresses between two peered VPCs.
- **VPC Endpoints:** Enables private connectivity to services hosted in AWS, from within your VPC without using an an Internet Gateway, VPN, Network Address Translation (NAT) devices, or firewall proxies.
- **Egress-only Internet Gateway:** A stateful gateway to provide egress only access for IPv6 traffic from the VPC to the Internet.

**Options for connecting to a VPC are:**

- Hardware based VPN
- Direct Connect
- VPN CloudHub
- Software VPN

**ROUTING**

The VPC router performs routing between AZs within a region.

The VPC router connects different AZs together and connects the VPC to the Internet Gateway.

Each subnet has a route table the router uses to forward traffic within the VPC.

Route tables also have entries to external destinations.

Up to 200 route tables per VPC.

Up to 50 route entries per route table.

Each subnet can only be associated with one route table.

Can assign one route table to multiple subnets.

If no route table is specified a subnet will be assigned to the main route table at creation time.

Cannot delete the main route table.

You can manually set another route table to become the main route table.

There is a default rule that allows all VPC subnets to communicate with one another – this cannot be deleted or modified.

Routing between subnets is always possible because of this rule – any problems communicating is more likely to be security groups or NACLs.

**SUBNETS AND SUBNET SIZING**

**Types of subnet:**

- If a subnet’s traffic is routed to an internet gateway, the subnet is known as a **public subnet.**
- If a subnet doesn’t have a route to the internet gateway, the subnet is known as a **private subnet** 
- If a subnet doesn’t have a route to the internet gateway, but has its traffic routed to a virtual private gateway for a VPN connection, the subnet is known as a **VPN-only subnet.**

The VPC is created with a master address range (CIDR block, can be anywhere from 16 - 28 bits), and subnet ranges are created within that range.

New subnets are always associated with the default route table.

Once the VPC is created you cannot change the CIDR block.

You cannot create additional CIDR blocks that overlap with existing CIDR blocks.

You cannot create additional CIDR blocks in a different RFC 1918 range.

Subnets with overlapping IP address ranges cannot be created.

The first 4 and last 1 IP addresses in a subnet are reserved.

Subnets are created within availability zones (AZs).

Each subnet must reside entirely within one Availability Zone and cannot span zones.

Availability Zones are distinct locations that are engineered to be isolated from failures in other Availability Zones.

Availability Zones are connected with low latency, high throughput, and highly redundant networking.

Can create private, public or VPN subnets.

Subnets map 1:1 to AZs and cannot span AZs.

You can only attach one Internet gateway to a custom VPC.

IPv6 addresses are all public and the range is allocated by AWS.

**INTERNET GATEWAYS**

An Internet Gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between instances in your VPC and the internet.

**An Internet Gateway serves two purposes:.**

- To provide a target in your VPC route tables for internet-routable traffic.
- To perform network address translation (NAT) for instances that have been assigned public IPv4 addresses.

Internet Gateways (IGW) must be created and then attached to a VPC, be added to a route table, and then associated with the relevant subnet(s).

No availability risk or bandwidth constraints.

If your subnet is associated with a route to the Internet, then it is a public subnet.

You cannot have multiple Internet Gateways in a VPC.

IGW is horizontally scaled, redundant and HA.

IGW performs NAT between private and public IPv4 addresses.

IGW supports IPv4 and IPv6.

IGWs must be detached before they can be deleted.

Can only attach 1 IGW to a VPC at a time.

**Gateway terminology:**

- Internet gateway (IGW) – AWS VPC side of the connection to the public Internet.
- Virtual private gateway (VPG) – VPC endpoint on the AWS side.
- Customer gateway (CGW) – representation of the customer end of the connection.

**To enable access to or from the Internet for instances in a VPC subnet, you must do the following:**

- Attach an Internet Gateway to your VPC.
- Ensure that your subnet’s route table points to the Internet Gateway (see below).
- Ensure that instances in your subnet have a globally unique IP address (public IPv4 address, Elastic IP address, or IPv6 address).
- Ensure that your network access control and security group rules allow the relevant traffic to flow to and from your instance.

**Must update subnet route table to point to IGW, either:**

- To all destinations, e.g. 0.0.0.0/0 for IPv4 or ::/0for IPv6.
- To specific public IPv4 addresses, e.g. your company’s public endpoints outside of AWS.

**Egress-only Internet Gateway:**

- Provides outbound Internet access for IPv6 addressed instances.
- Prevents inbound access to those IPv6 instances.
- IPv6 addresses are globally unique and are therefore public by default.
- Stateful – forwards traffic from instance to Internet and then sends back the response.
- Must create a custom route for ::/0 to the Egress-Only Internet Gateway.
- Use Egress-Only Internet Gateway instead of NAT for IPv6.

**VPC WIZARD**

**VPC with a Single Public Subnet:**

- Your instances run in a private, isolated section of the AWS cloud with direct access to the Internet.
- Network access control lists and security groups can be used to provide strict control over inbound and outbound network traffic to your instances.
- Creates a /16 network with a /24 subnet. Public subnet instances use Elastic IPs or Public IPs to access the Internet.

**VPC with Public and Private Subnets:**

- In addition to containing a public subnet, this configuration adds a private subnet whose instances are not addressable from the Internet.
- Instances in the private subnet can establish outbound connections to the Internet via the public subnet using Network Address Translation (NAT).
- Creates a /16 network with two /24 subnets.
- Public subnet instances use Elastic IPs to access the Internet.
- Private subnet instances access the Internet via Network Address Translation (NAT).

**VPC with Public and Private Subnets and Hardware VPN Access:**

- This configuration adds an IPsec Virtual Private Network (VPN) connection between your Amazon VPC and your data center – effectively extending your data center to the cloud while also providing direct access to the Internet for public subnet instances in your Amazon VPC.
- Creates a /16 network with two /24 subnets.
- One subnet is directly connected to the Internet while the other subnet is connected to your corporate network via an IPsec VPN tunnel.

**VPC with a Private Subnet Only and Hardware VPN Access:**

- Your instances run in a private, isolated section of the AWS cloud with a private subnet whose instances are not addressable from the Internet.
- You can connect this private subnet to your corporate data center via an IPsec Virtual Private Network (VPN) tunnel.
- Creates a /16 network with a /24 subnet and provisions an IPsec VPN tunnel between your Amazon VPC and your corporate network.

**NAT INSTANCES**

NAT instances are managed **by** you.

Used to enable private subnet instances to access the Internet.

NAT instance must live on a public subnet with a route to an Internet Gateway.

Private instances in private subnets must have a route to the NAT instance, usually the default route destination of 0.0.0.0/0.

When creating NAT instances always disable the source/destination check on the instance.

NAT instances must be in a single public subnet.

NAT instances need to be assigned to security groups.

Security groups for NAT instances must allow HTTP/HTTPS inbound from the private subnet and outbound to 0.0.0.0/0.

There needs to be a route from a private subnet to the NAT instance for it to work.

The amount of traffic a NAT instance can support is based on the instance type.

Using a NAT instance can lead to bottlenecks (not HA).

HA can be achieved by using Auto Scaling groups, multiple subnets in different AZ’s and a script to automate failover.

Performance is dependent on instance size.

Can scale up instance size or use enhanced networking.

Can scale out by using multiple NATs in multiple subnets.

Can use as a bastion (jump) host.

Can monitor traffic metrics.

Not supported for IPv6 (use Egress-Only Internet Gateway).

**NAT GATEWAYS**

NAT gateways are managed **for** you by AWS.

Fully-managed NAT service that replaces the need for NAT instances on EC2.

Must be created in a public subnet.

Uses an Elastic IP address for the public IP.

Private instances in private subnets must have a route to the NAT instance, usually the default route destination of 0.0.0.0/0.

Created in a specified AZ with redundancy in that zone.

For multi-AZ redundancy, create NAT Gateways in each AZ with routes for private subnets to use the local gateway.

Up to 5 Gbps bandwidth that can scale up to 45 Gbps.

Can’t use a NAT Gateway to access VPC peering, VPN or Direct Connect, so be sure to include specific routes to those in your route table.

NAT gateways are highly available in each AZ into which they are deployed.

They are preferred by enterprises.

No need to patch.

Not associated with any security groups.

Automatically assigned a public IP address.

Remember to update route tables and point towards your gateway.

More secure (e.g. you cannot access with SSH and there are no security groups to maintain).

No need to disable source/destination checks.

Egress only Internet gateways operate on IPv6 whereas NAT gateways operate on IPv4.

Port forwarding is not supported.

Using the NAT Gateway as a Bastion host server is not supported.

Traffic metrics are not supported.

The table below highlights the key differences between both types of gateway:

**SECURITY GROUPS**

Security groups act like a firewall at the instance level.

Specifically, security groups operate at the network interface level.

Can only assign permit rules in a security group, cannot assign deny rules.

There is an implicit deny rule at the end of the security group.

All rules are evaluated until a permit is encountered or continues until the implicit deny.

Can control ingress and egress traffic.

Security groups are stateful.

By default, custom security groups do not have inbound allow rules (all inbound traffic is denied by default).

By default, default security groups do have inbound allow rules (allowing traffic from within the group).

All outbound traffic is allowed by default in custom and default security groups.

You cannot delete the security group that’s created by default within a VPC.

You can use security group names as the source or destination in other security groups.

You can use the security group name as a source in its own inbound rules.

Security group members can be within any AZ or subnet within the VPC.

Security group membership can be changed whilst instances are running.

Any changes made will take effect immediately.

Up to 5 security groups can be added per EC2 instance interface.

There is no limit on the number of EC2 instances within a security group.

You cannot block specific IP addresses using security groups, use NACLs instead.

**NETWORK ACL'S**

Network ACL’s function at the subnet level.

The VPC router hosts the network ACL function.

With NACLs you can have permit and deny rules.

Network ACLs contain a numbered list of rules that are evaluated in order from the lowest number until the explicit deny.

Recommended to leave spacing between network ACL numbers.

Network ACLs have separate inbound and outbound rules and each rule can allow or deny traffic.

Network ACLs are stateless, so responses are subject to the rules for the direction of traffic.

NACLs only apply to traffic that is ingress or egress to the subnet not to traffic within the subnet.

A VPC automatically comes with a default network ACL which allows all inbound/outbound traffic.

A custom NACL denies all traffic both inbound and outbound by default.

All subnets must be associated with a network ACL.

You can create custom network ACL’s. By default, each custom network ACL denies all inbound and outbound traffic until you add rules.

Each subnet in your VPC must be associated with a network ACL. If you don’t do this manually it will be associated with the default network ACL.

You can associate a network ACL with multiple subnets; however, a subnet can only be associated with one network ACL at a time.

Network ACLs do not filter traffic between instances in the same subnet.

NACLs are the preferred option for blocking specific IPs or ranges.

Security groups cannot be used to block specific ranges of IPs.

NACL is the first line of defense, the security group is the second line.

Also recommended to have software firewalls installed on your instances.

Changes to NACLs take effect immediately.

**VPC CONNECTIVITY**

There are several **methods of connecting to a VPC**. These include:

- AWS Managed VPN
- AWS Direct Connect
- AWS Direct Connect plus a VPN
- AWS VPN CloudHub
- Software VPN
- Transit VPC
- VPC Peering
- AWS PrivateLink
- VPC Endpoints

Each of these will be further detailed below.

**AWS MANAGED VPN**

VPNs are quick, easy to deploy, and cost effective.

A Virtual Private Gateway (VGW) is required on the AWS side.

A Customer Gateway is required on the customer side.

The diagram below depicts an AWS Managed VPN configuration:

An Internet routable IP address is required on the customer gateway.

Two tunnels per connection must be configured for redundancy.

You cannot use a NAT gateway in AWS for clients coming in via a VPN.

For route propagation you need to point your VPN-only subnet’s route tables at the VGW.

Must define the IP prefixes that can send/receive traffic through the VGW.

VGW does not route traffic destined outside of the received BGP advertisements, static route entries, or its attached VPC CIDR.

Cannot access Elastic IPs on your VPC via the VPN – Elastic IPs can only be connected to via the Internet.


**AWS DIRECT CONNECT**

AWS Direct Connect makes it easy to establish a dedicated connection from an on-premises network to Amazon VPC.

Using AWS Direct Connect, you can establish private connectivity between AWS and your data center, office, or collocated environment.

This private connection can reduce network costs, increase bandwidth throughput, and provide a more consistent network experience than internet-based connections.

AWS Direct Connect lets you establish 1 Gbps or 10 Gbps dedicated network connections (or multiple connections) between AWS networks and one of the AWS Direct Connect locations.

It uses industry-standard VLANs to access Amazon Elastic Compute Cloud (Amazon EC2) instances running within an Amazon VPC using private IP addresses.

AWS Direct Connect does not encrypt your traffic that is in transit.

You can use the encryption options for the services that traverse AWS Direct Connect.

The diagram below depicts an AWS Direct Connect configuration:


**AWS DIRECT CONNECT PLUS VPN**

With AWS Direct Connect plus VPN, you can combine one or more AWS Direct Connect dedicated network connections with the Amazon VPC VPN.

This combination provides an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than internet-based VPN connections.

You can use AWS Direct Connect to establish a dedicated network connection between your network create a logical connection to public AWS resources, such as an Amazon virtual private gateway IPsec endpoint.

This solution combines the AWS managed benefits of the VPN solution with low latency, increased bandwidth, more consistent benefits of the AWS Direct Connect solution, and an end-to-end, secure IPsec connection.

The diagram below depicts an AWS Direct Connect plus VPN configuration:

**AWS VPN CLOUDHUB**

The AWS VPN CloudHub operates on a simple hub-and-spoke model that you can use with or without a VPC.

Use this design if you have multiple branch offices and existing internet connections and would like to implement a convenient, potentially low-cost hub-and-spoke model for primary or backup connectivity between these remote offices.

VPN CloudHub is used for hardware-based VPNs and allows you to configure your branch offices to go into a VPC and then connect that to the corporate DC (hub and spoke topology with AWS as the hub).

Can have up to 10 IPSec tunnels on a VGW by default.

Uses eBGP.

Branches can talk to each other (and provides redundancy).

Can have Direct Connect connections.

Hourly rates plus data egress charges.

The diagram below depicts an AWS VPN CloudHub configuration:

**SOFTWARE VPN**

Amazon VPC offers you the flexibility to fully manage both sides of your Amazon VPC connectivity by creating a VPN connection between your remote network and a software VPN appliance running in your Amazon VPC network.

This option is recommended if you must manage both ends of the VPN connection either for compliance purposes or for leveraging gateway devices that are not currently supported by Amazon VPC’s VPN solution.

The diagram below depicts a Software VPN configuration:

**TRANSIT VPC**

Building on the Software VPN design mentioned above, you can create a global transit network on AWS.

A transit VPC is a common strategy for connecting multiple, geographically disperse VPCs and remote networks in order to create a global network transit center.

A transit VPC simplifies network management and minimizes the number of connections required to connect multiple VPCs and remote networks.

The diagram below depicts a Transit VPC configuration:

**VPC PEERING**

A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses.

Instances in either VPC can communicate with each other as if they are within the same network.

You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account.

The VPCs can be in different regions (also known as an inter-region VPC peering connection).

Data sent between VPCs in different regions is encrypted (traffic charges apply).

**For inter-region VPC peering there are some limitations:**

- You cannot create a security group rule that references a peer security group.
- Cannot enable DNS resolution.
- Maximum MTU is 1500 bytes (no jumbo frames support).
- Limited region support.

AWS uses the existing infrastructure of a VPC to create a VPC peering connection.

It is neither a gateway nor a VPN connection and does not rely on a separate piece of physical hardware.

There is no single point of failure for communication or a bandwidth bottleneck.

A VPC peering connection helps you to facilitate the transfer of data.

Can only have one peering connection between any two VPCs at a time.

Can peer with other accounts (within or between regions).

Cannot have overlapping CIDR ranges.

A VPC peering connection is a one to one relationship between two VPCs.

You can create multiple VPC peering connections for each VPC that you own, but transitive peering relationships are not supported.

You do not have any peering relationship with VPCs that your VPC is not directly peered with.

Limits are 50 VPC peers per VPC, up to 125 by request.

DNS is supported.

Must update route tables to configure routing.

Must update the inbound and outbound rules for VPC security group to reference security groups in the peered VPC.

When creating a VPC peering connection with another account you need to enter the account ID and VPC ID from the other account.

Need to accept the pending access request in the peered VPC.

The VPC peering connection can be added to route tables – shows as a target starting with “pcx-“.

**AWS PRIVATELINK**

AWS PrivateLink simplifies the security of data shared with cloud-based applications by eliminating the exposure of data to the public Internet.

AWS PrivateLink provides private connectivity between VPCs, AWS services, and on-premises applications, securely on the Amazon network.

AWS PrivateLink makes it easy to connect services across different accounts and VPCs to significantly simplify the network architecture.

The table below provides more information on AWS PrivateLink and when to use it:

**EXAM TIP:** Know the difference between AWS PrivateLink and ClassicLink. ClassicLink allows you to link EC2-Classic instances to a VPC in your account, within the same region. EC2-Classic is an old platform from before VPCs were introduced and is not available to accounts created after December 2013. However, ClassicLink may come up in exam questions as a possible (incorrect)
answer so you need to know what it is.

**VPC ENDPOINTS**

An Interface endpoint uses AWS PrivateLink and is an elastic network interface (ENI) with a private IP address that serves as an entry point for traffic destined to a supported service.

Using PrivateLink you can connect your VPC to supported AWS services, services hosted by other AWS accounts (VPC endpoint services), and supported AWS Marketplace partner services.

**AWS PrivateLink access over Inter-Region VPC Peering:**

- Applications in an AWS VPC can securely access AWS PrivateLink endpoints across AWS Regions using Inter-Region VPC Peering.
- AWS PrivateLink allows you to privately access services hosted on AWS in a highly available and scalable manner, without using public IPs, and without requiring the traffic to traverse the Internet.
- Customers can privately connect to a service even if the service endpoint resides in a different AWS Region.
- Traffic using Inter-Region VPC Peering stays on the global AWS backbone and never traverses the public Internet.

A gateway endpoint is a gateway that is a target for a specified route in your route table, used for traffic destined to a supported AWS service.

An interface VPC endpoint (interface endpoint) enables you to connect to services powered by AWS PrivateLink.

The table below highlights some key information about both types of endpoint:

By default, IAM users do not have permission to work with endpoints.

You can create an IAM user policy that grants users the permissions to create, modify, describe, and delete endpoints.

There’s a long list of services that are supported by interface endpoints.

Gateway endpoints are only available for:

- Amazon DyanmoDB
- Amazon S 3

**EXAM TIP:** Know which services use interface endpoints and gateway endpoints. The easiest way to
remember this is that Gateway Endpoints are for Amazon S3 and DynamoDB only.

**SHARED SERVICES VPCS**

You can allow other AWS accounts to create their application resources, such as EC2 instances, Relational Database Service (RDS) databases, Redshift clusters, and Lambda functions, into shared, centrally-managed Amazon Virtual Private Clouds (VPCs).

VPC sharing enables subnets to be shared with other AWS accounts within the same AWS Organization. **Benefits include:**

- Separation of duties: centrally controlled VPC structure, routing, IP address allocation.
- Application owners continue to own resources, accounts, and security groups.
- VPC sharing participants can reference security group IDs of each other.
- Efficiencies: higher density in subnets, efficient use of VPNs and AWS Direct Connect.
- Hard limits can be avoided, for example, 50 VIFs per AWS Direct Connect connection through simplified network architecture.
- Costs can be optimized through reuse of NAT gateways, VPC interface endpoints, and intra- Availability Zone traffic.

You can create separate Amazon VPCs for each account with the account owner being responsible for connectivity and security of each Amazon VPC.

With VPC sharing, your IT team can own and manage your Amazon VPCs and your application developers no longer have to manage or configure Amazon VPCs, but they can access them as needed.

Can also share Amazon VPCs to leverage the implicit routing within a VPC for applications that require a high degree of interconnectivity and are within the same trust boundaries.

This reduces the number of VPCs that need to be created and managed, while you still benefit from using separate accounts for billing and access control.

Customers can further simplify network topologies by interconnecting shared Amazon VPCs using connectivity features, such as AWS PrivateLink, AWS Transit Gateway, and Amazon VPC peering.

Can also be used with AWS PrivateLink to secure access to resources shared such as applications behind a Network Load Balancer.

**VPC FLOW LOGS**

Flow Logs capture information about the IP traffic going to and from network interfaces in a VPC.

Flow log data is stored using Amazon CloudWatch Logs.

**Flow logs can be created at the following levels:**

- VPC.
- Subnet.
- Network interface.

You can’t enable flow logs for VPC’s that are peered with your VPC unless the peer VPC is in your account.

You can’t tag a flow log.

You can’t change the configuration of a flow log after it’s been created.

After you’ve created a flow log, you cannot change its configuration (you need to delete and re- create).

**Not all traffic is monitored, e.g. the following traffic is excluded:**

- Traffic that goes to Route53.
- Traffic generated for Windows license activation.
- Traffic to and from 169.254.169.254 (instance metadata).
- Traffic to and from 169.254.169.123 for the Amazon Time Sync Service.
- DHCP traffic.
- Traffic to the reserved IP address for the default VPC router.

**HIGH AVAILABILITY APPROACHES FOR NETWORKING**

By creating subnets in the available AZs, you create Multi-AZ presence for your VPC.

Best practice is to create at least two VPN tunnels into your Virtual Private Gateway.

Direct Connect is not HA by default, so you need to establish a secondary connection via another Direct Connect (ideally with another provider) or use a VPN.

Route 53’s health checks provide a basic level of redirecting DNS resolutions.

Elastic IPs allow you flexibility to change out backing assets without impacting name resolution.

For Multi-AZ redundancy of NAT Gateways, create gateways in each AZ with routes for private subnets to use the local gateway.

### Amazon CloudFront

**GENERAL CLOUDFRONT CONCEPTS**

CloudFront is a web service that gives businesses and web application developers an easy and cost- effective way to distribute content with low latency and high data transfer speeds.

CloudFront is a good choice for distribution of frequently accessed static content that benefits from edge delivery—like popular website images, videos, media files or software downloads.

Used for dynamic, static, streaming, and interactive content.

**CloudFront is a global service:**

- Ingress to upload objects.
- Egress to distribute content.

**Amazon CloudFront provides a simple API that lets you:**

- Distribute content with low latency and high data transfer rates by serving requests using a network of edge locations around the world.
- Get started without negotiating contracts and minimum commitments.

You can use a zone apex name on CloudFront.

CloudFront supports wildcard CNAME.

Supports wildcard SSL certificates, Dedicated IP, Custom SSL and SNI Custom SSL (cheaper).
Supports Perfect Forward Secrecy which creates a new private key for each SSL session.

**EDGE LOCATIONS AND REGIONAL EDGE CACHES**

An edge location is the location where content is cached (separate to AWS regions/AZs).

Requests are automatically routed to the nearest edge location.

Edge locations are not tied to Availability Zones or regions.

Regional Edge Caches are located between origin web servers and global edge locations and have a larger cache.

Regional Edge Caches have larger cache-width than any individual edge location, so your objects remain in cache longer at these locations.

Regional Edge caches aim to get content closer to users.

Proxy methods PUT/POST/PATCH/OPTIONS/DELETE go directly to the origin from the edge locations and do not proxy through Regional Edge caches.

Dynamic content goes straight to the origin and does not flow through Regional Edge caches.

Edge locations are not just read only, you can write to them too.

The diagram below shows where Regional Edge Caches and Edge Locations are placed in relation to end users:

**ORIGINS**

An origin is the origin of the files that the CDN will distribute.

Origins can be either an S3 bucket, an EC2 instance, an Elastic Load Balancer, or Route 53 – can also be external (non-AWS).

When using Amazon S3 as an origin you place all of your objects within the bucket.

You can use an existing bucket and the bucket is not modified in any way.

By default, all newly created buckets are private.

**You can setup access control to your buckets using:**

- Bucket policies.
- Access Control Lists.

You can make objects publicly available or use CloudFront signed URLs.

A custom origin server is a HTTP server which can be an EC2 instance or an on-premise/non-AWS based web server.

When using an on-premise or non-AWS based web server you must specify the DNS name, ports and protocols that you want CloudFront to use when fetching objects from your origin.

Most CloudFront features are supported for custom origins except RTMP distributions (must be an S3 bucket).

**When using EC2 for custom origins Amazon recommend:**

- Use an AMI that automatically installs the software for a web server.
- Use ELB to handle traffic across multiple EC2 instances.
- Specify the URL of your load balancer as the domain name of the origin server.

**S3 static website:**

- Enter the S3 static website hosting endpoint for your bucket in the configuration.
- Example: [http://<bucketname>.s3-website-<region>.amazonaws.com.](http://<bucketname>.s3-website-<region>.amazonaws.com.)

Objects are cached for 24 hours by default.

The expiration time is controlled through the TTL.

The minimum expiration time is 0.

Static websites on Amazon S3 are considered custom origins.

AWS origins are Amazon S3 buckets (not a static website).

CloudFront keeps persistent connections open with origin servers.

Files can also be uploaded to CloudFront.

**High availability with Origin Failover:**

- Can set up CloudFront with origin failover for scenarios that require high availability.
- Uses an origin group in which you designate a primary origin for CloudFront plus a second origin that CloudFront automatically switches to when the primary origin returns specific HTTP status code failure responses.
- Also works with Lambda@Edge functions.

**DISTRIBUTIONS**

To distribute content with CloudFront you need to create a distribution.

**The distribution includes the configuration of the CDN including:**

- Content origins.
- Access (public or restricted).
- Security (HTTP or HTTPS).
- Cookie or query-string forwarding.
- Geo-restrictions.
- Access logs (record viewer activity).

**There are two types of distribution.**

**Web Distribution:**

- Static and dynamic content including .html, .css, .php, and graphics files.
- Distributes files over HTTP and HTTPS.
- Add, update, or delete objects, and submit data from web forms.
- Use live streaming to stream an event in real time.

**RTMP:**

- Distribute streaming media files using Adobe Flash Media Server’s RTMP protocol.
- Allows an end user to begin playing a media file before the file has finished downloading from a CloudFront edge location.
- Files must be stored in an S3 bucket.

To use CloudFront live streaming, create a web distribution.

**For serving both the media player and media files you need two types of distributions:**

- A web distribution for the media player.
- An RTMP distribution for the media files.

S3 buckets can be configured to create access logs and cookie logs which log all requests made to the S3 bucket.

Amazon Athena can be used to analyze access logs.

CloudFront is integrated with CloudTrail.

CloudTrail saves logs to the S3 bucket you specify.

CloudTrail captures information about all requests whether they were made using the CloudFront console, the CloudFront API, the AWS SDKs, the CloudFront CLI, or another service.

CloudTrail can be used to determine which requests were made, the source IP address, who made the request etc.

To view CloudFront requests in CloudTrail logs you must update an existing trail to include global services.

To delete a distribution, it must first be disabled (can take up to 15 minutes).

The diagram below depicts Amazon CloudFront Distributions and Origins:

**CACHE BEHAVIOR**

Allows you to configure a variety of CloudFront functionality for a given URL path pattern.

**For each cache behavior you can configure the following functionality:**

- The path pattern (e.g. /images/*.jpg, /images*.php).
- The origin to forward requests to (if there are multiple origins).
- Whether to forward query strings.
- Whether to require signed URLs.
- Allowed HTTP methods.
- Minimum amount of time to retain the files in the CloudFront cache (regardless of the values of any cache-control headers).

The default cache behavior only allows a path pattern of /*.

Additional cache behaviors need to be defined to change the path pattern following creation of the distribution.

**You can restrict access to content using the following methods:**

- Restrict access to content using signed cookies or signed URLs.
- Restrict access to objects in your S3 bucket.

A special type of user called an Origin Access Identity (OAI) can be used to restrict access to content in an Amazon S3 bucket.

By using an OAI you can restrict users so they cannot access the content directly using the S3 URL, they must connect via CloudFront.

**You can define the viewer protocol policy:**

- HTTP and HTTPS
- Redirect HTTP to HTTPS
- HTTPS only

**You can define the Allowed HTTP Methods:**

- GET, HEAD
- GET, HEAD, OPTIONS
- GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE

For web distributions you can configure CloudFront to require that viewers use HTTPS.

**Field-Level Encryption:**

- Field-level encryption adds an additional layer of security on top of HTTPS that lets you protect specific data so that it is only visible to specific applications.
- Field-level encryption allows you to securely upload user-submitted sensitive information to your web servers.
- The sensitive information is encrypted at the edge closer to the user and remains encrypted throughout application processing.

**Origin policy:**

- HTTPS only.
- Match viewer – CloudFront matches the protocol with your custom origin.
- Use match viewer only if you specify Redirect HTTP to HTTPS or HTTPS only for the viewer protocol policy.
- CloudFront caches the object once even if viewers makes requests using HTTP and HTTPS.

**Object invalidation:**

- You can remove an object from the cache by invalidating the object.
- You cannot cancel an invalidation after submission.
- You cannot invalidate media files in the Microsoft Smooth Streaming format when you have enabled Smooth Streaming for the corresponding cache behavior.

Objects are cached for the TTL (always recorded in seconds, default is 24 hours, default max is 1 year).

Only caches for GET requests (not PUT, POST, PATCH, DELETE).

Dynamic content is cached.

Consider how often your files change when setting the TTL.

Invalidation can be used to immediately revoke cached objects – chargeable.

Deletions propagate.

**RESTRICTIONS**

Blacklists and whitelists can be used for geography – you can only use one at a time.

**There are two options available for geo-restriction (geo-blocking):**

- Use the CloudFront geo-restriction feature (use for restricting access to all files in a distribution and at the country level).
- Use a 3rd party geo-location service (use for restricting access to a subset of the files in a distribution and for finer granularity at the country level).

**AWS WAF**

AWS WAF is a web application firewall that lets you monitor HTTP and HTTPS requests that are forwarded to CloudFront and lets you control access to your content.

**With AWS WAF you can shield access to content based on conditions in a web access control list (web ACL) such as:**

- Origin IP address.
- Values in query strings.

CloudFront responds to requests with the requested content or an HTTP 403 status code (forbidden).

CloudFront can also be configured to deliver a custom error page.

Need to associate the relevant distribution with the web ACL.

**SECURITY**

PCI DSS compliant but recommended not to cache credit card information at edge locations.

HIPAA compliant as a HIPAA eligible service.

**Distributed Denial of Service (DDoS) protection:**

- CloudFront distributes traffic across multiple edge locations and filters requests to ensure that only valid HTTP(S) requests will be forwarded to backend hosts. CloudFront also supports geoblocking, which you can use to prevent requests from particular geographic locations from being served.


**DOMAIN NAMES**

CloudFront typically creates a domain name such as a232323.cloudfront.net.

Alternate domain names can be added using an alias record (Route 53).

For other service providers use a CNAME (cannot use the zone apex with CNAME).

**Moving domain names between distributions:**

- You can move subdomains yourself.
- For the root domain you need to use AWS support.

**CHARGES**

There is an option for reserved capacity over 12 months or longer (starts at 10TB of data transfer in a single region).

**You pay for:**

- Data Transfer Out to Internet.
- Data Transfer Out to Origin.
- Number of HTTP/HTTPS Requests.
- Invalidation Requests.
- Dedicated IP Custom SSL.
- Field level encryption requests.

**You do not pay for:**

- Data transfer between AWS regions and CloudFront.
- Regional edge cache.
- AWS ACM SSL/TLS certificates.
- Shared CloudFront certificates.

### Amazon Route

**GENERAL ROUTE 53 CONCEPTS**

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) service.

**Route 53 offers the following functions:**

- Domain name registry.
- DNS resolution.
- Health checking of resources.

Route 53 can perform any combination of these functions.

Route 53 provides a worldwide distributed DNS service.

Route 53 is located alongside all edge locations.

Health checks verify Internet connected resources are reachable, available and functional.

Route 53 can be used to route Internet traffic for domains registered with another domain registrar (any domain).

When you register a domain with Route 53 it becomes the authoritative DNS server for that domain and creates a public hosted zone.

To make Route 53 the authoritative DNS for an existing domain without transferring the domain create a Route 53 public hosted zone and change the DNS Name Servers on the existing provider to the Route 53 Name Servers.

Changes to Name Servers may not take effect for up to 48 hours due to the DNS record Time To Live (TTL) values.

You can transfer domains to Route 53 only if the Top Level Domain (TLD) is supported.

You can transfer a domain from Route 53 to another registrar by contacting AWS support.

You can transfer a domain to another account in AWS however it does not migrate the hosted zone by default (optional).

It is possible to have the domain registered in one AWS account and the hosted zone in another AWS account.

Primarily uses UDP port 53 (can use TCP).

AWS offer a 100% uptime SLA for Route 53.

You can control management access to your Amazon Route 53 hosted zone by using IAM.

There is a default limit of 50 domain names, but this can be increased by contacting support.

Private DNS is a Route 53 feature that lets you have authoritative DNS within your VPCs without exposing your DNS records (including the name of the resource and its IP address(es) to the Internet.

You can use the AWS Management Console or API to register new domain names with Route 53.

**HOSTED ZONES**

A hosted zone is a collection of records for a specified domain.

A hosted zone is analogous to a traditional DNS zone file; it represents a collection of records that
can be managed together.

**There are two types of zones:**

- Public host zone – determines how traffic is routed on the Internet.
- Private hosted zone for VPC – determines how traffic is routed within VPC (resources are not accessible outside the VPC).

Amazon Route 53 automatically creates the Name Server (NS) and Start of Authority (SOA) records for the hosted zones.

Amazon Route 53 creates a set of 4 unique name servers (a delegation set) within each hosted zone.

You can create multiple hosted zones with the same name and different records.

NS servers are specified by Fully Qualified Domain Name (FQDN) but you can get the IP addresses from the command line (e.g. dig or nslookup).

For private hosted zones you can see a list of VPCs in each region and must select one.

**For private hosted zones you must set the following VPC settings to “true”:**

- enableDnsHostname
- enableDnsSupport

You also need to create a DHCP options set.

You can extend an on-premises DNS to VPC.

You cannot extend Route 53 to on-premises instances.

You cannot automatically register EC2 instances with private hosted zones (would need to be scripted).

Health checks check the instance health by connecting to it.

**Health checks can be pointed at:**

- Endpoints
- Status of other health checks
- Status of a CloudWatch alarm

Endpoints can be IP addresses or domain names.

**RECORDS**

**Amazon Route 53 currently supports the following DNS record types:**

- A (address record)
- AAAA (IPv6 address record)
- CNAME (canonical name record)
- CAA (certification authority authorization)
- MX (mail exchange record)
- NAPTR (name authority pointer record
- NS (name server record)
- PTR (pointer record)
- SOA (start of authority record)
- SPF (sender policy framework)
- SRV (service locator)
- TXT (text record)
- Alias (an Amazon Route 53 - specific virtual record)

The Alias record is a Route 53 specific record type.

Alias records are used to map resource record sets in your hosted zone to Amazon Elastic Load Balancing load balancers, Amazon CloudFront distributions, AWS Elastic Beanstalk environments, or Amazon S3 buckets that are configured as websites.

You can use Alias records to map custom domain names (such as api.example.com) both to API

Gateway custom regional APIs and edge-optimized APIs and to Amazon VPC interface endpoints.

The Alias is pointed to the DNS name of the service.

You cannot set the TTL for Alias records for ELB, S3, or Elastic Beanstalk environment (uses the service’s default).

Alias records work like a CNAME record in that you can map one DNS name (e.g. example.com) to another ‘target’ DNS name (e.g. elb1234.elb.amazonaws.com).

An Alias record can be used for resolving apex / naked domain names (e.g. example.com rather than sub.example.com).

A CNAME record can’t be used for resolving apex / naked domain names.

Generally, use an Alias record where possible. The following table details the differences between Alias and CNAME records:

Route 53 supports wildcard entries for all record types, except NS records.

**ROUTING POLICIES**

Routing policies determine how Route 53 responds to queries.

The following table highlights the key function of each type of routing policy:

**Simple:**

- An A record is associated with one or more IP addresses
- Uses round robin
- Does not support health checks

The following diagram depicts an Amazon Route 53 Simple routing policy configuration:

**Failover:**

- Failover to a secondary IP address.
- Associated with a health check.
- Used for active-passive.
- Routes only when the resource is healthy.
- Can be used with ELB.
- When used with Alias records set Evaluate Target Health to “Yes” and do not use health checks.

The following diagram depicts an Amazon Route 53 Failover routing policy configuration:

**Geo-location:**

- Caters to different users in different countries and different languages.
- Contains users within a particular geography and offers them a customized version of the workload based on their specific needs.
- Geolocation can be used for localizing content and presenting some or all of your website in the language of your users.
- Can also protect distribution rights.
- Can be used for spreading load evenly between regions.
- If you have multiple records for overlapping regions, Route 53 will route to the smallest geographic region.
- You can create a default record for IP addresses that do not map to a geographic location.

The following diagram depicts an Amazon Route 53 Geolocation routing policy configuration:

**Geo-proximity routing policy (requires Route Flow):**

- Use for routing traffic based on the location of resources and, optionally, shift traffic from resources in one location to resources in another.

**Latency based routing:**

- AWS maintains a database of latency from different parts of the world.
- Focused on improving performance by routing to the region with the lowest latency.
- You create latency records for your resources in multiple EC2 locations.

The following diagram depicts an Amazon Route 53 Latency based routing policy configuration:

**Multi-value answer routing policy:**

- Use for responding to DNS queries with up to eight healthy records selected at random.

The following diagram depicts an Amazon Route 53 Multivalue routing policy configuration:

**Weighted:**

- Similar to simple but you can specify a weight per IP address.
- You create records that have the same name and type and assign each record a relative
    weight.
- Numerical value that favors one IP over another.
- To stop sending traffic to a resource you can change the weight of the record to 0.

The following diagram depicts an Amazon Route 53 Weighted routing policy configuration:


**TRAFFIC FLOW**

Route 53 Traffic Flow provides Global Traffic Management (GTM) services.

Traffic flow policies allow you to create routing configurations for resources using routing types
such as failover and geolocation.

Create policies that route traffic based on specific constraints, including latency, endpoint health,
load, geo-proximity and geography.

**Scenarios include:**

- Adding a simple backup page in Amazon S3 for a website.
- Building sophisticated routing policies that consider an end user’s geographic location,
    proximity to an AWS region, and the health of each of your endpoints.

Amazon Route 53 Traffic Flow also includes a versioning feature that allows you to maintain a
history of changes to your routing policies, and easily roll back to a previous policy version using the
console or API.

**ROUTE 53 RESOLVER**

Route 53 Resolver is a set of features that enable bi-directional querying between on-premises and
AWS over private connections.

Used for enabling DNS resolution for hybrid clouds.

**Route 53 Resolver Endpoints:**

- Inbound query capability is provided by Route 53 Resolver Endpoints, allowing DNS queries
    that originate on-premises to resolve AWS hosted domains.
- Connectivity needs to be established between your on-premises DNS infrastructure and
    AWS through a Direct Connect (DX) or a Virtual Private Network (VPN).
- Endpoints are configured through IP address assignment in each subnet for which you
    would like to provide a resolver.


**Conditional forwarding rules:**

- Outbound DNS queries are enabled through the use of Conditional Forwarding Rules..
- Domains hosted within your on-premises DNS infrastructure can be configured as
    forwarding rules in Route 53 Resolver.
- Rules will trigger when a query is made to one of those domains and will attempt to forward
    DNS requests to your DNS servers that were configured along with the rules.
- Like the inbound queries, this requires a private connection over DX or VPN.

**CHARGES**

You pay per hosted zone per month (no partial months).

A hosted zone deleted within 12 hours of creation is not charged (queries are charges).

**Additional charges for:**

- Queries
- Traffic Flow
- Health Checks
- Route 53 Resolver ENIs + queries
- Domain names

**Alias records are free of charge when the records are mapped to one of the following:**

- Elastic Load Balancers


- Amazon CloudFront distributions
- AWS Elastic Beanstalk environments
- Amazon S3 buckets that are configured as website endpoints

Health checks are charged with different prices for AWS vs non-AWS endpoints.

You do not pay for the records that you add to your hosted zones.

Latency-based routing queries are more expensive.

Geo DNS and geo-proximity also have higher prices.

### AWS Global Accelerator

AWS Global Accelerator is a service that improves the availability and performance of applications
with local or global users.

It provides static IP addresses that act as a fixed entry point to application endpoints in a single or
multiple AWS Regions, such as Application Load Balancers, Network Load Balancers or EC2
instances.

Uses the AWS global network to optimize the path from users to applications, improving the
performance of TCP and UDP traffic.

AWS Global Accelerator continually monitors the health of application endpoints and will detect an
unhealthy endpoint and redirect traffic to healthy endpoints in less than 1 minute.

**Details and Benefits**

Uses redundant (two) static anycast IP addresses in different network zones (A and B).

The redundant pair are globally advertised.

Uses AWS Edge Locations – addresses are announced from multiple edge locations at the same
time.

Addresses are associated to regional AWS resources or endpoints.

AWS Global Accelerator’s IP addresses serve as the frontend interface of applications.

Intelligent traffic distribution: Routes connections to the closest point of presence for applications.

Targets can be Amazon EC2 instances or Elastic Load Balancers (ALB and NLB).

By using the static IP addresses, you don’t need to make any client-facing changes or update DNS
records as you modify or replace endpoints.

The addresses are assigned to your accelerator for as long as it exists, even if you disable the
accelerator and it no longer accepts or routes traffic.

Does health checks for TCP only – not UDP.

Can assign target weight within a region to control routing and also “dial” up or down traffic to a
region.


**Fault tolerance:**

- Has a fault-isolating design that increases the availability of your applications.
- AWS Global Accelerator allocates two IPv4 static addresses that are serviced by
    independent network zones.
- Similar to Availability Zones, these network zones are isolated units with their own set of
    physical infrastructure and service IP addresses from a unique IP subnet.
- If one IP address from a network zone becomes unavailable, due to network disruptions or
    IP address blocking by certain client networks, client applications can retry using the healthy
    static IP address from the other isolated network zone.

**Global performance-based routing:**

- AWS Global Accelerator uses the vast, congestion-free AWS global network to route TCP
    and UDP traffic to a healthy application endpoint in the closest AWS Region to the user.
- If there’s an application failure, AWS Global Accelerator provides instant failover to the next
    best endpoint.

**Fine-grained traffic control:**

- AWS Global Accelerator gives you the option to dial up or dial down traffic to a specific AWS
    Region by using traffic dials.
- The traffic dial lets you easily do performance testing or blue/green deployment testing for
    new releases across different AWS Regions, for example.
- If an endpoint fails, AWS Global Accelerator assigns user traffic to the other endpoints, to
    maintain high availability.
- By default, traffic dials are set to 100% across all endpoint groups so that AWS Global
    Accelerator can select the best endpoint for applications.

**Continuous availability monitoring:**

- AWS Global Accelerator continuously monitors the health of application endpoints by using
    TCP, HTTP, and HTTPS health checks.
- It instantly reacts to changes in the health or configuration of application endpoints, and
    redirects user traffic to healthy endpoints that deliver the best performance and availability
    to end users.

**Client affinity:**

- AWS Global Accelerator enables you to build applications that require maintaining state.
- For stateful applications where you need to consistently route users to the same endpoint,
    you can choose to direct all requests from a user to the same endpoint, regardless of the
    port and protocol.

**Distributed denial of service (DDoS) resiliency at the edge:**

- By default, AWS Global Accelerator is protected by AWS Shield Standard, which minimizes
    application downtime and latency from denial of service attacks by using always-on network
    flow monitoring and automated in-line mitigation.
- You can also enable AWS Shield Advanced for automated resource-specific enhanced
    detection and mitigation, as well as 24x7 access to the AWS DDoS Response Team (DRT) for


```
manual mitigations of sophisticated DDoS attacks.
```
### Amazon API Gateway

**GENERAL API GATEWAY CONCEPTS**

An Amazon API Gateway is a collection of resources and methods that are integrated with back-end
HTTP endpoints, Lambda functions or other AWS services.

API Gateway is a fully managed service that makes it easy for developers to publish, maintain,
monitor, and secure APIs at any scale.

API Gateway provides developers with a simple, flexible, fully managed, pay-as-you-go service that
handles all aspects of creating and operating robust APIs for application back ends.

API Gateway handles all of the tasks involved in accepting and processing up to hundreds of
thousands of concurrent API calls.

API calls include traffic management, authorization and access control, monitoring, and API version
management.

Together with Lambda, API Gateway forms the app-facing part of the AWS serverless infrastructure.

Back-end services include Amazon EC2, AWS Lambda or any web application (public or private
endpoints).

CloudFront is used as the public endpoint for API Gateway.

Supports API keys and Usage Plans for user identification, throttling or quota management.

Using CloudFront behind the scenes, custom domains, and SNI are supported.

Can be published as products and monetized on AWS Marketplace.

Collections can be deployed in stages.

Permissions to invoke a method are granted using IAM roles and policies or API Gateway custom
authorizers.

An API can present a certificate to be authenticated by the back-end.

All of the APIs created with Amazon API Gateway expose HTTPS endpoints only (does not support
unencrypted endpoints).

By default, API Gateway assigns an internal domain that automatically uses the API Gateway
certificates.

When configuring your APIs to run under a custom domain name you can provide your own
certificate.

Supported data formats include JSON, XML, query string parameters, and request headers.

**Can enable Cross Origin Resource Sharing (CORS) for multiple domain use with Javascript/AJAX:**

- Can be used to enable requests from domains other than the APIs domain.
- Allows the sharing of resources between different domains.


- The method (GET, PUT, POST etc) for which you will enable CORS must be available in the
    API Gateway API before you enable CORS.
- If CORS is not enabled and an API resource received requests from another domain the
    request will be blocked.
- Enable CORS on the APIs resources using the selected methods under the API Gateway.

**Data types used with API Gateway:**

- Any payload sent over HTTP (always encrypted over HTTPS).
- Data formats include JSON, XML, query string parameters and request headers.
- You can declare any content type for your APIs responses, and then use the transform
    templates to change the back-end response into your desired format.

You can add caching to API calls by provisioning an Amazon API Gateway cache and specifying its
size in gigabytes.

**ENDPOINTS**

An _API endpoint_ type refers to the hostname of the API.

The API endpoint type can be _edge-optimized_ , _regional_ , or _private_ , depending on where the
majority of your API traffic originates from.

**Edge-Optimized Endpoint:**

- An edge-optimized API endpoint is best for geographically distributed clients. API requests
    are routed to the nearest CloudFront Point of Presence (POP). This is the default endpoint
    type for API Gateway REST APIs.
- Edge-optimized APIs capitalize the names of HTTP headers (for example, Cookie).
- CloudFront sorts HTTP cookies in natural order by cookie name before forwarding the
    request to your origin. For more information about the way CloudFront processes cookies,
    see Caching Content Based on Cookies.
- Any custom domain name that you use for an edge-optimized API applies across all regions.

**Regional Endpoint:**

- A regional API endpoint is intended for clients in the same region.
- When a client running on an EC2 instance calls an API in the same region, or when an API is
    intended to serve a small number of clients with high demands, a regional API reduces
    connection overhead.
- For a regional API, any custom domain name that you use is specific to the region where the
    API is deployed.
- If you deploy a regional API in multiple regions, it can have the same custom domain name
    in all regions.
- You can use custom domains together with Amazon Route 53 to perform tasks such as
    latency-based routing.
- Regional API endpoints pass all header names through as-is.

**Private Endpoint:**

- A private API endpoint is an API endpoint that can only be accessed from your Amazon


```
Virtual Private Cloud (VPC) using an interface VPC endpoint, which is an endpoint network
interface (ENI) that you create in your VPC.
```
- Private API endpoints pass all header names through as-is.

The following diagram depicts the three different Amazon API Gateway endpoint types:

**ADDITIONAL FEATURES AND BENEFITS**

API Gateway provides several features that assist with creating and managing APIs:

- **Metering** – Define plans that meter and restrict third-party developer access to APIs.
- **Security** – API Gateway provides multiple tools to authorize access to APIs and control
    service operation access.
- **Resiliency** – Manage traffic with throttling so that backend operations can withstand traffic
    spikes.
- **Operations Monitoring** – API Gateway provides a metrics dashboard to monitor calls to
    services.
- **Lifecycle Management** – Operate multiple API versions and multiple stages for each version
    simultaneously so that existing applications can continue to call previous versions after new
    API versions are published.

API Gateway provides robust, secure, and scalable access to backend APIs and hosts multiple
versions and release stages for your APIs.

You can create and distribute API Keys to developers.

Option to use AWS Sig-v4 to authorize access to APIs.

You can throttle and monitor requests to protect your backend.

API Gateway allows you to maintain a cache to store API responses.

SDK Generation for iOS, Android and JavaScript.

Reduced latency and distributed denial of service protection through the use of CloudFront.

Request/response data transformation and API mocking.

Provides Swagger support.


Resiliency through throttling rules based on the number of requests per second for each HTTP
method (GET, PUT).

Throttling can be configured at multiple levels including Global and Service Call.

A cache can be created and specified in gigabytes (not enabled by default).

Caches are provisioned for a specific stage of your APIs.

Caching features include customizable keys and time-to-live (TTL) in seconds for your API data
which enhances response times and reduces load on back-end services.

API Gateway can scale to any level of traffic received by an API.

**LOGGING AND MONITORING**

The Amazon API Gateway logs (near real time) back-end performance metrics such as API calls,
latency, and error rates to CloudWatch.

You can monitor through the API Gateway dashboard (REST API) allowing you to visually monitor
calls to the services.

API Gateway also meters utilization by third-party developers and the data is available in the API
Gateway console and through APIs.

Amazon API Gateway is integrated with AWS CloudTrail to give a full auditable history of the
changes to your REST APIs.

All API calls made to the Amazon API Gateway APIS to create, modify, delete, or deploy REST APIs
are logged to CloudTrail.

**CHARGES**

With Amazon API Gateway, you only pay when your APIs are in use.

There are no minimum fees or upfront commitments.

You pay only for the API calls you receive, and the amount of data transferred out.

There are no data transfer out charges for Private APIs (however, AWS PrivateLink charges apply
when using Private APIs in Amazon API Gateway).

Amazon API Gateway also provides optional data caching charged at an hourly rate that varies
based on the cache size you select.

The API Gateway free tier includes one million API calls per month for up to 12 months.

### AWS Direct Connect

AWS Direct Connect is a network service that provides an alternative to using the Internet to
connect a customer’s on-premise sites to AWS.

Data is transmitted through a private network connection between AWS and a customer’s
datacenter or corporate network.

**Benefits:**


- Reduce cost when using large volumes of traffic.
- Increase reliability (predictable performance).
- Increase bandwidth (predictable bandwidth).
- Decrease latency.

Each AWS Direct Connect connection can be configured with one or more virtual interfaces (VIFs).

Public VIFs allow access to public services such as S3, EC2, and DynamoDB.

Private VIFs allow access to your VPC.

Must use public IP addresses on public VIFs.

Must use private IP addresses on private VIFs.

Cannot do layer 2 over Direct Connect (L3 only).

From Direct Connect you can connect to all AZs **within the region.**

You can establish IPSec connections over public VIFs to remote regions.

Route propagation can be used to send customer side routes to the VPC.

You can only have one 0.0.0.0/0 (all IP addresses) entry per route table.

You can bind multiple ports for higher bandwidth.

Virtual interfaces are configured to connect to either AWS public services (e.g. EC2/S3) or private
services (e.g. VPC based resources).

The diagram below shoes the components of AWS Direct Connect:

Direct Connect is charged by port hours and data transfer.

Available in 1Gbps and 10Gbps.

Speeds of 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, and 500Mbps can be purchased
through AWS Direct Connect Partners.

Uses Ethernet trunking (802.1q).

Each connection consists of a single dedicated connection between ports on the customer router
and an Amazon router.


for HA you must have 2 DX connections – can be active/active or active/standby.

Route tables need to be updated to point to a Direct Connect connection.

VPN can be maintained as a backup with a higher BGP priority.

Recommended to enable Bidirectional Forwarding Detection (BFD) for faster detection and failover.

You cannot extend your on-premise VLANs into the AWS cloud using Direct Connect.

Can aggregate up to 4 Direct Connect ports into a single connection using Link Aggregation Groups
(LAG).

AWS Direct Connect supports both single (IPv4) and dual stack (IPv4/IPv6) configurations on public
and private VIFs.

**Technical requirements for connecting virtual interfaces:**

- A public or private ASN. If you are using a public ASN you must own it. If you are using a
    private ASN, it must be in the 64512 to 65535 range.
- A new unused VLAN tag that you select.
- **Private Connection (VPC)** – The VPC Virtual Private Gateway (VGW) ID.
- **Public Connection** – Public IPs (/30) allocated by you for the BGP session.

**AWS DIRECT CONNECT GATEWAY**

Grouping of Virtual Private Gateways (VGWs) and Private Virtual Interfaces (VIFs) that belong to the
same AWS account.

Direct Connect Gateway enables you to interface with VPCs in any AWS Region (except AWS China
Region).

**You associate an** **_AWS Direct Connect gateway_** **with either of the following gateways:**

- A transit gateway when you have multiple VPCs in the same Region.
- A virtual private gateway.

Can share private virtual interface to interface with more than one Virtual Private Clouds (VPCs)
reducing the number of BGP sessions.

A Direct Connect gateway is a globally available resource.

You can create the Direct Connect gateway in any public Region and access it from all other public
Regions.

The diagram below depicts the components of an AWS Direct Connect Gateway configuration:



### Networking & Content Delivery Quiz Questions

Answers and explanations are provided below after the last question in this section.

**Question 1: At which level do you attach an Internet gateway**

1. Public Subnet
2. Private Subnet
3. Availability Zone
4. VPC

**Question 2: What is the scope of a Virtual Private Cloud (VPC)?**

1. Global
2. Regional
3. Availability Zone

**Question 3: How should subnets be used for fault tolerance?**

1. Create subnets that span multiple availability zones
2. Create subnets that have multiple Internet Gateways
3. Launch EC2 instances into subnets attached to a region
4. Launch EC2 instances into subnets created in different availability zones

**Question 4: Your organization has a pre-production VPC and production VPC. You need to be able
to setup routing between these VPCs using private IP addresses. How can this be done?**

1. Configure a VPC endpoint
2. Add a route table entry for the opposite VPCs Internet gateway
3. Configure a peering connection
4. Use an Egress-only Internet gateway

**Question 5: You created a new private subnet and created a route table with a path to a NAT
gateway. However, EC2 instances launched into this subnet are not able to reach the Internet.
Security Groups for the EC2 instances are setup correctly. What is the most likely explanation?**

1. The security group for the NAT gateway is setup incorrectly.
2. You need to associate the new subnet with the new route table.
3. You need to add an entry for an Internet gateway.

**Question 6: You need to apply a firewall to a group of EC2 instances launched in multiple subnets.
Which option should be used?**

1. Network Access Control List (ACL)
2. Operating system firewall
3. Security Group
4. IAM Policy

**Question 7: An attack has been identified from a group of IP addresses. What’s the quickest way
to block these specific IP addresses from reaching the instances in your subnets?**

1. Apply a Security Group to the instances in the subnets with a deny rule
2. Change the IP addresses used by the instances


3. Detach the Internet Gateway
4. Apply a Network ACL to the subnets involved with a deny rule

**Question 8: An organization needs a private, high-bandwidth, low-latency connection to the AWS
Cloud in order to establish hybrid cloud configuration with their on-premises cloud. What type of
connection should they use?**

1. AWS Managed VPN
2. AWS VPN CloudHub
3. AWS Direct Connect
4. Transit VPC

**Question 9: An Architect needs to point the domain name dctlabs.com to the DNS name of an
Elastic Load Balancer. Which type of record should be used?**

1. MX record
2. A record
3. CNAME record
4. Alias record

**Question 10: A company hosts copies of the same data in Amazon S3 buckets around the world
and needs to ensure that customers connect to the nearest S3 bucket. Which Route 53 routing
policy should be used?**

1. Simple
2. Failover
3. Latency
4. Weighted

**Question 11: A media organization offers news in local languages around the world. Which Route
53 routing policy should be used to direct readers to the website with the correct language?**

1. Latency
2. Geolocation
3. Multivalue answer
4. Weighted

**Question 12: An Architect is designing a web application that has points of presence in several
regions around the world. The Architect would like to provide automatic routing to the nearest
region, with failover possible to other regions. Customers should receive 2 IP addresses for
whitelisting. How can this be achieved?**

1. Use Route 53 latency-based routing
2. Use Amazon CloudFront
3. Use AWS Global Accelerator
4. Use Route 53 geolocation routing

**Question 13: Which services does Amazon API Gateway use for its public endpoint?**

1. AWS Lambda
2. Amazon CloudFront
3. Amazon S3
4. Amazon ECS


**Question 14: A company provides videos for new employees around the world. They need to
store the videos in one location and then provide low-latency access for the employees around
the world. Which service would be best suited to providing fast access to the content?**

1. Amazon S3
2. AWS Global Accelerator
3. Amazon CloudFront
4. AWS Lambda

**Question 15: Which of the following are NOT valid origins for Amazon CloudFront?**

1. Amazon S3 buckets
2. EC2 instance
3. AWS Lambda function
4. Elastic Load Balancer (ELB)


**NETWORKING & CONTENT DELIVERY - ANSWERS**

**Question 1, Answer: 4**

**Explanation:**

```
1 is incorrect. You do not attach Internet gateways to subnets.
2 is incorrect. You do not attach Internet gateways to subnets.
3 is incorrect. You do not attach Internet gateways to AZs.
4 is correct. Internet Gateways are attached to the VPC. You then need to add entries to the
route tables for your public subnets to point to the IGW.
```
**Question 2, Answer: 2**

**Explanation:**

```
1 is incorrect. VPCs are not global.
2 is correct. VPCs are regional. You create VPCs in each region separately.
3 is incorrect. An availability zone exists within a region and a VPC can span subnets attached to
all AZs in the region.
```
**Question 3, Answer: 4**

**Explanation:**

```
1 is incorrect. Subnets cannot span multiple AZs.
2 is incorrect. You cannot have multiple IGWs attached to a VPC.
3 is incorrect. You cannot attach a subnet to a region.
4 is correct. You should create multiple subnets each within a different AZ and launch EC2
instances running your application across these subnets.
```
**Question 4, Answer: 3**

**Explanation:**

```
1 is incorrect. A VPC endpoint can be used for sharing resources between VPCs but it is not used
for direct routing between private IP addresses.
2 is incorrect. You cannot route between VPCs by using Internet gateways.
3 is correct. A peering connection enables you to route traffic via private IP addresses between
two peered VPCs.
4 is incorrect. An egress-only Internet gateway is used for IPv6 traffic.
```
**Question 5, Answer: 2**

**Explanation:**

```
1 is incorrect. NAT gateways do not have security groups.
2 is correct. By default, new subnets are associated with the default route table. You need to
assign the new route table in order for the instances to see the route to the NAT gateway.
3 is incorrect. You cannot use an Internet Gateway with a private subnet as the instances will not
have public IP addresses.
```
**Question 6, Answer: 3**

**Explanation:**


```
1 is incorrect. Network ACLs are applied at the subnet level and will apply to all instances in the
subnet, not just the group of EC2 instances.
2 is incorrect. Operating system-level firewalls require more administrative effort to maintain
and are not the best option on AWS.
3 is correct. A Security Group can be applied to the group of EC2 instances. You can specify what
ports and protocols are allowed to reach the instances and from what sources.
4 is incorrect. An IAM Policy is not a firewall.
```
**Question 7, Answer: 4**

**Explanation:**

```
1 is incorrect. You cannot apply deny rules with security groups.
2 is incorrect. This is not a good solution as it may break applications.
3 is incorrect. This would not block the specific IP addresses; it would stop all Internet
connectivity.
4 is correct. You can apply deny rules with Network ACLs to block the specific IP addresses only.
```
**Question 8, Answer: 3**

**Explanation:**

```
1 is incorrect. AWS Managed VPN uses the public Internet, so it’s not considered a private
connection or low-latency.
2 is incorrect. AWS VPN CloudHub is used for creating a hub and spoke topology of VPN
connections. Uses the public Internet not a private connection.
3 is correct. AWS Direct Connect uses private network connections into the AWS Cloud and is
high-bandwidth and low-latency. This is good for establishing hybrid cloud configurations.
4 is incorrect. A Transit VPC is used for connecting VPCs across regions.
```
**Question 9, Answer: 4**

**Explanation:**

```
1 is incorrect. An MX record is a mail exchange record for email servers.
2 is incorrect. An A record simply points a name to an IP address.
3 is incorrect. A CNAME record cannot be pointed at a domain apex record like dctlabs.com.
4 is correct. An Alias record can be used with domain apex records and can point to an ELB.
```
**Question 10, Answer: 3**

**Explanation:**

```
1 is incorrect. The simple routing policy does not perform any routing based on location or
latency.
2 is incorrect. The failover routing policy uses primary and secondary records for high availability.
3 is correct. The latency routing policy directs based on the lowest latency to the AWS resource.
Latency increases over distance so this should ensure customers connect to the closest S3
bucket.
4 is incorrect. The weighted policy uses relative weights not location or latency.
```
**Question 11, Answer: 2**

**Explanation:**


```
1 is incorrect. The latency routing policy directs based on latency (distance) but does not allow
you to specify geographic locations.
2 is correct. In this case you need to identify specific geographic locations and associate them
with the correct language version.
3 is incorrect. This routing policy returns multiple answers for load balancing.
4 is incorrect. The weighted policy uses relative weights not geographic information.
```
**Question 12, Answer: 3**

**Explanation:**

```
1 is incorrect. Route 53 latency based routing does not provide automatic failover or 2 IP
addresses.
2 is incorrect. Amazon CloudFront is a content delivery network. It does not perform automatic
routing across regions and doesn’t provide 2 IP addresses for whitelisting.
3 is correct. AWS Global Accelerator provides static IP addresses that act as a fixed entry point to
application endpoints in a single or multiple AWS Regions. It uses 2 static anycast IP addresses.
4 is incorrect. Route 53 geolocation based routing does not provide automatic failover or 2 IP
addresses.
```
**Question 13, Answer: 2**

**Explanation:**

```
1 is incorrect. AWS Lambda is not used as the public endpoint for API Gateway.
2 is correct. Amazon CloudFront is used as the public endpoint for API Gateway.
3 is incorrect. Amazon S3 is not used as the public endpoint for API Gateway.
4 is incorrect. Amazon ECS is not used as the public endpoint for API Gateway.
```
**Question 14, Answer: 3**

**Explanation:**

```
1 is incorrect. To provide low-latency access with Amazon S3 you would need to copy the videos
to buckets in different regions around the world and then create a mechanism for directing
employees to the local copy.
2 is incorrect. AWS Global Accelerator is used for directing users of applications to local points of
presence around the world. It is not used for accessing content in S3, it’s used with ELB and
EC2.
3 is correct. CloudFront is a content delivery network and is ideal for this use case as it caches
the content around the world, provides a single endpoint address, and uses a single source for
the videos.
4 is incorrect. AWS Lambda is a compute service and not suited to this use case.
```
**Question 15, Answer: 3**

**Explanation:**

```
1 is incorrect. Amazon S3 buckets are a valid origin for CloudFront.
2 is incorrect. EC2 instances are a valid origin for CloudFront.
3 is correct. AWS Lambda is not a valid origin for Amazon CloudFront.
4 is incorrect. ELBs are a valid origin for CloudFront.
```
