#### Question  2


**Three AWS accounts are owned by the same company but in different regions. Account Z has two AWS Direct Connect

connections to two separate company offices. Accounts A and B require the ability to route across account Z’s Direct

Connect connections to each company office. A Solutions Architect has created an AWS Direct Connect gateway in account

Z.**


**How can the required connectivity be configured?**


1: Associate the Direct Connect gateway to a transit gateway in each region


2: Associate the Direct Connect gateway to a virtual private gateway in account A and B


3: Create a VPC Endpoint to the Direct Connect gateway in account A and B


4: Create a PrivateLink connection in Account Z and ENIs in accounts A and B


Answer: 2


**Explanation:**


You can associate an _AWS Direct Connect gateway_ with either of the following gateways:


- A transit gateway when you have multiple VPCs in the same Region.

- A virtual private gateway.


In this case account Z owns the Direct Connect gateway so a VPG in accounts A and B must be associated with it to enable

this configuration to work. After Account Z accepts the proposals, Account A and Account B can route traffic from their

virtual private gateway to the Direct Connect gateway.


- CORRECT "Associate the Direct Connect gateway to a virtual private gateway in account A and B" is the correct answer.


- INCORRECT "Associate the Direct Connect gateway to a transit gateway in each region" is incorrect. This would be a

  good solution if the accounts were in VPCs within a region rather than across regions.


- INCORRECT "Create a VPC Endpoint to the Direct Connect gateway in account A and B" is incorrect. You cannot create a

  VPC endpoint for Direct Connect gateways.


- INCORRECT "Create a PrivateLink connection in Account Z and ENIs in accounts A and B" is incorrect. You cannot use

  PrivateLink connections to publish a Direct Connect gateway.


**References:**


https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/aws-direct-connect/

