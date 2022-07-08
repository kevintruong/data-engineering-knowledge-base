---
date created: 2022-07-05 23:16
---

## Quiz 7: An ecommerce website runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The application is stateless and elastic and scales from a minimum of 10 instances, up to a maximum of 200 instances. For at least 80% of the time at least 40 instances are required.**

**Which solution should be used to minimize costs?**

- [ ] Purchase Reserved Instances to cover 200 instances
- [ ] Purchase Reserved Instances to cover 80 instances. Use Spot Instances to cover the remaining instances
- [ ] Purchase On-Demand Instances to cover 40 instances. Use Spot Instances to cover the remaining instances
- [ ] Purchase Reserved Instances to cover 40 instances. Use On-Demand and Spot Instances to cover the remaining instances

---

**Explanation:**
In this case at least 40 instances are required for 80% of the time which means they are good candidates for reserved instances which can provide discounts of up to 72% over on-demand instances. For the remainder of instances on-demand and Spot instances should be used. Spot can be used as the application is stateless and this will minimize costs and on-demand can be used when Spot instances aren’t available or the price is not beneficial.

- ✅: "Purchase Reserved Instances to cover 40 instances. Use On-Demand and Spot Instances to cover the remaining instances" is the correct answer.
- ❌: "Purchase On-Demand Instances to cover 40 instances. Use Spot Instances to cover the remaining instances"

  is incorrect as on-demand instances will not minimize costs. For the instances that will be required at a minimum, reserved instances should be used.
- ❌: "Purchase Reserved Instances to cover 200 instances" is incorrect as these extra instances above 40 instances are only used for less and 20% of the time. It would better to reserve 40 instances only.
- ❌: "Purchase Reserved Instances to cover 80 instances. Use Spot Instances to cover the remaining instances"  is incorrect as only 40 instances should be reserved as these are used 80% of the time. The remainder should be spot instances.
  **References:**
  <https://aws.amazon.com/ec2/pricing/reserved-instances/>

---- 
#quiz 
- relateTo:: [[Domain 4 Design Cost-Optimized Architectures]]