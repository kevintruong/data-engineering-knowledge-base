#### Question  34


**A Solutions Architect is conducting an audit and needs to query several properties of EC2 instances in a VPC. Which

two methods are available for accessing and querying the properties of an EC2 instance such as instance ID, public keys

and network interfaces? (Select TWO)**


1: Use the EC2 Config service


2: Run the command “curl [http://169.254.169.254/latest/meta-data/”](http://169.254.169.254/latest/meta-data/”)


3: Download and run the Instance Metadata Query Tool


4: Run the command

“curl [http://169.254.169.254/latest/dynamic/instance-identity/”](http://169.254.169.254/latest/dynamic/instance-identity/”)


5: Use the Batch command


**Answer: 2,3**


**Explanation:**


This information is stored in the instance metadata on the instance. You can access the instance metadata through a URI

or by using the Instance Metadata Query tool.


The instance metadata is available

at [http://169.254.169.254/latest/meta-data.](http://169.254.169.254/latest/meta-data.)


The Instance Metadata Query tool allows you to query the instance metadata without having to type out the full URI or

category names.


- CORRECT "Run the command

  “curl [http://169.254.169.254/latest/meta-data/”"](http://169.254.169.254/latest/meta-data/”") is a correct answer.


- CORRECT "Download and run the Instance Metadata Query Tool" is also a correct answer.


- INCORRECT "Use the EC2 Config service" is incorrect. The EC2 config is not suitable for accessing this information.


- INCORRECT "Run the command

  “curl [http://169.254.169.254/latest/dynamic/instance-identity/”"](http://169.254.169.254/latest/dynamic/instance-identity/”")

  is incorrect. The correct command is provided above.


- INCORRECT "Use the Batch command" is incorrect. The batch command is not suitable for accessing this information.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

