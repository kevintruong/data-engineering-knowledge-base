*

**Explanation:**

This information is stored in the instance metadata on the instance. You can access the instance metadata through a URI

or by using the Instance Metadata Query tool.

The instance metadata is available

at [http://169.254.169.254/latest/meta-data.](http://169.254.169.254/latest/meta-data.)

The Instance Metadata Query tool allows you to query the instance metadata without having to type out the full URI or

category names.

* ✅ :  "Run the command

  “curl [http://169.254.169.254/latest/meta-data/”"](http://169.254.169.254/latest/meta-data/”") is a correct answer.

* ✅ :  "Download and run the Instance Metadata Query Tool" is also a correct answer.

* ❌ :  "Use the EC2 Config service" is incorrect. The EC2 config is not suitable for accessing this information.

* ❌ :  "Run the command

  “curl [http://169.254.169.254/latest/dynamic/instance-identity/”"](http://169.254.169.254/latest/dynamic/instance-identity/”")

  is incorrect. The correct command is provided above.

* ❌ :  "Use the Batch command" is incorrect. The batch command is not suitable for accessing this information.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/>

----
* #instance_metadata_query_tool #instance_metadata #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/> #ec2_config_service #ec2_config
