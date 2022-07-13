#### SCALING BASED ON AMAZON SQS

Can also scale based on an Amazon Simple Queue Service (SQS) queue.

This comes up as an exam question for SAA-C02.

Uses a custom metric that’s sent to Amazon CloudWatch that measures the number
of messages in the queue per EC2 instance

in the Auto Scaling group.

Then use a target tracking policy that configures your Auto Scaling group to
scale based on the custom metric and a set

target value. CloudWatch alarms invoke the scaling policy.

Use a custom “backlog per instance” metric to track not just the number of
messages in the queue but the number

available for retrieval.

Can base off the SQS Metric “ApproximateNumberOfMessages”.

