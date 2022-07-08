---
date created: 2022-07-05 23:14
---

## Quiz 3: A company delivers content to subscribers distributed globally from an application running on AWS. The application uses a fleet of Amazon EC2 instance in a private subnet behind an Application Load Balancer

(ALB). Due to an update in copyright restrictions, it is necessary to block access for specific countries.**
**What is the EASIEST method to meet this requirement?**

- [ ] Modify the ALB security group to deny incoming traffic from blocked countries
- [ ] Modify the security group for EC2 instances to deny incoming traffic from blocked countries
- [ ] Use Amazon CloudFront to serve the application and deny access to blocked countries
- [ ] Use a network ACL to block the IP address ranges associated with the specific countries

---

Answer: 3
**Explanation:**
When a user requests your content, CloudFront typically serves the requested content regardless of where the user is located. If you need to prevent users in specific countries from accessing your content, you can use the CloudFront geo restriction feature to do one of the following:

- Allow your users to access your content only if they're in one of the countries on a whitelist of approved countries.

- Prevent your users from accessing your content if they're in one of the countries on a blacklist of banned countries. For example, if a request comes from a country where, for copyright reasons, you are not authorized to distribute your content, you can use CloudFront geo restriction to block the request. This is the easiest and most effective way to implement a geographic restriction for the delivery of content.

- ✅: "Use Amazon CloudFront to serve the application and deny access to blocked countries" is the correct answer.

- ❌: "Use a Network ACL to block the IP address ranges associated with the specific countries" is incorrect as this would be extremely difficult to manage.

- ❌: "Modify the ALB security group to deny incoming traffic from blocked countries" is incorrect as security groups cannot block traffic by country.

- ❌: "Modify the security group for EC2 instances to deny incoming traffic from blocked countries" is incorrect as security groups cannot block traffic by country.
  **References:**
  <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html>
  delivery/amazon-cloudfront/

---

#quiz

- ::relateTo:: [[Domain 3 Design Secure Applications and Architectures]]
