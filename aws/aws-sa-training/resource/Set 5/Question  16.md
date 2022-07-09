#### Question  16


**An organization is planning their disaster recovery solution. They would like to keep their core business critical

systems running in the cloud. Other services can be replicated but switched off.**


**Which DR strategy should a Solutions Architect recommend?**


1: Backup and restore


2: Pilot light


3: Warm standby


4: Multi-site


Answer: 3


**Explanation:**


The term warm standby is used to describe a DR scenario in which a scaled-down version of a fully functional environment

is always running in the cloud. A warm standby solution extends the pilot light elements and preparation.


It further decreases the recovery time because some services are always running. By identifying your business- critical

systems, you can fully duplicate these systems on AWS and have them always on.


- CORRECT "Warm standby" is the correct answer.


- INCORRECT "Backup and restore" is incorrect. This is the lowest cost DR approach that simply entails creating online

  backups of all data and applications.


- INCORRECT Pilot light"" is incorrect. With a pilot light strategy a core minimum of services are running and the

  remainder are only brought online during a disaster recovery situation.


- INCORRECT "Multi-site" is incorrect. A multi-site solution runs on AWS as well as on your existing on-site

  infrastructure in an active- active configuration.


**References:**


https://aws.amazon.com/blogs/publicsector/rapidly-recover-mission-critical-systems-in-a-disaster/

