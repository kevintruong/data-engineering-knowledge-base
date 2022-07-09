#### Question  12


**A company are finalizing their disaster recovery plan. A limited set of core services will be replicated to the DR

site ready to seamlessly take over the in the event of a disaster. All other services will be switched off.**


**Which DR strategy is the company using?**


1: Backup and restore


2: Pilot light


3: Warm standby


4: Multi-site


Answer: 2


**Explanation:**


In this DR approach, you simply replicate part of your IT structure for a limited set of core services so that the AWS

cloud environment seamlessly takes over in the event of a disaster.


A small part of your infrastructure is always running simultaneously syncing mutable data (as databases or documents),

while other parts of your infrastructure are switched off and used only during testing.


Unlike a backup and recovery approach, you must ensure that your most critical core elements are already configured and

running in AWS (the pilot light). When the time comes for recovery, you can rapidly provision a full-scale production

environment around the critical core.


- CORRECT "Pilot light" is the correct answer.


- INCORRECT "Backup and restore" is incorrect. This is the lowest cost DR approach that simply entails creating online

  backups of all data and applications.


- INCORRECT "Warm standby" is incorrect. The term warm standby is used to describe a DR scenario in which a scaled-down

  version of a fully functional environment is always running in the cloud.


- INCORRECT "Multi-site" is incorrect. A multi-site solution runs on AWS as well as on your existing on-site

  infrastructure in an active- active configuration.


**References:**


https://aws.amazon.com/blogs/publicsector/rapidly-recover-mission-critical-systems-in-a-disaster/

