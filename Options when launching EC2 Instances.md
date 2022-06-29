---
up: [[EC2]]
---

### **Options when launching EC2 Instances**
- Choose whether to auto-assign a public IP – default is to use the subnet setting.
- Can add an instance to a placement group.
- Instances can be assigned to IAM roles which configures them with credentials to access AWS resources.
- {{c1::Termination protection}} can be enabled and prevents you from terminating an instance.
- {{c2::Basic}} monitoring is enabled by default ( 5 - minute periods),
- {{c3::detailed}} monitoring can be enabled (1 minute periods, chargeable).
- Can define shared or dedicated tenancy.
- T2 unlimited allows applications to burst past CPU performance baselines as required (chargeable).
- Can add a script to run on startup (user data).
- Can join to a directory (Windows instances only).
- There is an option to enable an Elastic GPU (Windows instances only).
- Storage options include adding {{c4::additional volumes}} and choosing the volume type.
- Non-root volumes can be encrypted.
- Root volumes can be {{c5::encrypted}} if the instance is launched from an encrypted AMI.
- There is an option to create tags (or can be done later).
- You can select an existing security group or create a new one.
- You must create or use an existing key pair – this is required.