#### AWS involvement to repair.

Instance status checks (StatusCheckFailed_Instance) detect problems that
require **your** involvement to repair.

Status checks are built into Amazon EC2, so they cannot be disabled or deleted.

You can, however, create or delete alarms that are triggered based on the result
of the status checks.

You can create Amazon CloudWatch alarms that monitor Amazon EC2 instances and
automatically perform an action if the

status check fails.

**Actions can include:**

- Recover the instance (only supported on specific instance types and can be
  used only with StatusCheckFailed_System).

- Stop the instance (only applicable to EBS-backed volumes).

- Terminate the instance (cannot terminate if termination protection is enabled)
  .

- Reboot the instance.

It is a best practice to use EC2 to reboot instance rather than the OS (create a
CloudWatch record).

**CloudWatch Monitoring frequency:**

- Standard monitoring = 5 mins

- Detailed monitoring = 1 min (chargeable)

