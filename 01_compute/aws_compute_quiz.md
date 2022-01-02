---
title: Quiz Elastic Compute Cloud EC2 hash_tag:

- ec2
- compute

---

# EC2 Compute Quiz Questions

## **Quiz: What do you need to securely connect using SSH to an EC2 instance launched from the Amazon Linux 2 AMI?**

<!-- #ec2_keypair -->

- [ ] A signed cookie
- [ ] An access key ID and secret access key
- [x] A key pair
- [ ] A password

----

**Question 1 Answer: a Key Pair **

**Explanation:**

```
- A signed cookie is incorrect. Signed cookies are not an authentication method for EC- [ ]
- An access key ID and secret access key is incorrect. An access key ID and secret access key are used for programmatic access to AWS services, not for securely connecting to Linux instances over SSH. Make sure you know the difference between these two concepts.
- A key pair is correct. Key pairs are used to securely connect to EC2 instances. A key pair consists of a public key that AWS stores, and a private key file that you store. For Linux AMIs, the private key file allows you to securely SSH (secure shell) into your instance.
- A password is incorrect. You do not need a password to connect to instances launched from the Amazon Linux 2 AMI.
```

## **Quiz: What can you use to run a script at startup on an Amazon EC2 Linux instance?**

<!-- #ec2_metadata #ec2_userdata -->

- [x] User data
- [ ] Metadata
- [ ] AWS Batch
- [ ] AWS Config

----

**Answer: 1**

**Explanation:**

```
1 is correct. User data is data that is supplied by the user at instance launch in the form of a script.
2 is incorrect. Instance metadata is data about your instance that you can use to configure or manage the running instance.
3 is incorrect. AWS Batch is used for running batch computing jobs across many instances.
4 is incorrect. AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources.
```

## **Quiz: Which EC2 pricing model would you use for a short-term requirement that needs to complete over a weekend?**

<!-- #ec2_instance_type #ec2_reserved #ec2_delicated_host -->

- [ ] Reserved Instance
- [ ] Spot Instance
- [ ] Dedicated Instance
- [x] On-Demand Instance

----

**Answer: 4**
On-Demand Instance
**Explanation:**

```
- Reserved Instance is incorrect. Reserved instances require a commitment over 1 or 3 years.
- Spot Instance is incorrect. Spot instances are good for cost-sensitive workloads that can afford to be interrupted. This workload must complete so Spot instances would not be ideal.
- Dedicated Instance is incorrect. Dedicated Instances are Amazon EC2 instances that run in a VPC on hardware that's dedicated to a single customer. This would be more expensive and there is no need for dedicated hardware in this case.
- On-Demand Instance is correct. On-demand instances are ideal for short-term or unpredictable workloads. You don’t get a discount, but you do have more flexibility with no commitments.
```

## **Quiz: An organization uses an application that uses per-socket licensing and they need full control over the placement of their EC2 instances on underlying hardware. What should they use?**

<!-- #ec2_delicated_host #ec2_reserved #ec2_instance_type -->

- [ ] Dedicated instances
- [x] Dedicated hosts
- [ ] Spot instances
- [ ] Reserved instances

----

**Answer: 2**

**Explanation:**

```
- Dedicated instances is incorrect. Dedicated instances provide dedicated hardware, but you don’t get visibility of sockets, cores, or targeted instance placement.
- Dedicated hosts is correct. Dedicated hosts provide dedicated hardware and they give you full visibility of sockets and cores and targeted instance placement.
- Spot instances is incorrect. With Spot instances you do not have control of instance placement on underlying hardware.
- Reserved instances is incorrect. With Reserved instances you do not have control of instance placement on underlying hardware.
```

## **Quiz: What type of storage is suitable for a use case that requires extremely high- performance local disks that do not need to be persistent?**

<!-- #ebs #snapshots #s3 #instance_store -->

- [ ] Elastic Block Store (EBS)
- [ ] Snapshots
- [x] Instance Store
- [ ] Amazon S3

----

**Answer:**

Instance Store

**Explanation:**

```
Elastic Block Store (EBS) is incorrect. EBS volumes are persistent. You can get high performance, but they are network attached disks, not local disks.
Snapshots is incorrect. Snapshots are used for taking a backup of EBS volumes.
Instance Store is correct. Instance store volumes are ephemeral (non-persistent) local disks that offer very high performance.
Amazon S3 is incorrect. Amazon S3 is an object storage system. It is not a local disk nor is it non-persistent.
```

## **Quiz: Which type of network adapter should be used for High Performance Computing (HPC) uses cases that include tightly coupled applications?**

<!-- #efa #eni #ena -->

- [x] Elastic Fabric Adapter (EFA)
- [ ] Elastic Network Interface (ENI)
- [ ] Elastic Network Adapter (ENA)

----

**Answer: 1**

**Explanation:**

```
1 is correct. EFA is good for High Performance Computing, MPI and ML use cases, tightly coupled applications and can be used with all instance types.
2 is incorrect. ENIs are the basic adapter type for when you don’t have any high-performance requirements.
3 is incorrect. ENAs are good for use cases that require higher bandwidth and lower inter- instance latency.
```

## **Quiz: An Architect would like to use an Elastic Load Balancer to forward traffic to different back-end applications for https://dctlabs.com/orders and https://dctlabs.com/account. Which type of ELB should be used?**

<!-- #alb #nlb #clb -->

- [x] Application Load Balancer with path-based routing
- [ ] Application Load Balancer with host-based routing
- [ ] Network Load Balancer with TCP port-based routing
- [ ] Classic Load Balancer with Layer 7 routing

----

**Answer: 1**
Application Load Balancer with path-based routing
**Explanation:**

