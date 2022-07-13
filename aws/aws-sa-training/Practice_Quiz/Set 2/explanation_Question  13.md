**Explanation:**

The problem that is being described is that the users are uploading the documents to an individual EC2 instance with a

local EBS volume. Therefore, as EBS volumes cannot be shared across AZs, the data is stored separately and the ALB will

be distributing incoming connections to different instances / data sets.

The simple resolution is to implement a shared storage layer for the documents so that they can be stored in one place

and seen by any user who connects no matter which instance they connect to.

- ✅ :  "Copy the data from all EBS volumes to Amazon EFS. Modify the application to save new documents to Amazon EFS"

  is the correct answer.

- ❌ :  "Run a script to synchronize the data between Amazon EBS volumes" is incorrect. This is a complex and messy

  approach. A better solution is to use a shared storage layer.

- ❌ :  "Use Sticky Sessions with the ALB to ensure users are directed to the same EC2 instance in a session" is

  incorrect as this will just “stick” a user to the same instance. They won’t see documents uploaded to other instances

  / EBS volumes.

```

EC 2 Instance

```

```

Amazon Elastic File

System

```

```

File system

```

```

/efs-mnt

```

```

EC 2 Instance

```

```

/efs-mnt

```

```

Availability Zone Availability Zone

```

- ❌ :  "Configure the Application Load Balancer to send the request to all servers. Return each document from the

  correct server" is incorrect as there is no mechanism here for selecting a specific document. The requirement also

  requests that all documents are visible.

**References:**

<https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/>

----

- #amazon_ebs_volumes #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/> #amazon_efs #ebs_volumes #individual_ec2_instance
