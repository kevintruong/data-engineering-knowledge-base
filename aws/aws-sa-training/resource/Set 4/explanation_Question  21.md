*

**Explanation:**

Launch templates enable you to store launch parameters so that you do not have to specify them every time you launch an

instance. When you launch an instance using the Amazon EC2 console, an AWS SDK, or a command line tool, you can specify

the launch template to use.

* ✅ :  "Launch Templates" is the correct answer.

* ❌ :  "Placement Groups" is incorrect. You can launch or start instances in a _placement group_ , which determines

  how instances are placed on underlying hardware.

* ❌ :  "Run Command" is incorrect. Run Command automates common administrative tasks, and lets you perform ad hoc

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

* Uses physical replication

* One secondary AWS region

* Uses dedicated infrastructure

* No impact on DB performance

* Good for disaster recovery

* ❌ :  "Launch Configurations" is incorrect. Launch Configurations are used with Auto Scaling Groups.

**References:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>

**Save time with our exam-specific cheat sheets:**

<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>

----
* #aws_sdk #secondary_aws_region #launch_configurations #aurora_global_database #amazon_ec2_console
