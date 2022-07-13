#### ACCESS CONTROL

When you create a file system, you create endpoints in your VPC called “mount
targets”.

When mounting from an EC2 instance, your file system’s DNS name, which you
provide in your mount command, resolves to a

mount target’s IP address.

You can control who can administer your file system using IAM.

You can control access to files and directories with POSIX-compliant user and
group-level permissions.

POSIX permissions allow you to restrict access from hosts by user and group.

EFS Security Groups act as a firewall, and the rules you add define the traffic
flow.

