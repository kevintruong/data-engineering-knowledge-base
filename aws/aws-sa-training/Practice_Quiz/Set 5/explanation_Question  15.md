**Explanation:**

You can build a hub-and-spoke topology with AWS Transit Gateway that supports transitive routing. This simplifies the

network topology and adds additional features over VPC peering. AWS Resource Access Manager can be used to share the

connection with the other AWS accounts.

- ✅ :  "Create an AWS Transit Gateway and share it with each account using AWS Resource Access Manager" is the

  correct answer.

- ❌ :  "Create a transitive VPC peering connection between each Amazon VPC and configure route tables" is

  incorrect. You cannot create transitive connections with VPC peering.

- ❌ :  "Create an AWS Managed VPN between each Amazon VPC and configure route tables" is incorrect. This is a much

  more complex solution compared to AWS Transit Gateway so is not the best option.

- ❌ :  "Create a hub-and-spoke topology with AWS App Mesh and use AWS Resource Access Manager to share route

  tables" is incorrect. AWS App Mesh is used for application-level networking for microservices applications.

**References:**

<https://aws.amazon.com/blogs/aws/new-use-an-aws-transit-gateway-to-simplify-your-network-architecture/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----

- #aws_transit_gateway #<https://aws.amazon.com/blogs/aws/new-use-an-aws-transit-gateway-to-simplify-your-network-architecture/> #aws_app_mesh #amazon_vpc #other_aws_accounts
