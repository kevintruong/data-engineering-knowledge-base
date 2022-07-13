**Explanation:**

The ELB Application Load Balancer can route traffic based on data included in the request including the host name

portion of the URL as well as the path in the URL. Creating a rule to route traffic based on information in the path

will work for this solution and ALB works well with Amazon ECS.

The diagram below depicts a configuration where a listener directs traffic that comes in with /orders in the URL to the

second target group and all other traffic to the first target group:

- ✅ :  "Use an AWS Application Load Balancer with a path-based routing rule to route traffic to the correct service"

  is the correct answer.

- ❌ :  "Use an AWS Classic Load Balancer with a host-based routing rule to route traffic to the correct service"

  is incorrect. The ELB Classic Load Balancer does not support any content-based routing including host or path-based.

- ❌ :  "Use the AWS CLI to update an Amazon Route 53 hosted zone to route traffic as services get updated" is

  incorrect. Using the AWS CLI to update Route 53 as to how to route traffic may work, but it is definitely not the most

  efficient way to solve this challenge.

- ❌ :  "Use Amazon CloudFront to manage and route traffic to the correct service" is incorrect. Amazon CloudFront

  does not have the capability to route traffic to different Amazon ECS services based on content metadata.

**References:**

<https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-load-balancer-routing.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load>-

balancing/

----

- #elb_application_load_balancer #<https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-load-balancer-routing.html> #aws_application_load_balancer #aws_classic_load_balancer #elb_classic_load_balancer
