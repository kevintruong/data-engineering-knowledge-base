**Explanation:**

VPCs can be shared among multiple AWS accounts. Resources can then be shared amongst those accounts. However, to

restrict access so that consumers cannot connect to other instances in the VPC the best solution is to use PrivateLink

to create an endpoint for the application. The endpoint type will be an interface endpoint and it uses an NLB in the

shared services VPC.

- ✅ :  "Create a Network Load Balancer (NLB)" is a correct answer.

- ✅ :  "Use AWS PrivateLink to expose the application as an endpoint service" is also a correct answer.

- ❌ :  "Use AWS ClassicLink to expose the application as an endpoint service" is incorrect. ClassicLink allows you

  to link EC2-Classic instances to a VPC in your account, within the same region. This solution does not include

  EC2-Classic which is now deprecated (replaced by VPC).

- ❌ :  "Setup VPC peering between each AWS VPC" is incorrect. VPC peering could be used along with security groups

  to restrict access to the application and other instances in the VPC. However, this would be administratively

  difficult as you would need to ensure that you maintain the security groups as resources and addresses change.

- ❌ :  "Configure security groups to restrict access" is incorrect. This could be used in conjunction with VPC

  peering but better method is to use PrivateLink for this use case.

**References:**

<https://aws.amazon.com/about-aws/whats-new/2018/12/amazon-virtual-private-clouds-can-now-be-shared>-

with-other-aws-accounts/

<https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple>-

accounts-and-vpc-management/

<https://d1.awsstatic.com/whitepapers/aws-privatelink.pdf>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----

- #aws_vpc #<https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple>>- #vpc_peering #aws_classiclink #aws_privatelink
