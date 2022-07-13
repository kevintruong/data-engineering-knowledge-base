#### NAT INSTANCES


NAT instances are managed **by** you.


Used to enable private subnet instances to access the Internet.


NAT instance must live on a public subnet with a route to an Internet Gateway.


Private instances in private subnets must have a route to the NAT instance, usually the default route destination of

0.0.0.0/0.


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

