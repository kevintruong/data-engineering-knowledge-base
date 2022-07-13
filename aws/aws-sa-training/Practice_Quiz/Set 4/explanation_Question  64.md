*

**Explanation:**

You can suspend and then resume one or more of the scaling processes for your Auto Scaling group. This can be useful

when you want to investigate a configuration problem or other issue with your web application and then make changes to

your application, without invoking the scaling processes. You can manually move an instance from an ASG and put it in

the standby state

Instances in standby state are still managed by Auto Scaling, are charged as normal, and do not count towards available

EC2 instance for workload/application use. Auto scaling does not perform health checks on instances in the standby

state. Standby state can be used for performing updates/changes/troubleshooting etc. without health checks being

performed or replacement instances being launched.

* ✅ :  "Place the EC2 instance that is experiencing issues into the Standby state" is a correct answer.

* ✅ :  "Suspend the scaling processes responsible for launching new instances" is also a correct answer.

* ❌ :  "Remove the EC2 instance from the Target Group" is incorrect. Target Groups are features of ELB

  (specifically ALB/NLB). Removing the instance from the target group will stop the ELB from sending connections to it

  but will not stop Auto Scaling from launching new instances while you are troubleshooting it.

* ❌ :  "Disable the launch configuration associated with the EC2 instance" is incorrect. You cannot disable the

  launch configuration and you can’t modify a launch configuration after you’ve created it.

* ❌ :  "Disable the dynamic scaling policy" is incorrect. You do not need to disable the dynamic scaling policy;

  you can just suspend it as previously described.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

----
* #<https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html> #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #ec2_instance #auto_scaling_group #auto_scaling
