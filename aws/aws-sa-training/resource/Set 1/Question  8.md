#### Question  8


**A solutions architect is creating a system that will run analytics on financial data for 4 hours a night, 5 days a

week. The analysis is expected to run for the same duration and cannot be interrupted once it is started. The system

will be required for a minimum of 1 year.**


**Which type of Amazon EC2 instances should be used to reduce the cost of the system?**


1: Spot Instances


2: On-Demand Instances


3: Standard Reserved Instances


4: Scheduled Reserved Instances


Answer: 4


**Explanation:**


Scheduled Reserved Instances (Scheduled Instances) enable you to purchase capacity reservations that recur on a daily,

weekly, or monthly basis, with a specified start time and duration, for a one-year term. You reserve the capacity in

advance, so that you know it is available when you need it. You pay for the time that the instances are scheduled, even

if you do not use them.


Scheduled Instances are a good choice for workloads that do not run continuously, but do run on a regular schedule. For

example, you can use Scheduled Instances for an application that runs during business hours or for batch processing that

runs at the end of the week.


- CORRECT "Scheduled Reserved Instances" is the correct answer.


- INCORRECT "Standard Reserved Instances" is incorrect as the workload only runs for 4 hours a day this would be more

  expensive.


- INCORRECT "On-Demand Instances" is incorrect as this would be much more expensive as there is no discount applied.


- INCORRECT "Spot Instances" is incorrect as the workload cannot be interrupted once started. With Spot instances

  workloads can be terminated if the Spot price changes or capacity is required.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-scheduled-instances.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

