#### Question  3


**Three Amazon VPCs are used by a company in the same region. The company has two AWS Direct Connect connections to two

separate company offices and wishes to share these with all three VPCs. A Solutions Architect has created an AWS Direct

Connect gateway. How can the required connectivity be configured?**


1: Associate the Direct Connect gateway to a transit gateway


2: Associate the Direct Connect gateway to a virtual private gateway in each VPC


3: Create a VPC peering connection between the VPCs and route entries for the Direct Connect Gateway


4: Create a transit virtual interface between the Direct Connect gateway and each VPC


Answer: 1


**Explanation:**


```

Users in US Amazon Route 53

```


```

Resolve dctlabs.com

```


```

Answer:

51. 45. 2. 12

53. 58. 31. 89

```


```

dctlabs.comin

us-east- 1

```


```

Edge location

```


```

dctlabs.comin

eu-central- 1

```


```

Addresses:

51. 45. 2. 12

53. 58. 31. 89

```


```

Addresses:

51. 45. 2. 12

53. 58. 31. 89

```


```

Uses the AWS

global network

```


```

Static anycast IP

addresses

```


You can manage a single connection for multiple VPCs or VPNs that are in the same Region by associating a Direct Connect

gateway to a transit gateway. The solution involves the following components:


- A transit gateway that has VPC attachments.

- A Direct Connect gateway.

- An association between the Direct Connect gateway and the transit gateway.

- A transit virtual interface that is attached to the Direct Connect gateway.


The following diagram depicts this configuration:


- CORRECT "Associate the Direct Connect gateway to a transit gateway" is the correct answer.


- INCORRECT "Associate the Direct Connect gateway to a virtual private gateway in each VPC" is incorrect. For VPCs in

  the same region a VPG is not necessary. A transit gateway can instead be configured.


- INCORRECT "Create a VPC peering connection between the VPCs and route entries for the Direct Connect Gateway" is

  incorrect. You cannot add route entries for a Direct Connect gateway to each VPC and enable routing. Use a transit

  gateway instead.


- INCORRECT "Create a transit virtual interface between the Direct Connect gateway and each VPC" is incorrect. The

  transit virtual interface is attached to the Direct Connect gateway on the connection side, not the VPC/transit

  gateway side.


**References:**


https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/aws-direct-connect/

