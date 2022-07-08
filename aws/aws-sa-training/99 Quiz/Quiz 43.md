## Quiz 43: A Solutions Architect needs to improve performance for a web application running on EC2 instances launched by an Auto Scaling group. The instances run behind an ELB Application Load Balancer. During heavy use periods the ASG doubles in size and analysis has shown that static content stored on the EC2 instances is being requested by users in a specific geographic location.**

**How can the Solutions Architect reduce the need to scale and improve the application performance?**

- [ ] Store the contents on Amazon EFS instead of the EC2 root volume

- [ ] Implement Amazon Redshift to create a repository of the content closer to the users

- [x] Create an Amazon CloudFront distribution for the site and redirect user traffic to the distribution

- [ ] Re-deploy the application in a new VPC that is closer to the users making the requests

----
Answer: 3
**Explanation:**
This is a good use case for CloudFront. CloudFront is a content delivery network (CDN) that caches content closer to users. You can cache the static content on CloudFront using the EC2 instances as origins for the content. This will improve performance (as the content is closer to the users) and reduce the need for the ASG to scale (as you don’t need the processing power of the EC2 instances to serve the static content).

- ✅: "Create an Amazon CloudFront distribution for the site and redirect user traffic to the distribution"

  is the correct answer.

- ❌: "Store the contents on Amazon EFS instead of the EC2 root volume" is incorrect. Using EFS instead of the EC2 root volume does not solve either problem.

- ❌: "Implement Amazon Redshift to create a repository of the content closer to the users" is incorrect. RedShift cannot be used to create content repositories to get content closer to users, it’s a data warehouse used for analytics.

- ❌: "Re-deploy the application in a new VPC that is closer to the users making the requests" is incorrect. Re-deploying the application in a VPC closer to the users may reduce latency (and therefore improve performance), but it doesn’t solve the problem of reducing the need for the ASG to scale.
  **References:**
  https://aws.amazon.com/caching/cdn/
  delivery/amazon-cloudfront/
  **44. Question**
  A company needs to store data for 5 years. The company will need to have immediate and highly available access to the data at any point in time but will not require frequent access. Which lifecycle action should be taken to meet the requirements while reducing costs?
- [ ] Transition objects from Amazon S3 Standard to the GLACIER storage class

- [ ] Transition objects to expire after 5 years

- [x] Transition objects from Amazon S3 Standard to Amazon S3 Standard-Infrequent Access (S3 Standard-IA)

- [ ] Transition objects from Amazon S3 Standard to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)

----
Answer: 3
**Explanation:**
This is a good use case for S3 Standard-IA which provides immediate access and 99.9% availability.

- ✅: "Transition objects from Amazon S3 Standard to Amazon S3 Standard-Infrequent Access (S3 Standard-IA)" is the correct answer.

- ❌: "Transition objects from Amazon S3 Standard to the GLACIER storage class" is incorrect. The Glacier storage class does not provide immediate access. You can retrieve within hours or minutes, but you do need to submit a job to retrieve the data.

- ❌: "Transition objects to expire after 5 years" is incorrect. Expiring the objects after 5 years is going to delete them at the end of the 5-year period, but you still need to work out the best storage solution to use before then, and this answer does not provide a solution.

- ❌: "Transition objects from Amazon S3 Standard to Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)" is incorrect. The S3 One Zone-IA tier provides immediate access, but the availability is lower at 99.5% so this is not the best option.
  **References:**
  https://aws.amazon.com/s3/storage-classes/
