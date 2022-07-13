#### IAM ROLES


IAM roles are more secure than storing access keys and secret access keys on EC2 instances.


IAM roles are easier to manage.


You can attach an IAM role to an instance at launch time or at any time after by using the AWS CLI, SDK, or the EC2

console.


IAM roles can be attached, modified, or replaced at any time.


Only one IAM role can be attached to an EC2 instance at a time.


IAM roles are universal and can be used in any region.


**BASTION/JUMP HOSTS**


You can configure EC2 instances as bastion hosts (aka jump boxes) in order to access your VPC instances for management.


Can use the SSH or RDP protocols to connect to your bastion host.


Need to configure a security group with the relevant permissions.


Can use auto-assigned public IPs or Elastic IPs.


Can use security groups to restrict the IP addresses/CIDRs that can access the bastion host.


Use auto-scaling groups for HA (set to 1 instance to just replace if it fails).


Best practice is to deploy Linux bastion hosts in two AZs, use auto-scaling and Elastic IP addresses.

