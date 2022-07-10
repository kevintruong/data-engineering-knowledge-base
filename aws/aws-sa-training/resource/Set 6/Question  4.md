#### Question  4


**An application makes calls to a REST API running on Amazon EC2 instances behind an Application Load Balancer (ALB).

Most API calls complete quickly. However, a single endpoint is making API calls that require much longer to complete and

this is introducing overall latency into the system. What steps can a Solutions Architect take to minimize the effects

of the long-running API calls?**


- [ ] Change the EC2 instance to one with enhanced networking to reduce latency


- [x] Create an Amazon SQS queue and decouple the long-running API calls


- [ ] Increase the ALB idle timeout to allow the long-running requests to complete


- [ ] Change the ALB to a Network Load Balancer (NLB) and use SSL/TLS termination



- hasExplain:: [[explanation_Question  4.md]]