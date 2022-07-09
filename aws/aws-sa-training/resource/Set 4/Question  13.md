#### Question  13


**An application that runs a computational fluid dynamics workload uses a tightly-coupled HPC architecture that uses the

MPI protocol and runs across many nodes. A service-managed deployment is required to minimize operational overhead.**


**Which deployment option is MOST suitable for provisioning and managing the resources required for this use case?**


1: Use Amazon EC2 Auto Scaling to deploy instances in multiple subnets


2: Use AWS CloudFormation to deploy a Cluster Placement Group on EC2


3: Use AWS Batch to deploy a multi-node parallel job


4: Use AWS Elastic Beanstalk to provision and manage the EC2 instances


Answer: 3


**Explanation:**


AWS Batch Multi-node parallel jobs enable you to run single jobs that span multiple Amazon EC2 instances. With AWS Batch

multi-node parallel jobs, you can run large-scale, tightly coupled, high performance


computing applications and distributed GPU model training without the need to launch, configure, and manage Amazon EC2

resources directly.


An AWS Batch multi-node parallel job is compatible with any framework that supports IP-based, internode communication,

such as Apache MXNet, TensorFlow, Caffe2, or Message Passing Interface (MPI).


This is the most efficient approach to deploy the resources required and supports the application requirements most

effectively.


- CORRECT "Use AWS Batch to deploy a multi-node parallel job" is the correct answer.


- INCORRECT "Use Amazon EC2 Auto Scaling to deploy instances in multiple subnets " is incorrect. This is not the best

  solution for a tightly-coupled HPC workload with specific requirements such as MPI support.


- INCORRECT "Use AWS CloudFormation to deploy a Cluster Placement Group on EC2" is incorrect. This would deploy a

  cluster placement group but not manage it. AWS Batch is a better fit for large scale workloads such as this.


- INCORRECT "Use AWS Elastic Beanstalk to provision and manage the EC2 instances" is incorrect. You can certainly

  provision and manage EC2 instances with Elastic Beanstalk but this scenario is for a specific workload that requires

  MPI support and managing a HPC deployment across a large number of nodes. AWS Batch is more suitable.


**References:**


https://d1.awsstatic.com/whitepapers/architecture/AWS-HPC-Lens.pdf


https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html