```
Application Load Balancer with path-based routing is correct. To forward based on the path (e.g. /orders or /account) you can use the ALB with path-based routing.
Application Load Balancer with host-based routing is incorrect. Host-based routing uses the host name (e.g. dctlabs.com or amazon.com) rather than the path (e.g. /orders or /account).
Network Load Balancer with TCP port-based routing is incorrect. The NLB can forward based on different ports/listeners. However all of this traffic will be coming on the single port for HTTPS (443).
Classic Load Balancer with Layer 7 routing is incorrect. The CLB is a layer 7 router but there is not concepts of path-based routing. 
```

## **Quiz: How can a systems administrator copy an EBS volume from the us-west-1a availability zone to an instance in the us-west-1b availability zone?**

<!-- #ebs #snapshots  -->

- [x] Create a snapshot of the EBS volume in us-west-1a. Create a new volume in us-west-2b from the snapshot
- [ ] Create a new EBS volume attached to the instance in us-west-2b. Attach the EBS volume to the instance in us-west-1b and copy data between volumes

----

**Answer: 1**

**Explanation:**

```
1 is correct. This is the best method for copying an EBS volume between AZs. Remember, snapshots are stored on Amazon S3 which stores data within a region, not an AZ.
2 is incorrect. You cannot attach an EBS volume to an instance in a different AZ. 
```

## **Quiz: Which type of data volume provides very high performance and is ideal for storing data which is either replicated between EC2 instances or is only temporary and can be lost?**

<!-- #ebs #instance_store -->

- [ ] Elastic Block Store (EBS)
- [x] Instance Store

----

**Answer: **

Elastic Block Store (EBS)

**Explanation:**

```
- Elastic Block Storage (EBS) incorrect. EBS is persistent storage and though it provides high performance it may not be the best solution for data that is replicated or can be lost.
- Instance Storeis correct. This is a good use case for Instance Store storage. It can also be cost-effective as it comes with the price of the EC2 instance.
```

## **Quiz: The development department in your organization need to quickly access a platform for running Docker containers. The platform service should be fully managed. Which AWS service should you provision for them?**

<!-- #ecr #eks #ecs #fargate -->

- [ ] Amazon Elastic Container Service (ECS) with the EC2 launch type
- [x] Amazon Elastic Container Service (ECS) with the Fargate launch type
- [ ] Amazon Elastic Kubernetes Service (EKS)
- [ ] Amazon Elastic Container Registry (ECR)

----

**Answer: 2**

Amazon Elastic Container Service (ECS) with the Fargate launch type

**Explanation:**

```
Amazon Elastic Container Service (ECS) with the EC2 launch type is incorrect. The EC2 launch type is not a fully managed service.
Amazon Elastic Container Service (ECS) with the Fargate launch type is correct. The Fargate launch type is a fully managed service.
Amazon Elastic Kubernetes Service (EKS) is incorrect. EKS is a managed service running the Kubernetes control plane. There are no specific requirements here for using Kubernetes so this is not the best option for quickly creating a platform for the developers.
Amazon Elastic Container Registry (ECR) is incorrect. ECR is a registry for storing container images.
```

## **Quiz: How can auto scaling be implemented for the ECS cluster instances?**

- [ ] This is not possible, you can only auto scale tasks using services
- [x] Using a Capacity Provider that is associated with an Auto Scaling Group (ASG)
- [ ] Using AWS Auto Scaling for Amazon ECS

<!-- #auto_scaling #ecs #asg -->

----

**Answer: 2**

**Explanation:**

```
1 is incorrect. This is no longer true since a recent feature update. Watch out for updates on the exam!
2 is correct. This is a new feature that may start appearing on the SAA-C02 version of the exam.
3 is incorrect. AWS Auto Scaling for Amazon ECS is not something that exists.
```

## **Quiz: You have some code that you would like to run occasionally and need to minimize costs. The completion time is typically under 10 minutes. Which solution is cost-effective and operationally efficient?**

- [ ] Run the code on an Amazon EC2 instance
- [ ] Run the code on an Amazon ECS task
- [ ] Run the code using AWS Batch
- [x] Run the code using an AWS Lambda function

<!-- #lambda #ec2 #aws_batch #ecs -->

---- 

**Answer: 4**

**Explanation:**

```
1 is incorrect. An EC2 instance is not cost-effective for a workload that needs to run only occasionally for 10 minutes.
2 is incorrect. An ECS task is not the most operationally effective option as you must spin up the ECS task to run the code and then manage the deletion of the task.
3 is incorrect. AWS Batch is used for running batch computing jobs on many EC2 instances. It’s not cost-effective or operationally effective for this use case.
4 is correct. This is the most cost-effective and operationally effective option. Remember that the maximum execution time is 900 seconds (15 minutes) so you are well within that timeframe here.
```

## **Quiz: Which of the following listener / protocol combinations is INCORRECT?**

- [x] Application Load Balancer TCP and HTTP/HTTPS
- [ ] Classic Load Balancer TCP and HTTP/HTTPS
- [ ] Network Load Balancer TCP

<!-- #alb #clb #nlb -->

----

**Answer: 1**

**Explanation:**

```
1 is correct. The ALB only support layer 7 which is HTTP and HTTPS – not TCP.
2 is incorrect. This is a correct combination of listener / protocol.
3 is incorrect. This is a correct combination of listener / protocol.
```

## **Quiz: Which type of scaling is provided by Amazon EC2 Auto Scaling?**

- [ ] Vertical
- [x] Horizontal

<!-- #auto_scaling  -->

----

**Answer: 2**

**Explanation:**

```
1 is incorrect. EC2 Auto Scaling is not an example of vertical scaling.
2 is correct. EC2 Auto Scaling scales horizontally by launching or terminating EC2 instances.
```