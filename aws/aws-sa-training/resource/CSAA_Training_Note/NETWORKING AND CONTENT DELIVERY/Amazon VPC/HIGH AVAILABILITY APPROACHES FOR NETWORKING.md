#### HIGH AVAILABILITY APPROACHES FOR NETWORKING

By creating subnets in the available AZs, you create Multi-AZ presence for your
VPC.

Best practice is to create at least two VPN tunnels into your Virtual Private
Gateway.

Direct Connect is not HA by default, so you need to establish a secondary
connection via another Direct Connect (ideally

with another provider) or use a VPN.

Route 53’s health checks provide a basic level of redirecting DNS resolutions.

Elastic IPs allow you flexibility to change out backing assets without impacting
name resolution.

For Multi-AZ redundancy of NAT Gateways, create gateways in each AZ with routes
for private subnets to use the local

gateway.

