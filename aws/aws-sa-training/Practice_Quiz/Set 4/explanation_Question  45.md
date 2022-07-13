*

**Explanation:**

The key requirements here are that you need to temporarily deploy a large number of instances, can tolerate an delay (

not time-critical), and need the most economical solution. In this case Spot instances are likely to be the most

economical solution.

You must be able to tolerate delays if using Spot instances as if the market price increases your instances will be

terminated and you may have to wait for the price to lower back to your budgeted allowance.

* ✅ :  "Use Spot instances" is the correct answer.

* ❌ :  "Use dedicated hosts" is incorrect. An EC2 Dedicated Host is a physical server with EC2 instance capacity

  fully dedicated to your use. They are much more expensive than on-demand or Spot instances and are used for use cases

  such as bringing your own socket-based software licences to AWS or for compliance reasons.

* ❌ :  "Use On-Demand instances" is incorrect. On-demand is good for temporary deployments when you cannot tolerate

  any delays (instances being terminated by AWS). It is likely to be more expensive than Spot however so if delays can

  be tolerated it is not the best solution.

* ❌ :  "Use Reserved instances" is incorrect. Reserved instances are used for longer more stable requirements where

  you can get a discount for a fixed 1 or 3 year term. This pricing model is not good for temporary requirements.

**References:**

<https://aws.amazon.com/ec2/pricing/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

----
* #ec2_instance_capacity #ec2_dedicated_host #spot_instances #<https://aws.amazon.com/ec2/pricing/_>> #aws
