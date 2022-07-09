#### Question  21


**A large multinational retail company has a presence in AWS in multiple regions. The company has established a new

office and needs to implement a high-bandwidth, low-latency connection to multiple VPCs in multiple regions within the

same account. The VPCs each have unique CIDR ranges.**


**What would be the optimum solution design using AWS technology? (Select TWO)**


1: Configure AWS VPN CloudHub


2: Create a Direct Connect gateway, and create private VIFs to each region


3: Provision an MPLS network


```

AWS Lambda

```


```

User /

application

Images Bucket

```


```

Resized Images

Bucket

```


```

Jpg image upload

```


```

Amazon CloudWatch

```


```

Event written to

CloudWatch Logs S 3 notifies Lambda

```


```

Note: Supported push notification

services include: S 3 , SNS, SES,

Cognito, CloudFormation,

CloudWatch Logs, CloudWatch

Events, CodeCommit, Scheduled

Events, Config, Alexa, Lex, API

Gateway, IoT Button, CloudFront,

Kinesis Data Firehose

```


```

Region

```


4: Implement Direct Connect connections to each AWS region


5: Implement a Direct Connect connection to the closest AWS region


**Answer: 2,5**


**Explanation:**


The company should implement an AWS Direct Connect connection to the closest region. A Direct Connect gateway can then

be used to create private virtual interfaces (VIFs) to each AWS region.


Direct Connect gateway provides a grouping of Virtual Private Gateways (VGWs) and Private Virtual Interfaces

(VIFs) that belong to the same AWS account and enables you to interface with VPCs in any AWS Region (except AWS China

Region).


You can share a private virtual interface to interface with more than one Virtual Private Cloud (VPC) reducing the

number of BGP sessions required.


- CORRECT "Create a Direct Connect gateway, and create private VIFs to each region" is a correct answer.


- CORRECT "Implement a Direct Connect connection to the closest AWS region" is also a correct answer.


- INCORRECT "Configure AWS VPN CloudHub" is incorrect. AWS VPN CloudHub is not the best solution as you have been asked

  to implement high-bandwidth, low-latency connections and VPN uses the Internet so is not reliable.


- INCORRECT "Provision an MPLS network" is incorrect. An MPLS network could be used to create a network topology that

  gets you closer to AWS in each region but you would still need use Direct Connect or VPN for the connectivity into

  AWS. Also, the question states that you should use AWS technology and MPLS is not offered as a service by AWS.


- INCORRECT "Implement Direct Connect connections to each AWS region" is incorrect. You do not need to implement

  multiple Direct Connect connections to each region. This would be a more expensive option as you would need to pay for

  an international private connection.


**References:**


https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/aws-direct-connect/

