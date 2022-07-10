#### Question  11


**A Solutions Architect is designing an application that consists of AWS Lambda and Amazon RDS Aurora MySQL. The Lambda

function must use database credentials to authenticate to MySQL and security policy mandates that these credentials must

not be stored in the function code.**


**How can the Solutions Architect securely store the database credentials and make them available to the function?**


- [ ] Store the credentials in AWS Key Management Service and use environment variables in the function code pointing to

KMS


- [x] Store the credentials in Systems Manager Parameter Store and update the function code and execution role


- [ ] Use the AWSAuthenticationPlugin and associate an IAM user account in the MySQL database


- [ ] Create an IAM policy and store the credentials in the policy. Attach the policy to the Lambda function execution role



- hasExplain:: [[explanation_Question  11.md]]

#credentials #awsauthenticationplugin #aws #aurora #authenticate 