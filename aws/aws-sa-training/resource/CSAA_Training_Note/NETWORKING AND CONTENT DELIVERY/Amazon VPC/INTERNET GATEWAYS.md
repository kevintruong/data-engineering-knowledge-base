#### INTERNET GATEWAYS


An Internet Gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication

between instances in your VPC and the internet.


**An Internet Gateway serves two purposes:.**


- To provide a target in your VPC route tables for internet-routable traffic.

- To perform network address translation (NAT) for instances that have been assigned public IPv4 addresses.


Internet Gateways (IGW) must be created and then attached to a VPC, be added to a route table, and then associated with

the relevant subnet(s).


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

- Ensure that instances in your subnet have a globally unique IP address (public IPv4 address, Elastic IP address, or

  IPv6 address).

- Ensure that your network access control and security group rules allow the relevant traffic to flow to and from your

  instance.


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

