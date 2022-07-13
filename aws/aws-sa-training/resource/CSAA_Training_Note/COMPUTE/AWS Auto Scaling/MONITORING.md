#### MONITORING

Basic monitoring sends EC2 metrics to CloudWatch about ASG instances every 5
minutes.

Detailed can be enabled and sends metrics every 1 minute (chargeable).

When the launch configuration is created from the console basic monitoring of
EC2 instances is enabled by default.

When the launch configuration is created from the CLI detailed monitoring of EC2
instances is enabled by default.

When you enable Auto Scaling group metrics, Auto Scaling sends sampled data to
CloudWatch every minute.

Configure ASG and EC2 monitoring options so they use the same time period, e.g.
detailed monitoring (EC2) and 60

seconds (ASG), or basic monitoring (EC2) and 300 seconds (ASG).

