---
up: [[EC2 Spot instance billing]]
---

#### **EC2 Spot New pricing model:**
- The Spot price is determined by long term trends in supply and demand for EC2 spare capacity.
- You don’t have to bid for Spot Instances in the new pricing model, and you just pay the Spot price that’s in effect for the current hour for the instances that you launch.
- Spot Instances receive a **two-minute interruption notice** when these instances are about to be reclaimed by EC2, because EC2 needs the capacity back.
- Instances are **not interrupted** because of higher competing bids.
- To reduce the impact of interruptions and optimize Spot Instances, diversify and run your application across **multiple capacity pools**.
- Each instance family, each instance size, in each Availability Zone, in every Region is a separate Spot pool.
- You can use the RequestSpotFleet API operation to launch thousands of Spot Instances and diversify resources automatically.
- To further reduce the impact of interruptions, you can also set up Spot Instances and Spot Fleets to respond to an interruption notice by stopping or hibernating rather than terminating instances when capacity is no longer available.