**Explanation:**

The solutions architect must enable high availability for the architecture and ensure it is cost-effective. To enable

high availability an Amazon EC2 Auto Scaling group should be created to add and remove instances across multiple

availability zones.

In order to distribute the traffic to the instances the architecture should use a Network Load Balancer which operates

at Layer 4. This architecture will also be cost-effective as the Auto Scaling group will ensure the right number of

instances are running based on demand.

- ✅ :  "Configure a Network Load Balancer in front of the EC2 instances" is a correct answer.

- ✅ :  "Configure an Auto Scaling group to add or remove instances in multiple Availability Zones automatically"

  is also a correct answer.

- ❌ :  "Increase the number of instances and use smaller EC2 instance types" is incorrect as this is not the most

  cost-effective option. Auto Scaling should be used to maintain the right number of active instances.

- ❌ :  "Configure an Auto Scaling group to add or remove instances in the Availability Zone automatically" is

  incorrect as this is not highly available as it’s a single AZ.

- ❌ :  "Configure an Application Load Balancer in front of the EC2 instances" is incorrect as an ALB operates at

  Layer 7 rather than Layer 4.

**References:**

<https://docsaws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----

- #amazon_ec2_auto_scaling_group #<https://docsaws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html> #smaller_ec2_instance_types #ec2_instances #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>>-
