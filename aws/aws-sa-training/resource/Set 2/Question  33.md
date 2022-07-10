#### Question  33

```

Amazon CloudFront

```

```

Distribution

```

```

Distribution User

```

```

S 3 Bucket

```

```

EC 2 Instance

```

```

Application

Load Balancer

EC 2 Instance

```

```

S 3 Origin:

```

```

S 3 Static

Website

```

```

Custom Origin:

```

```

Custom Origin:

```

```

Web Distribution:

```

- Static and dynamic content

- HTTP/HTTPS

- Add/update/delete objects + webforms

- Real time live streaming RTMP Distribution:

- Uses Adobe Flash Media RTMP protocol

- Can play media file before downloaded

- Must use S 3 origin

**A client is in the design phase of developing an application that will process orders for their online ticketing

system. The application will use a number of front-end EC2 instances that pick-up orders and place them in a queue for

processing by another set of back-end EC2 instances. The client will have multiple options for customers to choose the

level of service they want to pay for.**

**The client has asked how he can design the application to process the orders in a prioritized way based on the level

of service the customer has chosen?**

- [ ] Create multiple SQS queues, configure exactly-once processing and set the maximum visibility timeout to 12 hours

- [x] Create multiple SQS queues, configure the front-end application to place orders onto a specific queue based on the

level of service requested and configure the back-end instances to sequentially poll the queues in order of priority

- [ ] Create a combination of FIFO queues and Standard queues and configure the applications to place messages into the

relevant queue based on priority

- [ ] Create a single SQS queue, configure the front-end application to place orders on the queue in order of priority and

configure the back-end instances to poll the queue and pick up messages in the order they are presented

- hasExplain:: [[explanation_Question  33.md]]

# amazon_cloudfront #web_distribution #end_ec2_instances #ec #adobe_flash_media_rtmp_protocol
