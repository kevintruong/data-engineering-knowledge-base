#### Question  22

**An application running on an Amazon ECS container instance using the EC2 launch type needs permissions to write data

to Amazon DynamoDB.**

**How can you assign these permissions only to the specific ECS task that is running the application?**

- [ ] :  Create an IAM policy with permissions to DynamoDB and attach it to the container instance

- [x] :  Create an IAM policy with permissions to DynamoDB and assign It to a task using the _taskRoleArn_ parameter

- [ ] :  Use a security group to allow outbound connections to DynamoDB and assign it to the container instance

- [ ] :  Modify the _AmazonECSTaskExecutionRolePolicy_ policy to add permissions for DynamoDB

----

- #specific_ecs_task #amazon_dynamodb #amazon_ecs_container_instance #dynamodb #ec2_launch_type
- hasExplain:: [[explanation_Question  22.md]]
