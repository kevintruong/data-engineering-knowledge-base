#### ASG BEHAVIOR AND CONFIGURATION

**EC2 Auto Scaling – Termination Policy** :

- Termination policies control which instances are terminated first when a
  scale-in event occurs.

- There is a default termination policy and options for configuring your own
  customized termination policies.

- The default termination policy is designed to help ensure that your instances
  span Availability Zones evenly for high

  availability.

- The default policy is kept generic and flexible to cover a range of scenarios.

You can define Instance Protection which stops Auto Scaling from scaling in and
terminating the instances.

If Auto Scaling fails to launch instances in an AZ it will try other AZs until
successful.

The default health check grace period is 300 seconds.

Scale-out is the process in which EC2 instances are launched by the scaling
policy.

Scale-in is the process in which EC2 instances are terminated by the scaling
policy.

It is recommended to create a scale-in event for each scale-out event created.

Auto Scaling can perform rebalancing when it finds that the number of instances
across AZs is not

balanced.

Auto Scaling rebalances by launching new EC2 instances in the AZs that have
fewer instances first, only then will it

start terminating instances in AZs that had more instances.

Auto Scaling may go over the maximum number of instances by 10% temporarily for
the purposes of rebalancing.

**An imbalance may occur due to:**

- Manually removing AZs/subnets from the configuration.

- Manually terminating EC2 instances.

- EC2 capacity issues.

- Spot price is reached.

**Health checks:**

- By default uses EC2 status checks.

- Can also use ELB health checks and custom health checks.

- ELB health checks are in addition to the EC2 status checks.

- If any health check returns an unhealthy status the instance will be
  terminated.

- With ELB an instance is marked as unhealthy if ELB reports it as OutOfService.

- A healthy instance enters the InService state.

- If an instance is marked as unhealthy it will be scheduled for replacement.

- If connection draining is enabled, Auto Scaling waits for in-flight requests
  to complete or timeout before terminating

  instances.

- The health check grace period allows a period of time for a new instance to
  warm up before performing a health check (

  300 seconds by default).

If using an ELB it is best to enable ELB health checks as otherwise EC2 status
checks may show an instance as being

healthy that the ELB has determined is unhealthy. In this case the instance will
be removed from service by the ELB but

will not be terminated by Auto Scaling.

Elastic IPs and EBS volumes are detached from terminated instances and will need
to be manually reattached.

Using custom health checks a CLI command can be issued to set the instance’s
status to unhealthy, e.g.:

**_aws autoscaling set–instance-health – instance-id i-123abc45d – health-status
Unhealthy_**

Once in a terminating state an EC2 instance cannot be put back into service
again.

However, there is a short time period in which a CLI command can be run to
change an instance to healthy.

Unlike AZ rebalancing, termination of unhealthy instances happens first, then
Auto Scaling attempts to launch new

instances to replace terminated instances.

You can manually remove (detach) instances from an ASG using the AWS Console or
CLI.

When detaching an instance, you can optionally decrement the ASG’s desired
capacity (so it doesn’t launch another

instance).

An instance can be attached to one ASG at a time.

You can suspend and then resume one or more of the scaling processes for your
Auto Scaling group.

Suspending scaling processes can be useful when you want to investigate a
configuration problem or other issue with your

web application and then make changes to your application, without invoking the
scaling processes.

You can manually move an instance from an ASG and put it in the standby state.

Instances in standby state are still managed by Auto Scaling, are charged as
normal, and do not count towards available

EC2 instance for workload/application use.

Auto scaling does not perform health checks on instances in the standby state.

Standby state can be used for performing updates/changes/troubleshooting etc.
without health checks being performed or

replacement instances being launched.

When you delete an ASG the instances will be terminated.

You can choose to use Spot instances in launch configurations and specify a bid
price.

Auto Scaling treats spot instances the same as on-demand instances.

You cannot mix Spot instances with on-demand.

If you want to change the bid price you need to create a new launch
configuration.

**Auto Scaling can be configured to send an SNS email when:**

- An instance is launched.

- An instance is terminated.

- An instance fails to launch.

- An instance fails to terminate.

**Merging ASGs**

- You can merge multiple single AZ Auto Scaling Groups into a single multi-AZ
  ASG.

- Merging can only be performed by using the CLI.

- Process is to rezone one of the groups to cover/span the other AZs for the
  other ASGs.

- Then delete the other ASGs.

- Can be performed on ASGs with or without ELBs attached to them.

- The resulting ASG must be one of the pre-existing ASGs.

**Cooldown Period**

- The cooldown period is a configurable setting for your Auto Scaling group that
  helps to ensure that it doesn’t launch

  or terminate additional instances before the previous scaling activity takes
  effect.

- The default cooldown period is applied when you create your Auto Scaling
  group.

- The default value is 300 seconds.

- You can configure the default cooldown period when you create the Auto Scaling
  group, using the AWS Management

  Console, the create-auto-scaling-group command (AWS CLI), or the
  CreateAutoScalingGroup API operation.

- Automatically applies to dynamic scaling and optionally to manual scaling but
  not supported

```

for scheduled scaling.

```

- Can override the default cooldown via scaling-specific cooldown.

**Scheduled:**

- You cannot configure two scheduled activities at the same date/time.

- Scheduled actions can be edited from the AWS Console or CLI.

- Cooldown timer is not supported for scheduled or step on-demand scaling.

**Dynamic:**

- An alarm is an object that watches over a single metric, e.g.
  CPU/memory/network utilization.

- You need to have a scale-out and a scale-in policy configured.

**Step scaling:**

- Configure multiple steps/adjustments.

- Does not support cool down timers.

- Can respond to multiple alarms and initiate multiple scaling activities.

- Supports a warm-up timer which is the time it will take a newly launched
  instance to be ready.

The warm-up period is the period of time in which a newly created EC2 instance
launched by ASG using step scaling is not

considered toward the ASG metrics.

