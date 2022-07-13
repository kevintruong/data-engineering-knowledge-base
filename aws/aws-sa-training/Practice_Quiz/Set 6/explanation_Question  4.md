**Explanation:**

An Amazon Simple Queue Service (SQS) can be used to offload and decouple the long-running requests. They can then be

processed asynchronously by separate EC2 instances. This is the best way to reduce the overall latency introduced by the

long-running API call.

- ✅ :  "Create an Amazon SQS queue and decouple the long-running API calls" is the correct answer.

- ❌ :  "Change the EC2 instance to one with enhanced networking to reduce latency" is incorrect. This will not

  reduce the latency of the API call as network latency is not the issue here, it is the latency of how long the API

  call takes to complete.

- ❌ :  "Increase the ALB idle timeout to allow the long-running requests to complete" is incorrect. The issue is

  not the connection being interrupted, it is that the API call takes a long time to complete.

- ❌ :  "Change the ALB to a Network Load Balancer (NLB) and use SSL/TLS termination" is incorrect. SSL/TLS

  termination is not of benefit here as the problem is not encryption or processing of encryption. The issue is API call

  latency.

**References:**

<https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>-

integration/amazon-sqs/

----

- #amazon_simple_queue_service #amazon_sqs_queue #ec2_instance #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>>- #separate_ec2_instances
