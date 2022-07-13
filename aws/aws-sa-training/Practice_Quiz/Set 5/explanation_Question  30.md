*

**Explanation:**

A launch configuration is the template used to create new EC2 instances and includes parameters such as instance family,

instance type, AMI, key pair and security groups.

You cannot edit a launch configuration once defined. In this case you can create a new launch configuration that uses

the new AMI and any new instances that are launched by the ASG will use the new AMI.

* ✅ :  "Create a new launch configuration that uses the AMI and update the ASG to use the new launch configuration"

  is the correct answer.

* ❌ :  "Create a new target group that uses a new launch configuration with the new AMI" is incorrect. A target

  group is a concept associated with an ELB not Auto Scaling.

* ❌ :  "Modify the existing launch configuration to add the new AMI" is incorrect as you cannot modify an existing

  launch configuration.

* ❌ :  "Suspend Auto Scaling and replace the existing AMI" is incorrect. Suspending scaling processes can be useful

  when you want to investigate a configuration problem or other issue with your web application and then make changes to

  your application, without invoking the scaling processes. It is not useful in this situation.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/>

----
* #<https://docs.aws.amazon.com/autoscaling/ec2/userguide/launchconfiguration.html> #new_ec2_instances #new_ami #new_launch_configuration #new_instances
