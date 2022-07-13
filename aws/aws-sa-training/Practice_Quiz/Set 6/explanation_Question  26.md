*

**Explanation:**

When you launch an instance in Amazon EC2, you have the option of passing user data to the instance that can be used to

perform common automated configuration tasks and even run scripts after the instance starts. You can pass two types of

user data to Amazon EC2: shell scripts and cloud-init directives

User data is data that is supplied by the user at instance launch in the form of a script and is limited to 16KB.

* ✅ :  "User Data" is the correct answer.

* ❌ :  "Metadata" is incorrect. _Instance metadata_ is data about your instance that you can use to configure or

  manage the running instance. Instance metadata is divided into categories, for example, host name, events, and

  security groups.

* ❌ :  "Run Command" is incorrect. The AWS Systems Manager run command is used to manage the configuration of

  existing instances by using remotely executed commands. User data is better for specifying scripts to run at startup.

* ❌ :  "AWS Config" is incorrect. This service is used to manage the configuration of AWS resources, it does not

  run scripts on instances.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

----
* #instance_metadata #instance_metadata__ #aws_resources #aws_systems_manager #aws_config
