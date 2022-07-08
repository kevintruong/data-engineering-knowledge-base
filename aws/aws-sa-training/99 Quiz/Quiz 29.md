## Quiz 29: A manual script that runs a few times a week and completes within 10 minutes needs to be replaced with an automated solution. Which of the following options should an Architect use?**

- [ ] Use a cron job on an Amazon EC2 instance
- [ ] Use AWS Batch
- [x] Use AWS Lambda
- [ ] Use AWS CloudFormation

----
Answer:

- [x] Use AWS Lambda
  **Explanation:**
  AWS Lambda has a maximum execution time of 900 seconds (15 minutes). Therefore the script will complete within this time. AWS Lambda is the best solution as you don’t need to run any instances (it’s serverless) and therefore you will pay only for the execution time.
- ✅: "Use AWS Lambda" is the correct answer.

- ❌: "Use a cron job on an Amazon EC2 instance" is incorrect. Cron Jobs are used for scheduling tasks to run on Linux instances. They are used for automating maintenance and administration. This is a workable solution for running a script but does require the instance to be running all the time. Also, AWS prefer you to use services such as AWS Lambda for centralized control and administration.

- ❌: "Use AWS Batch" is incorrect. AWS Batch is used for running large numbers of batch computing jobs on AWS. AWS Batch dynamically provisions the EC2 instances. This is not a good solution for an ad-hoc use case such as this one where you just need to run a single script a few times a week.

- ❌: "Use AWS CloudFormation" is incorrect. AWS CloudFormation is used for launching infrastructure. You can use scripts with AWS CloudFormation but its more about running scripts related to infrastructure provisioning.
  **References:**
  https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html



----
#quiz 
- relateTo:: [[Domain 1 Design Resilient Architectures]]