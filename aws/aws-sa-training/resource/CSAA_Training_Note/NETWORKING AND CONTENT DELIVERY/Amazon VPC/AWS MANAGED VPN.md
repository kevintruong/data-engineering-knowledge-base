#### AWS MANAGED VPN


VPNs are quick, easy to deploy, and cost effective.


A Virtual Private Gateway (VGW) is required on the AWS side.


A Customer Gateway is required on the customer side.


The diagram below depicts an AWS Managed VPN configuration:


An Internet routable IP address is required on the customer gateway.


Two tunnels per connection must be configured for redundancy.


You cannot use a NAT gateway in AWS for clients coming in via a VPN.


For route propagation you need to point your VPN-only subnet’s route tables at the VGW.


Must define the IP prefixes that can send/receive traffic through the VGW.


VGW does not route traffic destined outside of the received BGP advertisements, static route entries, or its attached

VPC CIDR.


Cannot access Elastic IPs on your VPC via the VPN – Elastic IPs can only be connected to via the Internet.

