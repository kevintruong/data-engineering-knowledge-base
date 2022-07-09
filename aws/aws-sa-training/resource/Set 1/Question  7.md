#### Question  7


**An ecommerce website runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The application is

stateless and elastic and scales from a minimum of 10 instances, up to a maximum of 200 instances. For at least 80% of

the time at least 40 instances are required.**


**Which solution should be used to minimize costs?**


1: Purchase Reserved Instances to cover 200 instances


2: Purchase Reserved Instances to cover 80 instances. Use Spot Instances to cover the remaining instances


3: Purchase On-Demand Instances to cover 40 instances. Use Spot Instances to cover the remaining instances


4: Purchase Reserved Instances to cover 40 instances. Use On-Demand and Spot Instances to cover the remaining instances


Answer: 4


**Explanation:**


In this case at least 40 instances are required for 80% of the time which means they are good candidates for reserved

instances which can provide discounts of up to 72% over on-demand instances. For the remainder of instances on-demand

and Spot instances should be used. Spot can be used as the application is stateless and this will minimize costs and

on-demand can be used when Spot instances aren’t available or the price is not beneficial.


- CORRECT "Purchase Reserved Instances to cover 40 instances. Use On-Demand and Spot Instances to cover the remaining

  instances" is the correct answer.


- INCORRECT "Purchase On-Demand Instances to cover 40 instances. Use Spot Instances to cover the remaining instances"

  is incorrect as on-demand instances will not minimize costs. For the instances that will be required at a minimum,

  reserved instances should be used.


- INCORRECT "Purchase Reserved Instances to cover 200 instances" is incorrect as these extra instances above 40

  instances are only used for less and 20% of the time. It would better to reserve 40 instances only.


- INCORRECT "Purchase Reserved Instances to cover 80 instances. Use Spot Instances to cover the remaining instances"

  is incorrect as only 40 instances should be reserved as these are used 80% of the time. The remainder should be spot

  instances.


**References:**


https://aws.amazon.com/ec2/pricing/reserved-instances/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

