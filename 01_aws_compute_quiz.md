### Compute Quiz Questions

Answers and explanations are provided below after the last question in this section.

**Question 1: What do you need to securely connect using SSH to an EC2 instance launched from the Amazon Linux 2 AMI?**

1. A signed cookie
2. An access key ID and secret access key
3. A key pair
4. A password

**Question 2: What can you use to run a script at startup on an Amazon EC2 Linux instance?**

1. User data
2. Metadata
3. AWS Batch
4. AWS Config

**Question 3: Which EC2 pricing model would you use for a short-term requirement that needs to complete over a weekend?**

1. Reserved Instance
2. Spot Instance
3. Dedicated Instance
4. On-Demand Instance

**Question 4: An organization uses an application that uses per-socket licensing and they need full control over the placement of their EC2 instances on underlying hardware. What should they use?**

1. Dedicated instances
2. Dedicated hosts
3. Spot instances
4. Reserved instances

**Question 5: What type of storage is suitable for a use case that requires extremely high- performance local disks that do not need to be persistent?**

1. Elastic Block Store (EBS)
2. Snapshots
3. Instance Store
4. Amazon S3

**Question 6: Which type of network adapter should be used for High Performance Computing (HPC) uses cases that include tightly coupled applications?**

1. Elastic Fabric Adapter (EFA)
2. Elastic Network Interface (ENI)
3. Elastic Network Adapter (ENA)

**Question 7: An Architect would like to use an Elastic Load Balancer to forward traffic to different back-end applications for https://dctlabs.com/orders and https://dctlabs.com/account. Which type of ELB should be used?**


1. Application Load Balancer with path-based routing
2. Application Load Balancer with host-based routing
3. Network Load Balancer with TCP port-based routing
4. Classic Load Balancer with Layer 7 routing

**Question 8: How can a systems administrator copy an EBS volume from the us-west-1a availability zone to an instance in the us-west-1b availability zone?**

1. Create a snapshot of the EBS volume in us-west-1a. Create a new volume in us-west-2b
    from the snapshot
2. Create a new EBS volume attached to the instance in us-west-2b. Attach the EBS volume to
    the instance in us-west-1b and copy data between volumes

**Question 9: Which type of data volume provides very high performance and is ideal for storing data which is either replicated between EC2 instances or is only temporary and can be lost?** 

1. Elastic Block Store (EBS)
2. Instance Store

**Question 10: The development department in your organization need to quickly access a platform for running Docker containers. The platform service should be fully managed. Which AWS service should you provision for them?**

1. Amazon Elastic Container Service (ECS) with the EC2 launch type
2. Amazon Elastic Container Service (ECS) with the Fargate launch type
3. Amazon Elastic Kubernetes Service (EKS)
4. Amazon Elastic Container Registry (ECR)

**Question 11: How can auto scaling be implemented for the ECS cluster instances?** 

1. This is not possible, you can only auto scale tasks using services
2. Using a Capacity Provider that is associated with an Auto Scaling Group (ASG)
3. Using AWS Auto Scaling for Amazon ECS

**Question 12: You have some code that you would like to run occasionally and need to minimize costs. The completion time is typically under 10 minutes. Which solution is cost-effective and operationally efficient?**

1. Run the code on an Amazon EC2 instance
2. Run the code on an Amazon ECS task
3. Run the code using AWS Batch
4. Run the code using an AWS Lambda function

**Question 13: Which of the following listener / protocol combinations is INCORRECT?** 

1. Application Load Balancer TCP and HTTP/HTTPS
2. Classic Load Balancer TCP and HTTP/HTTPS
3. Network Load Balancer TCP

**Question 14: Which type of scaling is provided by Amazon EC2 Auto Scaling?**

1. Vertical
2. Horizontal


**COMPUTE - ANSWERS**

**Question 1, Answer: 3**

**Explanation:**

```
1 is incorrect. Signed cookies are not an authentication method for EC2.
2 is incorrect. An access key ID and secret access key are used for programmatic access to AWS
services, not for securely connecting to Linux instances over SSH. Make sure you know the
difference between these two concepts.
3 is correct. Key pairs are used to securely connect to EC2 instances. A key pair consists of a
public key that AWS stores, and a private key file that you store. For Linux AMIs, the private
key file allows you to securely SSH (secure shell) into your instance.
4 is incorrect. You do not need a password to connect to instances launched from the Amazon
Linux 2 AMI.
```
**Question 2, Answer: 1**

**Explanation:**

```
1 is correct. User data is data that is supplied by the user at instance launch in the form of a
script.
2 is incorrect. Instance metadata is data about your instance that you can use to configure or
manage the running instance.
3 is incorrect. AWS Batch is used for running batch computing jobs across many instances.
4 is incorrect. AWS Config is a service that enables you to assess, audit, and evaluate the
configurations of your AWS resources.
```
**Question 3, Answer: 4**

**Explanation:**

