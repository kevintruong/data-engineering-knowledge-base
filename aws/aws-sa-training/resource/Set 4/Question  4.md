#### Question  4


**A retail organization sends coupons out twice a week and this results in a predictable surge in sales traffic. The

application runs on Amazon EC2 instances behind an Elastic Load Balancer. The organization is looking for ways to reduce

cost without impacting performance or reliability. How can they achieve this goal?**


1: Purchase scheduled reserved instances


2: Use a mixture of spot instances and on demand instances


3: Increase the instance size of the existing EC2 instances


4: Purchase Amazon EC2 dedicated hosts


Answer: 1


**Explanation:**


Scheduled Reserved Instances (Scheduled Instances) enable you to purchase capacity reservations that recur on a daily,

weekly, or monthly basis, with a specified start time and duration, for a one-year term. You reserve


the capacity in advance, so that you know it is available when you need it. You pay for the time that the instances are

scheduled, even if you do not use them.


Scheduled Instances are a good choice for workloads that do not run continuously, but do run on a regular schedule. For

example, you can use Scheduled Instances for an application that runs during business hours or for batch processing that

runs at the end of the week.


- CORRECT "Purchase scheduled reserved instances" is the correct answer.


- INCORRECT "Use a mixture of spot instances and on demand instances" is incorrect. You can mix spot and on- demand in

  an auto scaling group. However, there’s a risk the spot price may not be good and as this is a regular, predictable

  increase in traffic a scheduled reserved instance is a safer option.


- INCORRECT "Increase the instance size of the existing EC2 instances" is incorrect. This would add more cost all of the

  time rather than catering for the temporary increase in traffic.


- INCORRECT "Purchase Amazon EC2 dedicated hosts" is incorrect. This is not a way to save cost as dedicated hosts are

  much more expensive than shared hosts.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-scheduled-instances.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

