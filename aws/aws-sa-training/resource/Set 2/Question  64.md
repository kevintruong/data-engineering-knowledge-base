#### Question  64

**An EC2 instance that you manage has an IAM role attached to it that provides it with access to Amazon S3 for saving

log data to a bucket. A change in the application architecture means that you now need to provide the additional ability

for the application to securely make API requests to Amazon API Gateway.**

**Which two methods could you use to resolve this challenge? (Select TWO)**

- [ ] Delegate access to the EC2 instance from the API Gateway management console

- [ ] Create an IAM role with a policy granting permissions to Amazon API Gateway and add it to the EC2 instance as an

additional IAM role

- [ ] You cannot modify the IAM role assigned to an EC2 instance after it has been launched. You’ll need to recreate the

EC2 instance and assign a new IAM role

- [x] Add an IAM policy to the existing IAM role that the EC2 instance is using granting permissions to access Amazon API

Gateway

- [x] Create a new IAM role with multiple IAM policies attached that grants access to Amazon S3 and Amazon API Gateway, and

replace the existing IAM role that is attached to the EC2 instance

- hasExplain:: [[explanation_Question  64.md]]

# amazon_api_gateway #amazon_api #additional_iam_role #new_iam_role #ec2_instance
