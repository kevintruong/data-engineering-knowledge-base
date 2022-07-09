#### Question  12


**A company needs to ensure that they can failover between AWS Regions in the event of a disaster seamlessly with

minimal downtime and data loss. The applications will run in an active-active configuration.**


**Which DR strategy should a Solutions Architect recommend?**


1: Backup and restore


2: Pilot light


3: Warm standby


4: Multi-site


Answer: 4


**Explanation:**


A multi-site solution runs on AWS as well as on your existing on-site infrastructure in an active- active configuration.

The data replication method that you employ will be determined by the recovery point that you choose. This is either

Recovery Time Objective (the maximum allowable downtime before degraded operations are restored) or Recovery Point

Objective (the maximum allowable time window whereby you will accept the loss of transactions during the DR process).


- CORRECT "Multi-site" is the correct answer.


- INCORRECT "Backup and restore" is incorrect. This is the lowest cost DR approach that simply entails creating online

  backups of all data and applications.


- INCORRECT "Pilot light" is incorrect. With a pilot light strategy a core minimum of services are running and the

  remainder are only brought online during a disaster recovery situation.


- INCORRECT "Warm standby" is incorrect. The term warm standby is used to describe a DR scenario in which a scaled-down

  version of a fully functional environment is always running in the cloud.


**References:**


https://aws.amazon.com/blogs/publicsector/rapidly-recover-mission-critical-systems-in-a-disaster/

