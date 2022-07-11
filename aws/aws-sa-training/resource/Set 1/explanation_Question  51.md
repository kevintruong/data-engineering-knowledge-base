**Explanation:**

An Application Load Balancer is a type of Elastic Load Balancer that can use layer 7 (HTTP/HTTPS) protocol data to make

forwarding decisions. An ALB supports both path-based (e.g. /images or /orders) and host-based routing (e.g.

example.com).

In this scenario a single EC2 instance is listening for traffic for each application on a different port. You can use a

target group that listens on a single port (HTTP or HTTPS) and then uses listener rules to selectively route to a

different port on the EC2 instance based on the information in the URL path. So you might have example.com/images going

to one backend port and example.com/orders going to a different backend port.

- ✅ :  "Application Load Balancer (ALB)" is the correct answer.

- ❌ :  "Amazon Route 53" is incorrect. Amazon Route 53 is a DNS service. It can be used to load balance however it

  does not have the ability to route based on information in the incoming request path.

- ❌ :  "Amazon CloudFront" is incorrect. Amazon CloudFront is used for caching content. It can route based on

  request path to custom origins however the question is not requesting a content caching service so it’s not the best

  fit for this use case.

- ❌ :  "Classic Load Balancer (CLB)" is incorrect. You cannot use host-based or path-based routing with a CLB.

**References:**

<https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----

- #elastic_load_balancer #amazon_cloudfront #amazon_route #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>>- #application_load_balancer
