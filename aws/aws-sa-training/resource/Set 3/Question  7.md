#### Question  7


**An application is deployed on multiple AWS regions and accessed from around the world. The application exposes static

public IP addresses. Some users are experiencing poor performance when accessing the application over the Internet.**


**What should a solutions architect recommend to reduce internet latency?**


1: Set up AWS Global Accelerator and add endpoints


2: Set up AWS Direct Connect locations in multiple Regions


3: Set up an Amazon CloudFront distribution to access an application


4: Set up an Amazon Route 53 geoproximity routing policy to route traffic


Answer: 1


**Explanation:**


AWS Global Accelerator is a service in which you create _accelerators_ to improve availability and performance of your

applications for local and global users. Global Accelerator directs traffic to optimal endpoints over the AWS global

network. This improves the availability and performance of your internet applications that are used by a global

audience. Global Accelerator is a global service that supports endpoints in multiple AWS Regions, which are listed in

the AWS Region Table.


```

Availability Zone Availability Zone Availability Zone

```


```

Primary

```


```

Data Copies Data Copies Data Copies

```


```

Replica Replica Replica

```


```

Reads Writes Writes Writes

```


```

Reads Reads Reads

```


```

Region

```


```

Single Logical Volume

```


```

Aurora Fault Tolerance

```


- Fault tolerance across 3 AZs

- Single logical volume

- Aurora Replicas scale-out read requests

- Up to 15 Aurora Replicas with sub- 10 ms replica lag

- Aurora Replicas are independent endpoints

- Can promote Aurora Replica to be a new primary or create new primary

- Set priority (tiers) on Aurora Replicas to control order of promotion

- Can use Auto Scaling to add replicas


By default, Global Accelerator provides you with two static IP addresses that you associate with your accelerator. (Or,

instead of using the IP addresses that Global Accelerator provides, you can configure these entry points to be IPv4

addresses from your own IP address ranges that you bring to Global Accelerator.)


The static IP addresses are anycast from the AWS edge network and distribute incoming application traffic across

multiple endpoint resources in multiple AWS Regions, which increases the availability of your applications. Endpoints

can be Network Load Balancers, Application Load Balancers, EC2 instances, or Elastic IP addresses that are located in

one AWS Region or multiple Regions.


- CORRECT "Set up AWS Global Accelerator and add endpoints" is the correct answer.


- INCORRECT "Set up AWS Direct Connect locations in multiple Regions" is incorrect as this is used to connect from an

  on-premises data center to AWS. It does not improve performance for users who are not connected to the on-premises

  data center.


- INCORRECT "Set up an Amazon CloudFront distribution to access an application" is incorrect as CloudFront cannot expose

  static public IP addresses.


- INCORRECT "Set up an Amazon Route 53 geoproximity routing policy to route traffic" is incorrect as this does not

  reduce internet latency as well as using Global Accelerator. GA will direct users to the closest edge location and

  then use the AWS global network.


**References:**


https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/aws-global-accelerator/

