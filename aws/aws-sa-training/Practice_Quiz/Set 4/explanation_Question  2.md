**Explanation:**

AWS Global Accelerator uses static IP addresses as fixed entry points for your application. You can migrate up to two

/24 IPv4 address ranges and choose which /32 IP addresses to use when you create your accelerator.

This solution ensures the company can continue using the same IP addresses and they are able to direct traffic to the

application endpoint in the AWS Region closest to the end user. Traffic is sent over the AWS global network for

consistent performance.

- ✅ :  "Create an AWS Global Accelerator and attach endpoints in each AWS Region" is a correct answer.

- ✅ :  "Migrate both public IP addresses to the AWS Global Accelerator" is also a correct answer.

- ❌ :  "Create an Amazon Route 53 geolocation based routing policy" is incorrect. With this solution new IP

  addresses will be required as there will be application endpoints in different regions.

- ❌ :  "Assign new static anycast IP addresses and modify any existing pointers" is incorrect. This is unnecessary

  as you can bring your own IP addresses to AWS Global Accelerator and this is preferred in this scenario.

- ❌ :  "Create PTR records to map existing public IP addresses to an Alias" is incorrect. This is not a workable

  solution for mapping existing IP addresses to an Amazon Route 53 Alias.

**References:**

<https://aws.amazon.com/global-accelerator/features/>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/aws-global-accelerator/

----

- #aws_global_accelerator #aws_region #aws #amazon_route #new_static_anycast_ip_addresses
