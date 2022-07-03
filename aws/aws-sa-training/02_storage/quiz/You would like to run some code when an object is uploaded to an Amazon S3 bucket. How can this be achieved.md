### **You would like to run some code when an object is uploaded to an Amazon S3 bucket. How can this be achieved?**

- [x] Create an event notification on the S3 bucket that triggers a Lambda function
- [ ] Configure Lambda to poll the S3 bucket for changes and run a function when it finds new objects
- [ ] Create an event notification on the S3 bucket that notifies Amazon SNS to trigger a Lambda function

----

**Answer:**
Create an event notification on the S3 bucket that triggers a Lambda function

**Explanation:**

- Create an event notification on the S3 bucket that triggers a Lambda function is correct. The best way to achieve this is to use an event notification on the S3 bucket that triggers a function that then runs the code.
- Configure Lambda to poll the S3 bucket for changes and run a function when it finds new objects is incorrect. Lambda does not poll S3.
- Create an event notification on the S3 bucket that notifies Amazon SNS to trigger a Lambda function is incorrect. You would not use Amazon SNS in this scenario as it is an unnecessary additional step.

---- 
#quiz 