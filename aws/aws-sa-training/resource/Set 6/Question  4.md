#### Question  4


**An application makes calls to a REST API running on Amazon EC2 instances behind an Application Load Balancer (ALB).

Most API calls complete quickly. However, a single endpoint is making API calls that require much longer to complete and

this is introducing overall latency into the system. What steps can a Solutions Architect take to minimize the effects

of the long-running API calls?**


1: Change the EC2 instance to one with enhanced networking to reduce latency


2: Create an Amazon SQS queue and decouple the long-running API calls


3: Increase the ALB idle timeout to allow the long-running requests to complete


4: Change the ALB to a Network Load Balancer (NLB) and use SSL/TLS termination


Answer: 2


**Explanation:**


An Amazon Simple Queue Service (SQS) can be used to offload and decouple the long-running requests. They can then be

processed asynchronously by separate EC2 instances. This is the best way to reduce the overall latency introduced by the

long-running API call.


- CORRECT "Create an Amazon SQS queue and decouple the long-running API calls" is the correct answer.


- INCORRECT "Change the EC2 instance to one with enhanced networking to reduce latency" is incorrect. This will not

  reduce the latency of the API call as network latency is not the issue here, it is the latency of how long the API

  call takes to complete.


- INCORRECT "Increase the ALB idle timeout to allow the long-running requests to complete" is incorrect. The issue is

  not the connection being interrupted, it is that the API call takes a long time to complete.


- INCORRECT "Change the ALB to a Network Load Balancer (NLB) and use SSL/TLS termination" is incorrect. SSL/TLS

  termination is not of benefit here as the problem is not encryption or processing of encryption. The issue is API call

  latency.


**References:**


https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sqs/

