#### Question  39


**An application launched on Amazon EC2 instances needs to publish personally identifiable information (PII)

about customers using Amazon SNS. The application is launched in private subnets within an Amazon VPC.**


**Which is the MOST secure way to allow the application to access service endpoints in the same region?**


**1: Use an Internet Gateway**


2: Use AWS PrivateLink


3: Use a proxy instance


4: Use a NAT gateway


Answer: 2


**Explanation:**


To publish messages to Amazon SNS topics from an Amazon VPC, create an interface VPC endpoint. Then, you can publish

messages to SNS topics while keeping the traffic within the network that you manage with the VPC. This is the most

secure option as traffic does not need to traverse the Internet.


- CORRECT "Use AWS PrivateLink" is the correct answer.


- INCORRECT "Use an Internet Gateway" is incorrect. Internet Gateways are used by instances in public subnets to access

  the Internet and this is less secure than an VPC endpoint.


- INCORRECT "Use a proxy instance" is incorrect. A proxy instance will also use the public Internet and so is less

  secure than a VPC endpoint.


- INCORRECT "Use a NAT gateway" is incorrect. A NAT Gateway is used by instances in private subnets to access the

  Internet and this is less secure than an VPC endpoint.


**References:**


https://docs.aws.amazon.com/sns/latest/dg/sns-vpc-endpoint.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

