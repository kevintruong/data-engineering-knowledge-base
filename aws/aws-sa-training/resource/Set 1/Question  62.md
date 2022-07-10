#### Question  62


**The company you work for is currently transitioning their infrastructure and applications into the AWS cloud. You are

planning to deploy an Elastic Load Balancer (ELB) that distributes traffic for a web application running on EC2

instances. You still have some application servers running on-premise and you would like to distribute application

traffic across both your AWS and on-premises resources.**


**How can this be achieved?**


- [x] Provision a Direct Connect connection between your on-premises location and AWS and create a target group on an ALB

to use IP based targets for both your EC2 instances and on-premises servers


- [x] Provision a Direct Connect connection between your on-premises location and AWS and create a target group on an ALB

to use Instance ID based targets for both your EC2 instances and on-premises servers


- [ ] Provision an IPSec VPN connection between your on-premises location and AWS and create a CLB that uses cross-zone

load balancing to distributed traffic across EC2 instances and on-premises servers


```

Region

```


```

Amazon CloudFront

```


```

S 3 Bucket configured

as static website

```


```

Custom Origin

```


```

Users

Bucket Policy

```


```

Origin Access Identity (OAI)

```


- [ ] This cannot be done, ELBs are an AWS service and can only distribute traffic within the AWS cloud



- hasExplain:: [[explanation_Question  62.md]]

#aws_service #aws_cloud #elastic_load_balancer #ec2_instances #aws 