*

**Explanation:**

The key requirements here are that you need to deploy several EC2 instances quickly to run the batch process and you

must ensure that the job completes. The on-demand pricing model is the best for this ad-hoc

```

Amazon Simple Queue

Service

```

```

Queue

```

```

EC 2 instance

polls SQS

```

```

Web Tier

```

```

Auto Scaling Group

```

```

App Tier

```

```

Auto Scaling Group

Decoupled integration

```

requirement as though spot pricing may be cheaper you cannot afford to risk that the instances are terminated by AWS

when the market price increases.

* ✅ :  "On-demand instances" is the correct answer.

* ❌ :  "Reserved instances" is incorrect. Reserved instances are used for longer more stable requirements where you

  can get a discount for a fixed 1 or 3 year term. This pricing model is not good for temporary requirements.

* ❌ :  "Spot instances" is incorrect. Spot instances provide a very low hourly compute cost and are good when you

  have flexible start and end times. They are often used for use cases such as grid computing and high-performance

  computing (HPC).

* ❌ :  "Flexible instances" is incorrect. There is no such thing as a “flexible instance”.

**References:**

<https://aws.amazon.com/ec2/pricing/>

**Save time with our exam-specific cheat sheets:**

**References:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

----
* #several_ec2_instances #<https://aws.amazon.com/ec2/pricing/_>> #demand_instances #flexible_instances #aws