```
1 is incorrect. Reserved instances require a commitment over 1 or 3 years.
2 is incorrect. Spot instances are good for cost-sensitive workloads that can afford to be
interrupted. This workload must complete so Spot instances would not be ideal.
3 is incorrect. Dedicated Instances are Amazon EC2 instances that run in a VPC on hardware
that's dedicated to a single customer. This would be more expensive and there is no need for
dedicated hardware in this case.
4 is correct. On-demand instances are ideal for short-term or unpredictable workloads. You don’t
get a discount, but you do have more flexibility with no commitments.
```
**Question 4, Answer: 2**

**Explanation:**

```
1 is incorrect. Dedicated instances provide dedicated hardware, but you don’t get visibility of
sockets, cores, or targeted instance placement.
2 is correct. Dedicated hosts provide dedicated hardware and they give you full visibility of
sockets and cores and targeted instance placement.
3 is incorrect. With Spot instances you do not have control of instance placement on underlying
hardware.
4 is incorrect. With Reserved instances you do not have control of instance placement on
```

```
underlying hardware.
```
**Question 5, Answer: 3**

**Explanation:**

```
1 is incorrect. EBS volumes are persistent. You can get high performance, but they are network
attached disks, not local disks.
2 is incorrect. Snapshots are used for taking a backup of EBS volumes.
3 is correct. Instance store volumes are ephemeral (non-persistent) local disks that offer very
high performance.
4 is incorrect. Amazon S3 is an object storage system. It is not a local disk nor is it non-persistent.
```
**Question 6, Answer: 1**

**Explanation:**

```
1 is correct. EFA is good for High Performance Computing, MPI and ML use cases, tightly coupled
applications and can be used with all instance types.
2 is incorrect. ENIs are the basic adapter type for when you don’t have any high-performance
requirements.
3 is incorrect. ENAs are good for use cases that require higher bandwidth and lower inter-
instance latency.
```
**Question 7, Answer: 1**

**Explanation:**

```
1 is correct. To forward based on the path (e.g. /orders or /account) you can use the ALB with
path-based routing.
2 is incorrect. Host-based routing uses the host name (e.g. dctlabs.com or amazon.com) rather
than the path (e.g. /orders or /account).
3 is incorrect. The NLB can forward based on different ports/listeners. However all of this traffic
will be coming on the single port for HTTPS (443).
4 is incorrect. The CLB is a layer 7 router but there is not concepts of path-based routing.
```
**Question 8, Answer: 1**

**Explanation:**

```
1 is correct. This is the best method for copying an EBS volume between AZs. Remember,
snapshots are stored on Amazon S3 which stores data within a region, not an AZ.
2 is incorrect. You cannot attach an EBS volume to an instance in a different AZ.
```
**Question 9, Answer: 2**

**Explanation:**

```
1 is incorrect. EBS is persistent storage and though it provides high performance it may not be
the best solution for data that is replicated or can be lost.
2 is correct. This is a good use case for Instance Store storage. It can also be cost-effective as it
comes with the price of the EC2 instance.
```
**Question 10, Answer: 2**


**Explanation:**

```
1 is incorrect. The EC2 launch type is not a fully managed service.
2 is correct. The Fargate launch type is a fully managed service.
3 is incorrect. EKS is a managed service running the Kubernetes control plane. There are no
specific requirements here for using Kubernetes so this is not the best option for quickly
creating a platform for the developers.
4 is incorrect. ECR is a registry for storing container images.
```
**Question 11, Answer: 2**

**Explanation:**

```
1 is incorrect. This is no longer true since a recent feature update. Watch out for updates on the
exam!
2 is correct. This is a new feature that may start appearing on the SAA-C02 version of the exam.
3 is incorrect. AWS Auto Scaling for Amazon ECS is not something that exists.
```
**Question 12, Answer: 4**

**Explanation:**

```
1 is incorrect. An EC2 instance is not cost-effective for a workload that needs to run only
occasionally for 10 minutes.
2 is incorrect. An ECS task is not the most operationally effective option as you must spin up the
ECS task to run the code and then manage the deletion of the task.
3 is incorrect. AWS Batch is used for running batch computing jobs on many EC2 instances. It’s
not cost-effective or operationally effective for this use case.
4 is correct. This is the most cost-effective and operationally effective option. Remember that
the maximum execution time is 900 seconds (15 minutes) so you are well within that
timeframe here.
```
**Question 13, Answer: 1**

**Explanation:**

```
1 is correct. The ALB only support layer 7 which is HTTP and HTTPS – not TCP.
2 is incorrect. This is a correct combination of listener / protocol.
3 is incorrect. This is a correct combination of listener / protocol.
```
**Question 14, Answer: 2**

**Explanation:**

```
1 is incorrect. EC2 Auto Scaling is not an example of vertical scaling.
2 is correct. EC2 Auto Scaling scales horizontally by launching or terminating EC2 instances.
```