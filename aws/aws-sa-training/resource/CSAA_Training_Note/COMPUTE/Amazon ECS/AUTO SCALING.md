#### AUTO SCALING

**Service Auto Scaling**

Amazon ECS service can optionally be configured to use Service Auto Scaling to
adjust the desired task count up or down

automatically.

Service Auto Scaling leverages the Application Auto Scaling service to provide
this functionality.

**Amazon ECS Service Auto Scaling supports the following types of scaling
policies:**

- Target Tracking Scaling Policies—Increase or decrease the number of tasks that
  your service runs based on a target

  value for a specific CloudWatch metric. This is similar to the way that your
  thermostat maintains the temperature of

  your home. You select temperature and the thermostat does the rest.

- Step Scaling Policies—Increase or decrease the number of tasks that your
  service runs in response to CloudWatch

  alarms. Step scaling is based on a set of scaling adjustments, known as step
  adjustments, which vary based on the size

  of the alarm breach.

**Cluster Auto Scaling**

This is a new feature released in December 2019. It is unlikely that this will
appear on the SAA-C01 exam but could

appear on the SAA-C02 exam.

Uses a new ECS resource type called a Capacity Provider.

A Capacity Provider can be associated with an EC2 Auto Scaling Group (ASG).

When you associate an ECS Capacity Provider with an ASG and add the Capacity
Provider to an ECS cluster, the cluster can

now scale your ASG automatically by using two new features of ECS:

1. **Managed scaling** , with an automatically-created scaling policy on your
   ASG, and a new scaling metric (Capacity

   Provider Reservation) that the scaling policy uses; and

2. **Managed instance termination protection** , which enables container-aware
   termination of instances in the ASG when

   scale-in happens.

**SECURITY/SLA**

EC2 instances use an IAM role to access ECS.

IAM can be used to control access at the container level using IAM roles.

The container agent makes calls to the ECS API on your behalf through the
applied IAM roles and policies.

You need to apply IAM roles to container instances before they are launched (EC2
launch type).

AWS recommend limiting the permissions that are assigned to the container
instance’s IAM roles.

Assign extra permissions to tasks through separate IAM roles (IAM Roles for
Tasks).

ECS tasks use an IAM role to access services and resources.

Security groups attach at the instance or container level.

You have root level access to the operating system of the EC2 instances.

The Compute SLA guarantees a Monthly Uptime Percentage of at least 99.99% for
Amazon ECS.

