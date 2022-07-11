**Explanation:**

Scaling based on a schedule allows you to set your own scaling schedule for predictable load changes. To configure your

Auto Scaling group to scale based on a schedule, you create a scheduled action. This is ideal for situations where you

know when and for how long you are going to need the additional capacity.

- ✅ :  "Add a Scheduled Scaling action" is the correct answer.

```

Producers capture and

send data to Kinesis

```

```

Shards

```

```

Stream Consumers (EC 2 ) Amazon S 3

```

```

Amazon DynamoDB

Amazon RedShift

```

```

Amazon EMR

```

```

Kinesis Firehose

```

```

Destinations

```

```

Data is captured and

stored for processing

```

```

Analytics Tools

```

- ❌ :  "Add a Step Scaling policy" is incorrect. Step scaling policies increase or decrease the current capacity of

  your Auto Scaling group based on a set of scaling adjustments, known as step adjustments. The adjustments vary based

  on the size of the alarm breach. This is more suitable to situations where the load unpredictable.

- ❌ :  "Add a Simple Scaling policy" is incorrect. AWS recommend using step over simple scaling in most cases. With

  simple scaling, after a scaling activity is started, the policy must wait for the scaling activity or health check

  replacement to complete and the cooldown period to expire before responding to additional alarms (in contrast to step

  scaling). Again, this is more suitable to unpredictable workloads.

- ❌ :  "Add Amazon EC2 Spot instances" is incorrect. Adding spot instances may decrease EC2 costs but you still

  need to ensure they are available. The main requirement of the question is that the performance issues are resolved

  rather than the cost being minimized.

**References:**

**<https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html>**

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----

- #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #own_scaling_schedule #scaling_activity #step_scaling_policy #step_scaling_policies
