#### Question  28


**A web app allows users to upload images for viewing online. The compute layer that processes the images is behind an

Auto Scaling group. The processing layer should be decoupled from the front end and the ASG needs to dynamically adjust

based on the number of images being uploaded.**


**How can this be achieved?**


1: Create an Amazon SNS Topic to generate a notification each time a message is uploaded. Have the ASG scale based on

the number of SNS messages


2: Create a target tracking policy that keeps the ASG at 70% CPU utilization


3: Create an Amazon SQS queue and custom CloudWatch metric to measure the number of messages in the queue. Configure the

ASG to scale based on the number of messages in the queue


4: Create a scheduled policy that scales the ASG at times of expected peak load


```

VPC

```


```

Private subnet

```


```

Public subnet

```


```

Web Server

```


```

Default VPC

```


```

VPC

```


```

Private subnet

```


```

Public subnet

```


```

EC 2 Instance

```


```

Custom VPC – Provider

```


```

Endpoint

```


```

Network Load

Balancer

```


```

Endpoint Service

```


Answer: 3


**Explanation:**


The best solution is to use Amazon SQS to decouple the front end from the processing compute layer. To do this you can

create a custom CloudWatch metric that measures the number of messages in the queue and then configure the ASG to scale

using a target tracking policy that tracks a certain value.


- CORRECT "Create an Amazon SQS queue and custom CloudWatch metric to measure the number of messages in the queue.

  Configure the ASG to scale based on the number of messages in the queue" is the correct answer.


- INCORRECT "Create an Amazon SNS Topic to generate a notification each time a message is uploaded. Have the ASG scale

  based on the number of SNS messages" is incorrect. The Amazon Simple Notification Service

  (SNS) is used for sending notifications using topics. Amazon SQS is a better solution for this scenario as it provides

  a decoupling mechanism where the actual images can be stored for processing. SNS does not provide somewhere for the

  images to be stored.


- INCORRECT "Create a target tracking policy that keeps the ASG at 70% CPU utilization" is incorrect. Using a target

  tracking policy with the ASG that tracks CPU utilization does not allow scaling based on the number of images being

  uploaded.


- INCORRECT "Create a scheduled policy that scales the ASG at times of expected peak load" is incorrect. Using a

  scheduled policy is less dynamic as though you may be able to predict usage patterns, it would be better to adjust

  dynamically based on actual usage.


**References:**


https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-

scaling/

