**Explanation:**

To prevent direct connectivity to the EC2 instances from the internet you can deploy your EC2 instances in a private

subnet and have the ELB in a public subnet. To configure this you must enable a public subnet in the ELB that is in the

same AZ as the private subnet.

- ✅ :  "Launch the EC2 instances in a private subnet and create an Application Load Balancer in a public subnet"

  is the correct answer.

- ❌ :  "Launch the EC2 instances in a private subnet with a NAT gateway and update the route table" is incorrect.

  This configuration will not allow the application to be accessible from the internet, the aim is to only prevent

  direct access to the EC2 instances.

- ❌ :  "Launch the EC2 instances in a public subnet and use AWS WAF to protect the instances from internet-based

  attacks" is incorrect. With the EC2 instances in a public subnet, direct access from the internet is possible. It only

  takes a security group misconfiguration or software exploit and the instance becomes vulnerable to attack.

- ❌ :  "Launch the EC2 instances in a public subnet and create an Application Load Balancer in a public subnet"

  is incorrect. The EC2 instances should be launched in a private subnet.

**References:**

<https://aws.amazon.com/premiumsupport/knowledge-center/public-load-balancer-private-ec2/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #ec2_instances #aws_waf #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>- #elb #application_load_balancer
