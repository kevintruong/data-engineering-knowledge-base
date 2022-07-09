#### Question  58


**An organization in the health industry needs to create an application that will transmit protected health data to

thousands of service consumers in different AWS accounts. The application servers run on EC2 instances in private VPC

subnets. The routing for the application must be fault tolerant.**


**What should be done to meet these requirements?**


- [ ] Create a virtual private gateway connection between each pair of service provider VPCs and service consumer VPCs


- [ ] Create a proxy server in the service provider VPC to route requests from service consumers to the application servers


```

Amazon Simple Queue

Service

```


```

Queue

```


```

EC 2 instance

polls SQS

```


```

Web Tier

```


```

Auto Scaling Group

```


```

App Tier

```


```

Auto Scaling Group

Decoupled integration

```


- [x] Create a VPC endpoint service and grant permissions to specific service consumers to create a connection


- [ ] Create an internal Application Load Balancer in the service provider VPC and put application servers behind it

