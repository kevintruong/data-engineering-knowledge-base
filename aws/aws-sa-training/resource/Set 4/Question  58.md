#### Question  58


**A Solutions Architect created a new VPC and setup an Auto Scaling Group to maintain a desired count of 2 Amazon EC2

instances. The security team has requested that the EC2 instances be located in a private subnet. To distribute load, an

Internet-facing Application Load Balancer (ALB) is also required.**


**With the security team’s requirements in mind, what else needs to be done to get this configuration to work? (Select

TWO)**


1: Attach an Internet Gateway to the private subnets


2: Associate the public subnets with the ALB


3: Add an Elastic IP address to each EC2 instance in the private subnet


4: Add a NAT gateway to the private subnet


5: For each private subnet create a corresponding public subnet in the same AZ


**Answer: 2,5**


**Explanation:**


ELB nodes have public IPs and route traffic to the private IP addresses of the EC2 instances. You need one public subnet

in each AZ where the ELB is defined and the private subnets are located


- CORRECT "Associate the public subnets with the ALB" is a correct answer.


- CORRECT "For each private subnet create a corresponding public subnet in the same AZ" is also a correct answer.


- INCORRECT "Attach an Internet Gateway to the private subnets" is incorrect. Attaching an Internet gateway

  (which is done at the VPC level, not the subnet level) or a NAT gateway will not assist as these are both used for

  outbound communications which is not the goal here.


- INCORRECT "Add an Elastic IP address to each EC2 instance in the private subnet" is incorrect. ELBs talk to the

  private IP addresses of the EC2 instances so adding an Elastic IP address to the instance won’t help. Additionally,

  Elastic IP addresses are used in public subnets to allow Internet access via an Internet Gateway.


- INCORRECT "Add a NAT gateway to the private subnet" is incorrect as this would only enable outbound internet access.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/public-load-balancer-private-ec2/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-

balancing/

