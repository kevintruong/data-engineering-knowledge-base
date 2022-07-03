---

---

### **IP Addresses**

<!-- #ec2_network_ipaddress -->

There are three types of IP address that can be assigned to an Amazon EC2 instance:
- Public – public address that is assigned automatically to instances in public subnets and reassigned if instance is stopped/started.
- Private – private address assigned automatically to all instances.
- Elastic IP – public address that is static.
  
  Public IPv4 addresses are lost when the instance is stopped but private addresses (IPv4 and IPv6) are retained.
  
  Public IPv4 addresses are retained if you restart the instance.
  
  Elastic IPs are retained when the instance is stopped.
  
  Elastic IP addresses are static public IP addresses that can be remapped (moved) between instances.

  ----
#networking

-  up:: [[EC2 NETWORKING]]