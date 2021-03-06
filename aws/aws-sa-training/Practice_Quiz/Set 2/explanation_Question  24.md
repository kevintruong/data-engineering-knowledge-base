**Explanation:**

AWS Direct Connect provides a secure, reliable and private connection. However, lead times are often longer than 1 month

so it cannot be used to migrate data within the timeframes. Therefore, it is better to use AWS Snowball to move the data

and order a Direct Connect connection to satisfy the other requirement later on. In the meantime the organization can

use an AWS VPN for secure, private access to their VPC.

- ✅ :  "Migrate data using AWS Snowball. Provision an AWS VPN initially and order a Direct Connect link"

  is the correct answer.

- ❌ :  "Provision an AWS Direct Connect connection and migrate the data over the link" is incorrect due to the lead

  time for installation.

- ❌ :  "Launch a Virtual Private Gateway (VPG) and migrate the data over the AWS VPN" is incorrect. A VPG is the

  AWS-side of an AWS VPN. A VPN does not provide a private connection and is not reliable as you can never guarantee the

  latency over the Internet

- ❌ :  "Provision an AWS VPN CloudHub connection and migrate the data over redundant links" is incorrect. AWS VPN

  CloudHub is a service for connecting multiple sites into your VPC over VPN connections. It is not used for aggregating

  links and the limitations of Internet bandwidth from the company where the data is stored will still be an issue. It

  also uses the public Internet so is not a private or reliable connection.

**References:**

<https://aws.amazon.com/snowball/>

<https://aws.amazon.com/directconnect/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/aws-direct-connect/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/migration/aws-snowball/>

----

- #aws_vpn_cloudhub_connection #aws_direct_connect #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/migration/aws-snowball/> #aws_vpn #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>-
