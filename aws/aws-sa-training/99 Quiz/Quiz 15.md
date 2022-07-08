---
date created: 2022-07-06 00:02
---

## Quiz 15: A company runs a web application that serves weather updates. The application runs on a fleet of Amazon EC2 instances in a Multi-AZ Auto scaling group behind an Application Load Balancer (ALB). 

The instances  Store data in an Amazon Aurora database. 

A solutions architect needs to make the application more resilient to sporadic increases in request rates.

Which architecture should the solutions architect implement? (Select TWO)

- [ ] Add and AWS WAF in front of the ALB

- [x] Add Amazon Aurora Replicas

- [ ] Add an AWS Transit Gateway to the Availability Zones

- [ ] Add an AWS Global Accelerator endpoint

- [x] Add an Amazon CloudFront distribution in front of the ALB

---

Answer: 2, 5

- [x] Add Amazon Aurora Replicas

- [x] Add an Amazon CloudFront distribution in front of the ALB
  **Explanation:**
  The architecture is already highly resilient but may be subject to performance degradation if there are sudden increases in request rates. To resolve this situation Amazon Aurora Read Replicas can be used to serve read traffic which offloads requests from the main database. On the frontend an Amazon CloudFront distribution can be placed in front of the ALB and this will cache content for better performance and also offloads requests from the backend.

- ✅: "Add Amazon Aurora Replicas" is the correct answer.

- ✅: "Add an Amazon CloudFront distribution in front of the ALB" is the correct answer.

- ❌: "Add and AWS WAF in front of the ALB" is incorrect. A web application firewall protects applications from malicious attacks. It does not improve performance.

- ❌: "Add an AWS Transit Gateway to the Availability Zones" is incorrect as this is used to connect on- premises networks to VPCs.

- ❌: "Add an AWS Global Accelerator endpoint" is incorrect as this service is used for directing users to different instances of the application in different regions based on latency.
  **References:**
  <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html>
  <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html>



----
#quiz 
- relateTo:: [[Domain 1 Design Resilient Architectures]]