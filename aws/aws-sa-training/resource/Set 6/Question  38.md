#### Question  38


**A Solutions Architect has created an AWS account and selected the Asia Pacific (Sydney) region. Within the default VPC

there is a default security group. What settings are configured within this security group by default? (Select TWO)**


1: There is an inbound rule that allows all traffic from the security group itself


2: There is an inbound rule that allows all traffic from any address


3: There is an outbound rule that allows all traffic to the security group itself


4: There is an outbound rule that allows all traffic to all addresses


5: There is an outbound rule that allows traffic to the VPC router


**Answer: 1,4**


SQS Queue


Consumer


Producer


```

Short polling checks

a subset of servers

and may not return

all messages

```


1


5


3


2


```

Long polling waits for the

Wai t Ti meSec ondsand

eliminates empty responses

```


**Explanation:**


Default security groups have inbound allow rules (allowing traffic from within the group) whereas custom security groups

do not have inbound allow rules (all inbound traffic is denied by default). All outbound traffic is allowed by default

in custom and default security groups.


- CORRECT "There is an inbound rule that allows all traffic from the security group itself" is a correct answer.


- CORRECT "There is an outbound rule that allows all traffic to all addresses" is also a correct answer.


- INCORRECT "There is an inbound rule that allows all traffic from any address" is incorrect as explained above.


- INCORRECT "There is an outbound rule that allows all traffic to the security group itself" is incorrect as explained

  above.


- INCORRECT "There is an outbound rule that allows traffic to the VPC router" is incorrect as explained above.


**References:**


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-vpc/

