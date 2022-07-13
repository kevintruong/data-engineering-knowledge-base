*

**Explanation:**

The 2xlarge instance type provides more CPUs. The best answer is to use this instance type for all instances as the CPU

utilization has been lower.

* ✅ :  "Change the configuration to use only c4.2xlarge instance types" is the correct answer.

* ❌ :  "Enable the weighted routing policy on the ELB and configure a higher weighting for the c4.2xlarge

  instances" is incorrect. The weighted routing policy is a Route 53 feature that would not assist in this situation.

* ❌ :  "Add all of the instances into a Placement Group" is incorrect. A placement group helps provide low-latency

  connectivity between instances and would not help here.

* ❌ :  "Add more c5.large instances to spread the load more evenly" is incorrect. This would not help as this

  instance type is underperforming with high CPU utilization rates.

**References:**

<https://aws.amazon.com/ec2/instance-types/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

----
* #more_c5.large_instances #<https://aws.amazon.com/ec2/instance-types/> #c4.2xlarge_instance_types #instances #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>
