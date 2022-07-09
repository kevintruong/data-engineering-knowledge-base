#### Question  30


**A High Performance Computing (HPC) application will be migrated to AWS. The application requires low network latency

and high throughput between nodes and will be deployed in a single AZ.**


**How should the application be deployed for best inter-node performance?**


1: In a partition placement group


2: In a cluster placement group


3: In a spread placement group


4: Behind a Network Load Balancer (NLB)


Answer: 2


**Explanation:**


A cluster placement group provides low latency and high throughput for instances deployed in a single AZ. It is the best

way to provide the performance required for this application.


- CORRECT "In a cluster placement group" is the correct answer.


- INCORRECT "In a partition placement group" is incorrect. A partition placement group is used for grouping instances

  into logical segments. It provides control and visibility into instance placement but is not the best option for

  performance.


- INCORRECT "In a spread placement group" is incorrect. A spread placement group is used to spread instances across

  underlying hardware. It is not the best option for performance.


- INCORRECT "Behind a Network Load Balancer (NLB)" is incorrect. A network load balancer is used for distributing

  incoming connections, this does assist with inter-node performance.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ec2/

