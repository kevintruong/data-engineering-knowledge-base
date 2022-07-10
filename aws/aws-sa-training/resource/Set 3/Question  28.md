#### Question  28

**A web app allows users to upload images for viewing online. The compute layer that processes the images is behind an

Auto Scaling group. The processing layer should be decoupled from the front end and the ASG needs to dynamically adjust

based on the number of images being uploaded.**

**How can this be achieved?**

- [ ] :  Create an Amazon SNS Topic to generate a notification each time a message is uploaded. Have the ASG scale based on

the number of SNS messages

- [ ] :  Create a target tracking policy that keeps the ASG at 70% CPU utilization

- [x] :  Create an Amazon SQS queue and custom CloudWatch metric to measure the number of messages in the queue. Configure the

ASG to scale based on the number of messages in the queue

- [ ] :  Create a scheduled policy that scales the ASG at times of expected peak load

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

----

- #custom_cloudwatch #amazon_sqs_queue #amazon_sns_topic #queue #asg_scale
- hasExplain:: [[explanation_Question  28.md]]
