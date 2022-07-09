#### Question  18


**A Solutions Architect needs to select a low-cost, short-term option for adding resilience to an AWS Direct Connect

connection. What is the MOST cost-effective solution to provide a backup for the Direct Connect connection?**


1: Implement a second AWS Direct Connection


2: Implement an IPSec VPN connection and use the same BGP prefix


3: Configure AWS Transit Gateway with an IPSec VPN backup


4: Configure an IPSec VPN connection over the Direct Connect link


Answer: 2


**Explanation:**


This is the most cost-effective solution. With this option both the Direct Connect connection and IPSec VPN are active

and being advertised using the Border Gateway Protocol (BGP). The Direct Connect link will always be preferred unless it

is unavailable.


- CORRECT "Implement an IPSec VPN connection and use the same BGP prefix" is the correct answer.


- INCORRECT "Implement a second AWS Direct Connection" is incorrect. This is not a short-term or low-cost option as it

  takes time to implement and is costly.


- INCORRECT "Configure AWS Transit Gateway with an IPSec VPN backup" is incorrect. This is a workable solution and

  provides some advantages. However, you do need to pay for the Transit Gateway so it is not the most cost-effective

  option and probably not suitable for a short-term need.


- INCORRECT "Configure an IPSec VPN connection over the Direct Connect link" is incorrect. This is not a solution to the

  problem as the VPN connection is going over the Direct Connect link. This is something you might do to add encryption

  to Direct Connect but it doesn’t make it more resilient.


**References:**


https://aws.amazon.com/premiumsupport/knowledge-center/configure-vpn-backup-dx/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/aws-direct-connect/

