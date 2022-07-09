#### Question  21


**A Solutions Architect regularly launches EC2 instances manually from the console and wants to streamline the process

to reduce administrative overhead. Which feature of EC2 enables storing of settings such as AMI ID, instance type, key

pairs and Security Groups?**


1: Placement Groups


2: Launch Templates


3: Run Command


4: Launch Configurations


**Answer: 2**


**Explanation:**


Launch templates enable you to store launch parameters so that you do not have to specify them every time you launch an

instance. When you launch an instance using the Amazon EC2 console, an AWS SDK, or a command line tool, you can specify

the launch template to use.


- CORRECT "Launch Templates" is the correct answer.


- INCORRECT "Placement Groups" is incorrect. You can launch or start instances in a _placement group_ , which determines

  how instances are placed on underlying hardware.


- INCORRECT "Run Command" is incorrect. Run Command automates common administrative tasks, and lets you perform ad hoc

  configuration changes at scale.


```

Region

```


```

Availability

Zone

```


```

Availability

Zone

```


```

Availability

Zone

```


```

Writes Writes

```


```

Region

```


```

Availability

Zone

```


```

Availability

Zone

```


```

Availability

Zone

```


```

Asynchronous Reads Reads

replication

```


```

Primary Region Secondary^ Region

```


```

Aurora Global Database:

```


- Uses physical replication

- One secondary AWS region

- Uses dedicated infrastructure

- No impact on DB performance

- Good for disaster recovery


- INCORRECT "Launch Configurations" is incorrect. Launch Configurations are used with Auto Scaling Groups.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html


**Save time with our exam-specific cheat sheets:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html

