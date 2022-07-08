## Quiz 51: An application tier of a multi-tier web application currently hosts two web services on the same set of instances. The web services each listen for traffic on different ports. Which AWS service should a Solutions Architect use to route traffic to the service based on the incoming request path?**

- [ ] Amazon Route 53

- [ ] Amazon CloudFront

- [x] Application Load Balancer (ALB)

- [ ] Classic Load Balancer (CLB)

----
Answer: 3
**Explanation:**
An Application Load Balancer is a type of Elastic Load Balancer that can use layer 7 (HTTP/HTTPS) protocol data to make forwarding decisions. An ALB supports both path-based (e.g. /images or /orders) and host-based routing (e.g. example.com). In this scenario a single EC2 instance is listening for traffic for each application on a different port. You can use a target group that listens on a single port (HTTP or HTTPS) and then uses listener rules to selectively route to a different port on the EC2 instance based on the information in the URL path. So you might have example.com/images going to one backend port and example.com/orders going to a different backend port.

- ✅: "Application Load Balancer (ALB)" is the correct answer.
- ❌: "Amazon Route 53" is incorrect. Amazon Route 53 is a DNS service. It can be used to load balance however it does not have the ability to route based on information in the incoming request path.
- ❌: "Amazon CloudFront" is incorrect. Amazon CloudFront is used for caching content. It can route based on request path to custom origins however the question is not requesting a content caching service so it’s not the best fit for this use case.
- ❌: "Classic Load Balancer (CLB)" is incorrect. You cannot use host-based or path-based routing with a CLB.
  **References:**
  https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html
  balancing/
