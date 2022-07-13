#### SCALING

The scaling options define the triggers and when instances should be
provisioned/de-provisioned.

**There are four scaling options:**

- Maintain – keep a specific or minimum number of instances running.

- Manual – use maximum, minimum, or a specific number of instances.

- Scheduled – increase or decrease the number of instances based on a schedule.

- Dynamic – scale based on real-time system metrics (e.g. CloudWatch metrics).

The following table describes the scaling options available and when to use
them:

The scaling options are configured through Scaling Policies which determine
when, if, and how the ASG scales and

shrinks.

The following table describes the scaling policy types available for dynamic
scaling policies and when to use them (more

detail further down the page):

The diagram below depicts an Auto Scaling group with a Scaling policy set to a
minimum size of 1 instance, a desired

capacity of 2 instances, and a maximum size of 4 instances:

