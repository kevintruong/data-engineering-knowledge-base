---
up: [[Dedicated instances]]
up: [[EC2 BILLING AND PROVISIONING]]
---
## Dedicated instance billing

Partial instance - hours consumed are billed based on instance usage.

Instances are billed when they’re in a ||running state|| – need to stop or terminate to avoid paying.

Charging by ||the hour or second|| (by the second with Linux instances only).

Data between instances in {{c3::different regions}} is charged (in and out).

Regional Data Transfer rates apply if at least one of the following is true, but are only charged once for a given instance even if both are true:
- The other instance is in a different Availability Zone, regardless of which type of address is used.
- Public or Elastic IP addresses are used, regardless of which Availability Zone the other instance is in.
