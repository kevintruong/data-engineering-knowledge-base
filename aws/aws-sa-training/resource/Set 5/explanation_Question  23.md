*

**Explanation:**

An Interface endpoint uses AWS PrivateLink and is an elastic network interface (ENI) with a private IP address that

serves as an entry point for traffic destined to a supported service. Using PrivateLink you can connect your VPC to

supported AWS services, services hosted by other AWS accounts (VPC endpoint services), and supported AWS Marketplace

partner services.

* ✅ :  "Create a private API using an interface VPC endpoint" is the correct answer.

* ❌ :  "Create a NAT gateway" is incorrect. NAT Gateways are used to provide Internet access for EC2 instances in

  private subnets so are of no use in this solution.

* ❌ :  "Create a public VIF on a Direct Connect connection" is incorrect. You do not need to implement Direct

  Connect and create a public VIF. Public IP addresses are used in public VIFs and the question requests that only

  private addresses are used.

* ❌ :  "Add the API gateway to the subnet the EC2 instances are located in" is incorrect. You cannot add API

  Gateway to the subnet the EC2 instances are in, it is a public service with a public endpoint.

**References:**

<https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #interface_vpc_endpoint #vpc_endpoint_services #aws_services #elastic_network_interface #aws_marketplace
