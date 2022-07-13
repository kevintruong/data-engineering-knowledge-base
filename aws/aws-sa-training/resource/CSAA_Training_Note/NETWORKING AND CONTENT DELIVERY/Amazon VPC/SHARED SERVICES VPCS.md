#### SHARED SERVICES VPCS


You can allow other AWS accounts to create their application resources, such as EC2 instances, Relational Database

Service (RDS) databases, Redshift clusters, and Lambda functions, into shared, centrally-managed Amazon Virtual Private

Clouds (VPCs).


VPC sharing enables subnets to be shared with other AWS accounts within the same AWS Organization. **Benefits include:**


- Separation of duties: centrally controlled VPC structure, routing, IP address allocation.

- Application owners continue to own resources, accounts, and security groups.

- VPC sharing participants can reference security group IDs of each other.

- Efficiencies: higher density in subnets, efficient use of VPNs and AWS Direct Connect.

- Hard limits can be avoided, for example, 50 VIFs per AWS Direct Connect connection through simplified network

  architecture.

- Costs can be optimized through reuse of NAT gateways, VPC interface endpoints, and intra- Availability Zone traffic.


You can create separate Amazon VPCs for each account with the account owner being responsible for connectivity and

security of each Amazon VPC.


With VPC sharing, your IT team can own and manage your Amazon VPCs and your application developers no longer have to

manage or configure Amazon VPCs, but they can access them as needed.


Can also share Amazon VPCs to leverage the implicit routing within a VPC for applications that


require a high degree of interconnectivity and are within the same trust boundaries.


This reduces the number of VPCs that need to be created and managed, while you still benefit from using separate

accounts for billing and access control.


Customers can further simplify network topologies by interconnecting shared Amazon VPCs using connectivity features,

such as AWS PrivateLink, AWS Transit Gateway, and Amazon VPC peering.


Can also be used with AWS PrivateLink to secure access to resources shared such as applications behind a Network Load

Balancer.

