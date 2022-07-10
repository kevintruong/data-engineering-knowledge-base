#### Question  25


**An application on Amazon Elastic Container Service (ECS) performs data processing in two parts. The second part takes

much longer to complete. How can an Architect decouple the data processing from the backend application component?**


- [ ] Process both parts using the same ECS task. Create an Amazon Kinesis Firehose stream


- [ ] Process each part using a separate ECS task. Create an Amazon SNS topic and send a notification when the processing

completes


- [ ] Create an Amazon DynamoDB table and save the output of the first part to the table


- [x] Process each part using a separate ECS task. Create an Amazon SQS queue



- hasExplain:: [[explanation_Question  25.md]]

#separate_ecs_task #amazon_elastic_container_service #same_ecs_task #amazon_kinesis_firehose_stream #amazon_dynamodb_table 