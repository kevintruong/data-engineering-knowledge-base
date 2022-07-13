**Explanation:**

In this case we need to find a durable and loosely coupled solution for storing jobs. Amazon SQS is ideal for this use

case and can be configured to use dynamic scaling based on the number of jobs waiting in the queue.

To configure this scaling you can use the _backlog per instance_ metric with the target value being the _acceptable

backlog per instance_ to maintain. You can calculate these numbers as follows:

- **Backlog per instance** : To calculate your backlog per instance, start with the ApproximateNumberOfMessages queue

  attribute to determine the length of the SQS queue

  (number of messages available for retrieval from the queue). Divide that number by the fleet's running capacity, which

  for an Auto Scaling group is the number of instances in the InService state, to get the backlog per instance.

- **Acceptable backlog per instance** : To calculate your target value, first determine what your application can accept

  in terms of latency. Then, take the acceptable latency value and divide it by the average time that an EC2 instance

  takes to process a message.

This solution will scale EC2 instances using Auto Scaling based on the number of jobs waiting in the SQS queue.

- ✅ :  "Create an Amazon SQS queue to hold the jobs that needs to be processed. Create an Amazon EC2 Auto Scaling

  group for the compute application. Set the scaling policy for the Auto Scaling group to add and remove nodes based on

  the number of items in the SQS queue" is the correct answer.

- ❌ :  "Create an Amazon SQS queue to hold the jobs that need to be processed. Create an Amazon EC2 Auto Scaling

  group for the compute application. Set the scaling policy for the Auto Scaling group to add and remove nodes based on

  network usage" is incorrect as scaling on network usage does not relate to the number of jobs waiting to be processed.

- ❌ :  "Create an Amazon SNS topic to send the jobs that need to be processed. Create an Amazon EC2 Auto Scaling

  group for the compute application. Set the scaling policy for the Auto Scaling group to add and remove nodes based on

  CPU usage" is incorrect. Amazon SNS is a notification service so it delivers notifications to subscribers. It does

  store data durably but is less suitable than SQS for this use case. Scaling on CPU usage is not the best solution as

  it does not relate to the number of jobs waiting to be processed.

- ❌ :  "Create an Amazon SNS topic to send the jobs that need to be processed. Create an Amazon EC2 Auto Scaling

  group for the compute application. Set the scaling policy for the Auto Scaling group to add and remove nodes based on

  the number of messages published to the SNS topic" is incorrect. Amazon SNS is a notification service so it delivers

  notifications to subscribers. It does store data durably but is less suitable than SQS for this use case. Scaling on

  the number of notifications in SNS is not possible.

**References:**

<https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>- scaling/

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application>-

integration/amazon-sqs/

----

- #amazon_sqs_queue #amazon_ec2_auto_scaling #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto>-_scaling/> #sqs_queue #ec2_instances
