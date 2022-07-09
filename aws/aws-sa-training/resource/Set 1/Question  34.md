#### Question  34


**A legacy tightly-coupled High Performance Computing (HPC) application will be migrated to AWS. Which network adapter

type should be used?**


1: Elastic Network Interface (ENI)


2: Elastic Network Adapter (ENA)


3: Elastic Fabric Adapter (EFA)


4: Elastic IP Address


Answer: 3


**Explanation:**


An Elastic Fabric Adapter is an AWS Elastic Network Adapter (ENA) with added capabilities. The EFA lets you apply the

scale, flexibility, and elasticity of the AWS Cloud to tightly-coupled HPC apps. It is ideal for tightly coupled app as

it uses the Message Passing Interface (MPI).


- CORRECT "Elastic Fabric Adapter (EFA)" is the correct answer.


- INCORRECT "Elastic Network Interface (ENI)" is incorrect. The ENI is a basic type of adapter and is not the best

  choice for this use case.


- INCORRECT "Elastic Network Adapter (ENA)" is incorrect. The ENA, which provides Enhanced Networking, does provide high

  bandwidth and low inter-instance latency but it does not support the features for a tightly- coupled app that the EFA

  does.


- INCORRECT "Elastic IP Address" is incorrect. An Elastic IP address is just a static public IP address, it is not a

  type of network adapter.


**References:**


https://aws.amazon.com/blogs/aws/now-available-elastic-fabric-adapter-efa-for-tightly-coupled-hpc-

workloads/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

