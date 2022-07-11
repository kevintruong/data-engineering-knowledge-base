### Networking & Content Delivery Quiz Questions


Answers and explanations are provided below after the last question in this section.


**Question 1: At which level do you attach an Internet gateway**


1. Public Subnet

2. Private Subnet

3. Availability Zone

4. VPC


**Question 2: What is the scope of a Virtual Private Cloud (VPC)?**


1. Global

2. Regional

3. Availability Zone


**Question 3: How should subnets be used for fault tolerance?**


1. Create subnets that span multiple availability zones

2. Create subnets that have multiple Internet Gateways

3. Launch EC2 instances into subnets attached to a region

4. Launch EC2 instances into subnets created in different availability zones


**Question 4: Your organization has a pre-production VPC and production VPC. You need to be able to setup routing

between these VPCs using private IP addresses. How can this be done?**


1. Configure a VPC endpoint

2. Add a route table entry for the opposite VPCs Internet gateway

3. Configure a peering connection

4. Use an Egress-only Internet gateway


**Question 5: You created a new private subnet and created a route table with a path to a NAT gateway. However, EC2

instances launched into this subnet are not able to reach the Internet. Security Groups for the EC2 instances are setup

correctly. What is the most likely explanation?**


1. The security group for the NAT gateway is setup incorrectly.

2. You need to associate the new subnet with the new route table.

3. You need to add an entry for an Internet gateway.


**Question 6: You need to apply a firewall to a group of EC2 instances launched in multiple subnets. Which option should

be used?**


1. Network Access Control List (ACL)

2. Operating system firewall

3. Security Group

4. IAM Policy


**Question 7: An attack has been identified from a group of IP addresses. What’s the quickest way to block these

specific IP addresses from reaching the instances in your subnets?**


1. Apply a Security Group to the instances in the subnets with a deny rule

2. Change the IP addresses used by the instances


3. Detach the Internet Gateway

4. Apply a Network ACL to the subnets involved with a deny rule


**Question 8: An organization needs a private, high-bandwidth, low-latency connection to the AWS Cloud in order to

establish hybrid cloud configuration with their on-premises cloud. What type of connection should they use?**


1. AWS Managed VPN

2. AWS VPN CloudHub

3. AWS Direct Connect

4. Transit VPC


**Question 9: An Architect needs to point the domain name dctlabs.com to the DNS name of an Elastic Load Balancer. Which

type of record should be used?**


1. MX record

2. A record

3. CNAME record

4. Alias record


**Question 10: A company hosts copies of the same data in Amazon S3 buckets around the world and needs to ensure that

customers connect to the nearest S3 bucket. Which Route 53 routing policy should be used?**


1. Simple

2. Failover

3. Latency

4. Weighted


**Question 11: A media organization offers news in local languages around the world. Which Route 53 routing policy

should be used to direct readers to the website with the correct language?**


1. Latency

2. Geolocation

3. Multivalue answer

4. Weighted


**Question 12: An Architect is designing a web application that has points of presence in several regions around the

world. The Architect would like to provide automatic routing to the nearest region, with failover possible to other

regions. Customers should receive 2 IP addresses for whitelisting. How can this be achieved?**


1. Use Route 53 latency-based routing

2. Use Amazon CloudFront

3. Use AWS Global Accelerator

4. Use Route 53 geolocation routing


**Question 13: Which services does Amazon API Gateway use for its public endpoint?**


1. AWS Lambda

2. Amazon CloudFront

3. Amazon S3

4. Amazon ECS


**Question 14: A company provides videos for new employees around the world. They need to store the videos in one

location and then provide low-latency access for the employees around the world. Which service would be best suited to

providing fast access to the content?**


1. Amazon S3

2. AWS Global Accelerator

3. Amazon CloudFront

4. AWS Lambda


**Question 15: Which of the following are NOT valid origins for Amazon CloudFront?**


1. Amazon S3 buckets

2. EC2 instance

3. AWS Lambda function

4. Elastic Load Balancer (ELB)


**NETWORKING & CONTENT DELIVERY - ANSWERS**


**Question 1, Answer: 4**


**Explanation:**


```

1 is incorrect. You do not attach Internet gateways to subnets.

2 is incorrect. You do not attach Internet gateways to subnets.

3 is incorrect. You do not attach Internet gateways to AZs.

4 is correct. Internet Gateways are attached to the VPC. You then need to add entries to the

route tables for your public subnets to point to the IGW.

```


**Question 2, Answer: 2**


**Explanation:**


```

1 is incorrect. VPCs are not global.

2 is correct. VPCs are regional. You create VPCs in each region separately.

3 is incorrect. An availability zone exists within a region and a VPC can span subnets attached to

all AZs in the region.

```


**Question 3, Answer: 4**


**Explanation:**


```

1 is incorrect. Subnets cannot span multiple AZs.

2 is incorrect. You cannot have multiple IGWs attached to a VPC.

3 is incorrect. You cannot attach a subnet to a region.

4 is correct. You should create multiple subnets each within a different AZ and launch EC2

instances running your application across these subnets.

```


**Question 4, Answer: 3**


**Explanation:**


