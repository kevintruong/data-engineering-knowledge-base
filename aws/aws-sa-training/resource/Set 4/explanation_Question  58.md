*

**Explanation:**

ELB nodes have public IPs and route traffic to the private IP addresses of the EC2 instances. You need one public subnet

in each AZ where the ELB is defined and the private subnets are located

* ✅ :  "Associate the public subnets with the ALB" is a correct answer.

* ✅ :  "For each private subnet create a corresponding public subnet in the same AZ" is also a correct answer.

* ❌ :  "Attach an Internet Gateway to the private subnets" is incorrect. Attaching an Internet gateway

  (which is done at the VPC level, not the subnet level) or a NAT gateway will not assist as these are both used for

  outbound communications which is not the goal here.

* ❌ :  "Add an Elastic IP address to each EC2 instance in the private subnet" is incorrect. ELBs talk to the

  private IP addresses of the EC2 instances so adding an Elastic IP address to the instance won’t help. Additionally,

  Elastic IP addresses are used in public subnets to allow Internet access via an Internet Gateway.

* ❌ :  "Add a NAT gateway to the private subnet" is incorrect as this would only enable outbound internet access.

**References:**

<https://aws.amazon.com/premiumsupport/knowledge-center/public-load-balancer-private-ec2/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----
* #elb_nodes #elbs #elb #elastic_ip_addresses #ec2_instances
