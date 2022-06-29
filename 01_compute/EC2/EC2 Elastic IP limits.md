### Elastic IP limits 
  
  <!-- #ec2_network_elastic_ip -->
  
  All accounts are limited to 5 elastic IP’s per region by default.
  
  AWS charge for elastic IP’s when they’re not being used.
  
  An Elastic IP address is for use in a specific region only.
  
  You can assign custom tags to your Elastic IP addresses to categorize them.
  
  By default, EC2 instances come with a private IP assigned to the primary network interface (eth0).
  
  Public IP addresses are assigned for instances in public subnets (VPC).
  
  Public IP addresses are always assigned for instances in EC2-Classic.
  
  DNS records for elastic IP’s can be configured by filling out a form.
  
  Secondary IP addresses can be useful for hosting multiple websites on a server or redirecting traffic to a standby EC2 instance for HA.
  
  You can choose whether secondary IP addresses can be reassigned.
  
  You can associate a single private IPv4 address with a single Elastic IP address and vice versa.
  
  When reassigned the IPv4 to Elastic IP association is maintained.
  
  When a secondary private address is unassigned from an interface, the associated Elastic IP address is disassociated.
  
  You can assign or remove IP addresses from EC2 instances while they are running or stopped.
  
  All IP addresses (IPv4 and IPv6) remain attached to the network interface when detached or reassigned to another instance.
  
  You can attach a network interface to an instance in a different subnet as long as it’s within the same AZ.
  
  The following table compares the different types of IP address available in Amazon EC2:
  
  ![img.png](ec2_ip_address_types.png)
