#### Question  22


**You recently noticed that your Network Load Balancer (NLB) in one of your VPCs is not distributing traffic evenly

between EC2 instances in your AZs. There are an odd number of EC2 instances spread across two AZs. The NLB is configured

with a TCP listener on port 80 and is using active health checks.**


**What is the most likely problem?**


- [ ] There is no HTTP listener


- [ ] Health checks are failing in one AZ due to latency


- [ ] NLB can only load balance within a single AZ


- [x] Cross-zone load balancing is disabled


*

- hasExplain:: [[explanation_Question  22.md]]