```

1 is incorrect. A VPC endpoint can be used for sharing resources between VPCs but it is not used

for direct routing between private IP addresses.

2 is incorrect. You cannot route between VPCs by using Internet gateways.

3 is correct. A peering connection enables you to route traffic via private IP addresses between

two peered VPCs.

4 is incorrect. An egress-only Internet gateway is used for IPv6 traffic.

```


**Question 5, Answer: 2**


**Explanation:**


```

1 is incorrect. NAT gateways do not have security groups.

2 is correct. By default, new subnets are associated with the default route table. You need to

assign the new route table in order for the instances to see the route to the NAT gateway.

3 is incorrect. You cannot use an Internet Gateway with a private subnet as the instances will not

have public IP addresses.

```


**Question 6, Answer: 3**


**Explanation:**


```

1 is incorrect. Network ACLs are applied at the subnet level and will apply to all instances in the

subnet, not just the group of EC2 instances.

2 is incorrect. Operating system-level firewalls require more administrative effort to maintain

and are not the best option on AWS.

3 is correct. A Security Group can be applied to the group of EC2 instances. You can specify what

ports and protocols are allowed to reach the instances and from what sources.

4 is incorrect. An IAM Policy is not a firewall.

```


**Question 7, Answer: 4**


**Explanation:**


```

1 is incorrect. You cannot apply deny rules with security groups.

2 is incorrect. This is not a good solution as it may break applications.

3 is incorrect. This would not block the specific IP addresses; it would stop all Internet

connectivity.

4 is correct. You can apply deny rules with Network ACLs to block the specific IP addresses only.

```


**Question 8, Answer: 3**


**Explanation:**


```

1 is incorrect. AWS Managed VPN uses the public Internet, so it’s not considered a private

connection or low-latency.

2 is incorrect. AWS VPN CloudHub is used for creating a hub and spoke topology of VPN

connections. Uses the public Internet not a private connection.

3 is correct. AWS Direct Connect uses private network connections into the AWS Cloud and is

high-bandwidth and low-latency. This is good for establishing hybrid cloud configurations.

4 is incorrect. A Transit VPC is used for connecting VPCs across regions.

```


**Question 9, Answer: 4**


**Explanation:**


```

1 is incorrect. An MX record is a mail exchange record for email servers.

2 is incorrect. An A record simply points a name to an IP address.

3 is incorrect. A CNAME record cannot be pointed at a domain apex record like dctlabs.com.

4 is correct. An Alias record can be used with domain apex records and can point to an ELB.

```


**Question 10, Answer: 3**


**Explanation:**


```

1 is incorrect. The simple routing policy does not perform any routing based on location or

latency.

2 is incorrect. The failover routing policy uses primary and secondary records for high availability.

3 is correct. The latency routing policy directs based on the lowest latency to the AWS resource.

Latency increases over distance so this should ensure customers connect to the closest S3

bucket.

4 is incorrect. The weighted policy uses relative weights not location or latency.

```


**Question 11, Answer: 2**


**Explanation:**


```

1 is incorrect. The latency routing policy directs based on latency (distance) but does not allow

you to specify geographic locations.

2 is correct. In this case you need to identify specific geographic locations and associate them

with the correct language version.

3 is incorrect. This routing policy returns multiple answers for load balancing.

4 is incorrect. The weighted policy uses relative weights not geographic information.

```


**Question 12, Answer: 3**


**Explanation:**


```

1 is incorrect. Route 53 latency based routing does not provide automatic failover or 2 IP

addresses.

2 is incorrect. Amazon CloudFront is a content delivery network. It does not perform automatic

routing across regions and doesn’t provide 2 IP addresses for whitelisting.

3 is correct. AWS Global Accelerator provides static IP addresses that act as a fixed entry point to

application endpoints in a single or multiple AWS Regions. It uses 2 static anycast IP addresses.

4 is incorrect. Route 53 geolocation based routing does not provide automatic failover or 2 IP

addresses.

```


**Question 13, Answer: 2**


**Explanation:**


```

1 is incorrect. AWS Lambda is not used as the public endpoint for API Gateway.

2 is correct. Amazon CloudFront is used as the public endpoint for API Gateway.

3 is incorrect. Amazon S3 is not used as the public endpoint for API Gateway.

4 is incorrect. Amazon ECS is not used as the public endpoint for API Gateway.

```


**Question 14, Answer: 3**


**Explanation:**


```

1 is incorrect. To provide low-latency access with Amazon S3 you would need to copy the videos

to buckets in different regions around the world and then create a mechanism for directing

employees to the local copy.

2 is incorrect. AWS Global Accelerator is used for directing users of applications to local points of

presence around the world. It is not used for accessing content in S3, it’s used with ELB and

EC2.

3 is correct. CloudFront is a content delivery network and is ideal for this use case as it caches

the content around the world, provides a single endpoint address, and uses a single source for

the videos.

4 is incorrect. AWS Lambda is a compute service and not suited to this use case.

```


**Question 15, Answer: 3**


**Explanation:**


```

1 is incorrect. Amazon S3 buckets are a valid origin for CloudFront.

2 is incorrect. EC2 instances are a valid origin for CloudFront.

3 is correct. AWS Lambda is not a valid origin for Amazon CloudFront.

4 is incorrect. ELBs are a valid origin for CloudFront.

```

