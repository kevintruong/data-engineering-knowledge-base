#### Question  13


```

EC 2 Instance

```


```

EC 2 Instance

```


```

Region

```


```

VPC

```


```

Corporate data center

```


```

On-premises

client

```


```

VPN or Direct

Connect connection

```


```

Availability Zone

```


```

Availability Zone

Public subnet

```


```

Public subnet

```


```

S 3 objects can be

viewed as files in FSx;

result data can be

S 3 Bucket written back to S 3

```


```

Amazon FSxfor Lustre

```


```

Use for cloud

bursting and data

migration

```


**A web application that allows users to upload and share documents is running on a single Amazon EC2 instance with an

Amazon EBS volume. To increase availability the architecture has been updated to use an Auto Scaling group of several

instances across Availability Zones behind an Application Load Balancer. After the change users can only see a subset of

the documents.**


**What is the BEST method for a solutions architect to modify the solution so users can see all documents?**


- [ ] Run a script to synchronize the data between Amazon EBS volumes


- [ ] Use Sticky Sessions with the ALB to ensure users are directed to the same EC2 instance in a session


- [x] Copy the data from all EBS volumes to Amazon EFS. Modify the application to save new documents to Amazon EFS


- [ ] Configure the Application Load Balancer to send the request to all servers. Return each document from the correct

server



- hasExplain:: [[explanation_Question  13.md]]

#amazon_ebs_volumes #single_amazon_ec2_instance #amazon_efs #ebs_volumes #amazon_ebs_volume 