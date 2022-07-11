**Explanation:**

The best option is to configure the database security group to only allow traffic that originates from the application

security group. You can also define the destination port as the database port. This setup will allow any instance that

is launched and attached to this security group to connect to the database.

- ✅ :  "Configure the database security group to allow traffic only from the application security group" is the

  correct answer.

- ❌ :  "Configure the database security group to allow traffic only from port 3306" is incorrect. Port 3306 for

  MySQL should be the destination port, not the source.

- ❌ :  "Configure a Network ACL on the database subnet to deny all traffic to ports other than 3306" is incorrect.

  This does not restrict access specifically to the application instances.

- ❌ :  "Configure a Network ACL on the database subnet to allow all traffic from the application subnet"

  is incorrect. This does not restrict access specifically to the application instances.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #database_security_group #database_port #database_subnet #application_security_group #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>-
