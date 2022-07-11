*

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

* ✅ :  "There is an inbound rule that allows all traffic from the security group itself" is a correct answer.

* ✅ :  "There is an outbound rule that allows all traffic to all addresses" is also a correct answer.

* ❌ :  "There is an inbound rule that allows all traffic from any address" is incorrect as explained above.

* ❌ :  "There is an outbound rule that allows all traffic to the security group itself" is incorrect as explained

  above.

* ❌ :  "There is an outbound rule that allows traffic to the VPC router" is incorrect as explained above.

**References:**

<https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #inbound_rule #outbound_rule #inbound_traffic #outbound_traffic #sqs_queue
