#### Question  53


**An Amazon EBS-backed EC2 instance has been launched. A requirement has come up for some high- performance ephemeral

storage.**


**How can a Solutions Architect add a new instance store volume?**


1: You must shutdown the instance in order to be able to add the instance store volume


2: You must use an Elastic Network Adapter (ENA) to add instance store volumes. First, attach an ENA, and then attach

the instance store volume


3: You can specify the instance store volumes for your instance only when you launch an instance


4: You can use a block device mapping to specify additional instance store volumes when you launch your instance, or you

can attach additional instance store volumes after your instance is running


**Answer: 3**


**Explanation:**


You can specify the instance store volumes for your instance only when you launch an instance. You can’t attach instance

store volumes to an instance after you’ve launched it.


- CORRECT "You can specify the instance store volumes for your instance only when you launch an instance" is the correct

  answer.


- INCORRECT "You must shutdown the instance in order to be able to add the instance store volume" is incorrect. You can

  use a block device mapping to specify additional EBS volumes when you launch your instance, or you can attach

  additional EBS volumes after your instance is running.


- INCORRECT "You must use an Elastic Network Adapter (ENA) to add instance store volumes. First, attach an ENA, and then

  attach the instance store volume" is incorrect. An Elastic Network Adapter has nothing to do with adding instance

  store volumes.


- INCORRECT "You can use a block device mapping to specify additional instance store volumes when you launch your

  instance, or you can attach additional instance store volumes after your instance is running" is incorrect. You can’t

  attach instance store volumes to an instance after you’ve launched it.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-instance-store-volumes.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

