#### BILLING AND PROVISIONING

**On demand:**

- Pay for hours used with no commitment.

- Low cost and flexibility with no upfront cost.

- Ideal for auto scaling groups and unpredictable workloads.

- Good for dev/test.

**Spot:**

- Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity in the
  AWS cloud.

- Spot Instances are available at up to a 90% discount compared to On-Demand
  prices.

- You can use Spot Instances for various stateless, fault-tolerant, or flexible
  applications such as big data,

  containerized workloads, CI/CD, web servers, high-performance computing

  (HPC), and other test & development workloads.

- You can request Spot Instances by using the Spot management console, CLI, API
  or the same interface that is used for

  launching On-Demand instances by indicating the option to use Spot.

- You can also select a Launch Template or a pre-configured or custom Amazon
  Machine Image (AMI), configure security and

  network access to your Spot instance, choose from multiple instance types and
  locations, use static IP endpoints, and

  attach persistent block storage to your Spot instances.

- **New pricing model:** The Spot price is determined by long term trends in
  supply and demand for EC2 spare capacity.

- You don’t have to bid for Spot Instances in the new pricing model, and you
  just pay the Spot price that’s in effect

  for the current hour for the instances that you launch.

- Spot Instances receive a two-minute interruption notice when these instances
  are about to be reclaimed by EC2, because

  EC2 needs the capacity back.

- Instances are not interrupted because of higher competing bids.

- To reduce the impact of interruptions and optimize Spot Instances, diversify
  and run your application across multiple

  capacity pools.

- Each instance family, each instance size, in each Availability Zone, in every
  Region is a separate Spot pool.

- You can use the RequestSpotFleet API operation to launch thousands of Spot
  Instances and diversify resources

  automatically.

- To further reduce the impact of interruptions, you can also set up Spot
  Instances and Spot Fleets to respond to an

  interruption notice by stopping or hibernating rather than terminating
  instances when capacity is no longer available.

**Reserved:**

- Purchase (or agree to purchase) usage of EC2 instances in advance for
  significant discounts over On-Demand pricing.


- Provides a capacity reservation when used in a specific AZ.

- AWS Billing automatically applies discounted rates when you launch an instance
  that matches your purchased RI.

- Capacity is reserved for a term of 1 or 3 years.

- EC2 has three RI types: Standard, Convertible, and Scheduled.

- Standard = commitment of 1 or 3 years, charged whether it’s on or off.

- Scheduled = reserved for specific periods of time, accrue charges hourly,
  billed in monthly increments over the term (

  1 year).

- Scheduled RIs match your capacity reservation to a predictable recurring
  schedule.

- For the differences between standard and convertible RIs, see the table below.

- RIs are used for steady state workloads and predictable usage.

- Ideal for applications that need reserved capacity.

- Upfront payments can reduce the hourly rate.

- Can switch AZ within the same region.

- Can change the instance size within the same instance type.

- Instance type modifications are supported for Linux only.

- Cannot change the instance size of Windows RIs.

- Billed whether running or not.

- Can sell reservations on the AWS marketplace.

- Can be used in Auto Scaling Groups.

- Can be used in Placement Groups.

- Can be shared across multiple accounts within Consolidated Billing.

- If you don’t need your RI’s, you can try to sell them on the Reserved Instance
  Marketplace.

**RI Attributes:**

- Instance type – designates CPU, memory, networking capability.

- Platform – Linux, SUSE Linux, RHEL, Microsoft Windows, Microsoft SQL Server.

- Tenancy – Default (shared) tenancy, or Dedicated tenancy.

- Availability Zone (optional) – if AZ is selected, RI is reserved, and discount
  applies to that AZ

  (Zonal RI). If no AZ is specified, no reservation is created but the discount
  is applied to any

```

instance in the family in any AZ in the region (Regional RI).

```

**Comparing Amazon EC2 Pricing Models**

The following table provides a brief comparison of On-demand, Reserved and Spot
pricing models:

```

On-Demand Reserved Spot

No upfront fee Options: No upfront, partial

upfront or all upfront

```

```

No upfront fee

```

```

Charged by hour or second Charged by hour or second Charged by hour or second

No commitment 1 - year or 3 - year commitment No commitment

Ideal for short term needs or

unpredictable workloads

```

```

Ideal for steady-state

workloads and predictable

usage

```

```

Ideal for cost-sensitive,

compute intensive use cases

that can withstand

interruption

```

**Dedicated hosts:**

- Physical servers dedicated just for your use.

- You then have control over which instances are deployed on that host.

- Available as On-Demand or with Dedicated Host Reservation.

- Useful if you have server-bound software licences that use metrics like
  per-core, per-socket, or per-VM.

- Each dedicated host can only run one EC2 instance size and type.

- Good for regulatory compliance or licensing requirements.

- Predictable performance.

- Complete isolation.

- Most expensive option.

- Billing is per host.

**Dedicated instances:**

- Virtualized instances on hardware just for you.

- Also uses physically dedicated EC2 servers.

- Does not provide the additional visibility and controls of dedicated hosts (
  e.g. how instance are placed on a server).

- Billing is per instance.

- May share hardware with other non-dedicated instances in the same account.

- Available as On-Demand, Reserved Instances, and Spot Instances.

- Cost additional $2 per hour per region.

The following table describes some of the differences between dedicated
instances and dedicated hosts:

Partial instance- hours consumed are billed based on instance usage.

Instances are billed when they’re in a running state – need to stop or terminate
to avoid paying.

Charging by the hour or second (by the second with Linux instances only).

Data between instances in different regions is charged (in and out).

Regional Data Transfer rates apply if at least one of the following is true, but
are only charged once for a given

instance even if both are true:

- The other instance is in a different Availability Zone, regardless of which
  type of address is used.

- Public or Elastic IP addresses are used, regardless of which Availability Zone
  the other instance is in.

