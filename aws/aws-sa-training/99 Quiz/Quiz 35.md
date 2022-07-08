## Quiz 35: A new application is to be published in multiple regions around the world. The Architect needs to ensure only 2 IP addresses need to be whitelisted. The solution should intelligently route traffic for lowest latency and provide fast regional failover.**

**How can this be achieved?**

- [ ] Launch EC2 instances into multiple regions behind an NLB with a static IP address
- [ ] Launch EC2 instances into multiple regions behind an ALB and use a Route 53 failover routing policy
- [x] Launch EC2 instances into multiple regions behind an NLB and use AWS Global Accelerator
- [ ] Launch EC2 instances into multiple regions behind an ALB and use Amazon CloudFront with a pair of static IP addresses

----
Answer:

- [x] Launch EC2 instances into multiple regions behind an NLB and use AWS Global Accelerator
  **Explanation:**
  AWS Global Accelerator uses the vast, congestion-free AWS global network to route TCP and UDP traffic to a healthy application endpoint in the closest AWS Region to the user. This means it will intelligently route traffic to the closest point of presence (reducing latency). Seamless failover is ensured as AWS Global Accelerator uses anycast IP address which means the IP does not change when failing over between regions so there are no issues with client caches having incorrect entries that need to expire.
  ![](aws-solution-architecture-practice-quiz-1641093155564.png)
  This is the only solution that provides deterministic failover.
- ✅: "Launch EC2 instances into multiple regions behind an NLB and use AWS Global Accelerator" is the correct answer.

- ❌: "Launch EC2 instances into multiple regions behind an NLB with a static IP address" is incorrect. An NLB with a static IP is a workable solution as you could configure a primary and secondary address in applications. However, this solution does not intelligently route traffic for lowest latency.

- ❌: "Launch EC2 instances into multiple regions behind an ALB and use a Route 53 failover routing policy" is incorrect. A Route 53 failover routing policy uses a primary and standby configuration. Therefore, it sends all traffic to the primary until it fails a health check at which time it sends traffic to the secondary. This solution does not intelligently route traffic for lowest latency.

- ❌: "Launch EC2 instances into multiple regions behind an ALB and use Amazon CloudFront with a pair of static IP addresses" is incorrect. Amazon CloudFront cannot be configured with “a pair of static IP addresses”.
  **References:**
  https://aws.amazon.com/global-accelerator/
  https://aws.amazon.com/global-accelerator/faqs/
  https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html
