## WELCOME

Thanks for purchasing these training notes for the **AWS Certified Solutions Architect Associate**
exam from Digital Cloud Training. The information in this document relates to the latest SAA-C version of the exam blueprint that replaced the SAA-C01 exam as of June 30, 2020.

The aim of putting all of the exam-specific information together into one document is to provide a centralized, detailed list of the facts you need to know before you sit the exam. This will shortcut your study time and maximize your chance of passing the AWS Certified Solutions Architect exam first time.

I trust that you get great value from this popular resource that has been well received by our pool of over 25 0,000 students. Through diligent study of these learning materials, you will be in the perfect position to ace your AWS Certified Solutions Architect Associate exam first time.

Wishing you all the best with your AWS Certification exam.

Neal Davis

**Founder of Digital Cloud Training**

### About these Training Notes

Please note that this document does not read like a book or instructional text. We provide a raw, point-to-point list of facts backed by tables and diagrams to help with understanding.

For easy navigation, the information on each AWS service in this document is organized into the same categories as they are in the AWS Management Console.

The scope of coverage of services, and what information is included for each service, is based on feedback from our pool of over 2 50,000 students who have taken the exam, as well as our own experience.

To test your understanding, we have added **80 quiz questions** that you will find at the end of each major chapter. Please note that quiz questions that are **numbered** , are primarily designed as a tool to review your knowledge of the content that was presented within the section. Quiz questions that are **lettered** represent the AWS exam style or difficulty. You will also find examples of exam style practice questions within the chapter "How to best prepare for your exam".

### What do other Students say?

Check out the excellent reviews from our many students who passed their AWS exam with an average passing score of over 850 :

*****

_A wide collection of the important concepts that one needs to know to pass the AWS Certified Solutions Architect Associate exam. This was my go-to resource as I was preparing for my exam._

*****

_This is a terrific book to review what you need to know for the certification exam of AWS Solutions Architect – Associate. It succinctly presents all the important points of every subject in that arena._

*****

_The material includes tons of facts and explanations of the exam objectives. Very well organized and it comes with some practice tests that simulate real-world scenarios._

*****

_The book is a very concise collection of the important facts one needs to know to pass the AWS Certified Solutions Architect Associate exam. It was my go-to resource during my final phase of preparing for the exam – which I easily passed._

*****

_The quick notes on what you need to pass. Also, I passed and it was one of the tools I used to get certified. All the screen time it was time to give my eyes a break._

## TABLE OF CONTENTS

- [WELCOME](#welcome)
    - [About these Training Notes](#about-these-training-notes)
    - [What do other Students say?](#what-do-other-students-say)
- [TABLE OF CONTENTS](#table-of-contents)
- [GETTING STARTED](#getting-started)
    - [Your Pathway to Success](#your-pathway-to-success)
    - [Support & Feedback](#support--feedback)
    - [Join the AWS Community](#join-the-aws-community)
    - [Connect with Neal on Social Media](#connect-with-neal-on-social-media)
- [HOW TO BEST PREPARE FOR YOUR EXAM](#how-to-best-prepare-for-your-exam)
    - [The 2020 SAA-C02 Exam Version](#the-2020-saa-c02-exam-version)
    - [Domains, Objectives and Examples](#domains-objectives-and-examples)
- [COMPUTE](#compute)
    - [Amazon EC2](#amazon-ec2)
        - [AMAZON MACHINE IMAGES](#amazon-machine-images)
    - [Amazon EBS](#amazon-ebs)
    - [Elastic Load Balancing](#elastic-load-balancing)
    - [AWS Auto Scaling](#aws-auto-scaling)
    - [Amazon ECS](#amazon-ecs)
    - [AWS Lambda](#aws-lambda)
    - [AWS Elastic Beanstalk](#aws-elastic-beanstalk)
    - [Compute Quiz Questions](#compute-quiz-questions)
- [STORAGE](#storage)
    - [Amazon S3](#amazon-s3)
    - [S3 performance guidelines](#s3-performance-guidelines)
    - [Glacier](#glacier)
    - [Amazon EFS](#amazon-efs)
    - [AWS Storage Gateway](#aws-storage-gateway)
    - [Amazon fsx](#amazon-fsx)
    - [Storage Quiz Questions](#storage-quiz-questions)
- [AWS DATABASE](#aws-database)
    - [Amazon RDS](#amazon-rds)
    - [Amazon Aurora](#amazon-aurora)
    - [Amazon DynamoDB](#amazon-dynamodb)
    - [Amazon ElastiCache](#amazon-elasticache)
    - [Amazon RedShift](#amazon-redshift)
    - [Database Quiz Questions](#database-quiz-questions)
- [MIGRATION](#migration)
    - [AWS Snowball](#aws-snowball)
    - [AWS Database Migration Service](#aws-database-migration-service)
    - [AWS DataSync](#aws-datasync)
    - [Migration Quiz Question](#migration-quiz-question)
- [NETWORKING AND CONTENT DELIVERY](#networking-and-content-delivery)
    - [Amazon VPC](#amazon-vpc)
    - [Amazon CloudFront](#amazon-cloudfront)
    - [Amazon Route](#amazon-route)
    - [AWS Global Accelerator](#aws-global-accelerator)
    - [Amazon API Gateway](#amazon-api-gateway)
    - [AWS Direct Connect](#aws-direct-connect)
    - [Networking & Content Delivery Quiz Questions](#networking--content-delivery-quiz-questions)
- [MANAGEMENT TOOLS](#management-tools)
    - [Amazon CloudWatch](#amazon-cloudwatch)
    - [AWS CloudTrail](#aws-cloudtrail)
    - [AWS OpsWorks](#aws-opsworks)
    - [AWS CloudFormation](#aws-cloudformation)
    - [AWS Config](#aws-config)
    - [AWS Systems Manager](#aws-systems-manager)
    - [Management Tools Quiz Questions](#management-tools-quiz-questions)
- [MEDIA SERVICES](#media-services)
    - [Amazon Elastic Transcoder](#amazon-elastic-transcoder)
    - [Media Services Quiz Questions](#media-services-quiz-questions)
- [ANALYTICS](#analytics)
    - [Amazon EMR](#amazon-emr)
    - [Amazon Kinesis](#amazon-kinesis)
    - [Amazon Athena](#amazon-athena)
    - [AWS Glue](#aws-glue)
    - [Analytics Quiz Questions](#analytics-quiz-questions)
- [AWS SECURITY, IDENTITY & COMPLIANCE](#aws-security-identity--compliance)
    - [AWS IAM](#aws-iam)
    - [AWS Accounts](#aws-accounts)
    - [AWS Resource access manager](#aws-resource-access-manager)
    - [Resource Groups](#resource-groups)
    - [AWS Directory Service](#aws-directory-service)
    - [AWS Key Management Store (KMS)](#aws-key-management-store-kms)
    - [AWS CloudHSM](#aws-cloudhsm)
    - [Amazon Cognito](#amazon-cognito)
    - [AWS WAF and Shield](#aws-waf-and-shield)
    - [Security, Identity & Compliance Quiz Questions](#security-identity--compliance-quiz-questions)
- [APPLICATION INTEGRATION](#application-integration)
    - [Amazon SNS](#amazon-sns)
    - [Amazon SQS](#amazon-sqs)
    - [Amazon Simple Workflow Service (SWF)](#amazon-simple-workflow-service-swf)
    - [Amazon MQ](#amazon-mq)
    - [AWS Step Functions](#aws-step-functions)
    - [Application Integration Quiz Questions](#application-integration-quiz-questions)
- [AWS DESKTOP & APP STREAMING](#aws-desktop--app-streaming)
    - [Amazon Workspaces](#amazon-workspaces)
- [CONCLUSION](#conclusion)
    - [Before taking the AWS Exam](#before-taking-the-aws-exam)
    - [Reach out and Connect](#reach-out-and-connect)
- [OTHER BOOKS & COURSES BY NEAL DAVIS](#other-books--courses-by-neal-davis)
    - [Courses for the AWS Certified Cloud Practitioner](#courses-for-the-aws-certified-cloud-practitioner)
    - [Courses for the AWS Certified Solutions Architect Associate](#courses-for-the-aws-certified-solutions-architect-associate)
    - [Courses for the AWS Certified Developer Associate](#courses-for-the-aws-certified-developer-associate)
    - [Courses for the AWS Certified SysOps Administrator Associate](#courses-for-the-aws-certified-sysops-administrator-associate)
- [ABOUT THE AUTHOR](#about-the-author)

## GETTING STARTED

### Your Pathway to Success

So, you’re excited to get started with the AWS Certified Solutions Architect Associate certification and wondering what resources are out there to help you. Let’s start with the free options. Visit https://digitalcloud.training/amazon-aws-free-certification-training-solutions-architect for links to various free resources including sample practice questions, blog articles, video tutorials and AWS documentation.

For the full training experience though, your best bet are the following training courses:

**Step 1: Enroll in the Instructor-led Video Course**

To get you started, we’d suggest first enrolling in the on-demand AWS Certified Solutions Architect Associate Video Course from Digital Cloud Training to familiarize yourself with the AWS platform before returning to the Training Notes to get a more detailed understanding of the AWS services.

For more information, visit: https://digitalcloud.training/aws-certified-solutions-architect-associate- hands-on-course-saa-c

**Step 2: Practice Exam Course with online Exam Simulator (**

**Practice Questions)**

To assess where you are at on your AWS journey, we recommend taking the AWS Certified Solutions Architect Associate Practice Exams on the Digital Cloud Training website. The **online exam simulator** with over **500 unique questions** will help you identify your strengths and weaknesses. These practice tests are designed to reflect the difficulty of the AWS exam and are the closest to the real exam experience available. To learn more, visit https://digitalcloud.training/aws-certified- solutions-architect-associate-practice-tests-saa-c

Our online Practice Exams are delivered in 4 different variations:

- **Exam Mode**
  In exam simulation mode, you complete one full-length practice exam and answer all 65 questions within the allotted time. You are then presented with a pass / fail score report showing your overall score and performance in each knowledge area to identify your strengths and weaknesses.
- **Training Mode**
  When taking the practice exam in training mode, you will be shown the answers and explanations for every question after clicking “check”. Upon completion of the exam, the score report will show your overall score and performance in each knowledge area.
- **Knowledge Reviews**
  Now that you have identified your strengths and weaknesses, you get to dive deep into specific areas with our knowledge reviews. You are presented with a series of questions focussed on a specific topic. There is no time limit and you can view the answer to each question as you go through them.
- **Final Exam Simulator**
  The exam simulator randomly selects 65 questions from our pool of over 500 unique questions – mimicking the real AWS exam environment. The practice exam has the same format, style, time limit and passing score as the real AWS exam

**Step 3: Training Notes**

As a final step, use these training notes to focus your study on the knowledge areas where you need to most. Get a detailed understanding of the AWS services and deep dive into the SAA-C02 exam objectives with detailed facts, tables and diagrams that will shortcut your time to success.

### Support & Feedback

We want you to get great value from these training resources. If for any reason you are not 100% satisfied, please contact us at support@digitalcloud.training. We promise to address all questions and concerns, typically within 24hrs. We really want you to have a 5 - star learning experience!

The AWS platform is evolving quickly, and the exam tracks these changes with a typical lag of around 6 months. We are therefore reliant on student feedback to keep track of what is appearing in the exam. If there are any topics in your exam that weren't covered in our training resources, please provide us with feedback using this form https://digitalcloud.training/student-feedback. We appreciate any feedback that will help us further improve our AWS training resources.

### Join the AWS Community

Our private Facebook group is a great place to ask questions and share knowledge and exam tips with the AWS community. Join the AWS Certification QA group on Facebook and share your exam

feedback with the AWS community: https://www.facebook.com/groups/awscertificationqa

To join the discussion about all things related to Amazon Web Services on Slack, visit:
[http://digitalcloud.training/slack](http://digitalcloud.training/slack) for instructions.

### Connect with Neal on Social Media

To learn more about the different ways of connecting with Neal, visit:
https://digitalcloud.training/neal-davis

```
digitalcloud.training/n eal-davis
```

```
https://www.youtube.com/c/digitalclo udtraining
```

```
facebook.com/digitalcl oudtraining
```

```
Twitter @nealkdavis
```

```
linkedin.com/in/nealkd avis
```

```
Instagram @digitalcloudtraining
```

## HOW TO BEST PREPARE FOR YOUR EXAM

### The 2020 SAA-C02 Exam Version

The **new SAA-C02 exam** for the **AWS Certified Solutions Architect Associate certification** has been available since March 2020. The old version of the exam was retired on 1st July 2020 after it was extended for an extra couple of months due to the exam testing center closures caused by the COVID- 19 pandemic. The new exam has been updated with new content to align with the latest AWS features and services.

To help you best prepare for the AWS Certified Solutions Architect Associate SAA-C02 exam, let's have a closer look at the exam blueprint and break down the various "domains" of the exam guide so you know what to expect.

**THE AWS EXAM BLUEPRINT**

The AWS Certified Solutions Architect Associate exam is recommended for individuals with at least one year of hands-on experience. The exam is intended for Solutions Architects and requires you to demonstrate knowledge of how to define a solution using architectural design principles based on customer requirements and provide implementation guidance based on best practices to the organization throughout the lifecycle of the project.

In the official Exam Guide for the AWS Certified Solutions Architect, the following **AWS knowledge is recommended:**

- One year of hands-on experience designing available, cost-efficient, fault-tolerant, and scalable distributed systems on AWS.
- Hands-on experience using compute, networking, storage and database AWS services.
- Hands-on experience with AWS deployment and management services.
- Ability to identify and define technical requirements for an AWS-based application.
- Ability to identify which AWS services meet a given technical requirement.
- Knowledge of recommended best practices for building secure and reliable applications on the AWS platform.
- An understanding of the basic architectural principles of building on the AWS cloud.
- An understanding of the AWS global infrastructure.
- An understanding of network technologies as they relate to AWS.
- An understanding of security features and tools that AWS provides and how they relate to traditional services.

**The exam includes 65 questions and has a time limit of 130 minutes**. You need to score a minimum of 720 out of 1000 points to pass the exam.

The question format of the exam is multiple-choice (one correct response from four options) and multiple response (two or more correct responses from five or more options). The questions are 100% scenario based with most scenarios being just a couple to a few lines long.

You will find there are often multiple correct answers and you must select the answer that best fits the scenario. For instance, you may be asked to select the MOST secure, MOST cost-effective, BEST architecture or LEAST complex option.

**Important** : Be very careful reading the wording of the question to ensure you select correctly. Sometimes small details can be easily missed that change the answer so take your time when sitting the exam.

### Domains, Objectives and Examples

The knowledge required is organized into four test “domains”. Within each test domain, there are several objectives that broadly describe the knowledge and experience required to pass the exam.

**Test Domain 1: Design Resilient Architectures**

This domain makes up 30% of the exam and includes the following four objectives:

1.1 Design a multi-tier architecture solution.

1.2 Design highly available and/or fault-tolerant architectures.

1.3 Design decoupling mechanisms using AWS services.

1.4 Choose appropriate resilient storage.

**What you need to know**

You need to understand the various block, file and object storage technologies such as Amazon EBS, Instance Store, Amazon EFS, Amazon S3, and Amazon FSx and know their use cases.

You must be able to design multi-tier application architectures and know-how to decouple application components using technologies such as Amazon SQS and Amazon SWF.

The architectures also need to be highly available in the case of component failure, and able to recover in the case of major outages, so you need to know the various ways of implementing high availability and fault tolerance.

Technologies you need to understand include Amazon Elastic Load Balancing, Amazon Route 53 and Amazon RDS Read Replicas and Multi-AZ.

You also need to understand the AWS Global Infrastructure in order to determine how to design application stacks to best use the underlying infrastructure architecture.

**Example Questions**

**Question:** You are a Solutions Architect at a media company, and you need to build an application stack that can receive customer comments from sporting events. The application is expected to receive significant load that could scale to millions of messages within a short space of time following high-profile matches.

As you are unsure of the load required for the database layer what is the most cost-effective way to ensure that the messages are not dropped?

1. Use RDS Auto Scaling for the database layer which will automatically scale as required
2. Create an SQS queue and modify the application to write to the SQS queue. Launch another application instance that polls the queue and writes messages to the database
3. Write the data to an S3 bucket, configure RDS to poll the bucket for new messages
4. Use DynamoDB and provision enough write capacity to handle the highest expected load

**Answer: 2** , Amazon Simple Queue Service (Amazon SQS) offers a reliable, highly scalable, hosted queue for storing messages in transit between computers and is used for distributed/decoupled applications. This is a great use case for SQS as you don’t have to over-provision the database layer or worry about messages being dropped.

**Question:** A new Big Data application you are developing will use hundreds of EC2 instances to write data to a shared file system. The file system must be stored redundantly across multiple AZs within a region and allow the EC2 instances to concurrently access the file system. The required throughput is multiple GB per second.

From the options presented which storage solution can deliver these requirements?

1. Amazon EBS using multiple volumes in a RAID 0 configuration
2. Amazon S
3. Amazon EFS
4. Amazon Storage Gateway

**Answer: 3** , Amazon EFS is the best solution as it is the only solution that is a file-level storage solution (not block/object-based), stores data redundantly across multiple AZs within a region and you can concurrently connect up to thousands of EC2 instances to a single filesystem.

**Test Domain 2: Design High-Performing Architectures**

This domain makes up 28% of the exam and includes the following **objectives** :

2.1 Identify elastic and scalable compute solutions for a workload.

2.2 Select high-performing and scalable storage solutions for a workload.

2.3 Select high-performing networking solutions for a workload.

2.4 Choose high-performing database solutions for a workload.

**What you need to know**

You need to be able to select the best storage and database services to use for a given scenario, taking into account requirements for performance.

Technologies to increase performance may include a caching layer such as Amazon ElastiCache, Amazon DynamoDB DAX, or Amazon CloudFront and you must be able to select the best service to use in the situation presented.

You must know how to effectively implement elasticity and scalability to your application architectures. This means understanding at an architectural and implementation level what to use and how to build it.

Elasticity and scalability services you need to understand, include AWS Auto Scaling, EC2 Auto Scaling, and how to implement these features at the application, storage, and database layers of your application using AWS technology.

**Example Questions**

**Question:** A developer is creating a solution for a real-time bidding application for a large retail company that allows users to bid on items of end-of-season clothing. The application is expected to be extremely popular and the back-end DynamoDB database may not perform as required.

How can the Solutions Architect enable in-memory read performance with microsecond response times for the DynamoDB database?

1. Configure DynamoDB Auto Scaling
2. Enable read replicas
3. Increase the provisioned throughput
4. Configure Amazon DAX

**Answer:** 4, Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache for DynamoDB that delivers up to a 10x performance improvement – from milliseconds to microseconds – even at millions of requests per second. You can enable DAX for a DynamoDB database with a few clicks.

**Question:** A Solutions Architect is designing a workload that requires a high-performance object- based storage system that must be shared with multiple Amazon EC2 instances.

Which AWS service delivers these requirements?

1. Amazon S3
2. Amazon EFS
3. Amazon EBS
4. Amazon ElastiCache

**Answer:** 1, Amazon S3 is an object-based storage system. Though object storage systems aren’t mounted and shared like filesystems or block-based storage systems, they can be shared by multiple instances as they allow concurrent access.

**Test Domain 3: Design Secure Applications and Architectures**

This domain makes up 24% of the exam and includes the following three objectives:

3.1 Design secure access to AWS resources.

3.2 Design secure application tiers.

3.3 Select appropriate data security options.

**What you need to know**

You need to understand how to use native AWS technologies and solution architecture to create secure applications. This includes configuring security controls for authentication, authorization, and access and applying encryption to data.

You need to know how to design isolation and separation through AWS service architecture, Amazon EC2 instance deployment options and Amazon VPC configuration.

It is also recommended to understand the best practices for implementing services in the most secure manner and best practices for creating users, groups, and roles using AWS IAM. Which services can use multi-factor authentication is also required knowledge and you should understand the available AWS Directory Services at a high-level and when to use them.

Questions often come up asking you to identify which technologies include DDoS mitigation and these include AWS Auto Scaling, Amazon CloudFront, and Amazon Route 53.

You should also know how to implement monitoring and logging using Amazon CloudWatch and AWS CloudTrail, when and what penetration testing you are allowed to perform within the AWS cloud and what compliance programs AWS comply with.

Technologies you need to know for domain 3 include Amazon VPC, AWS KMS, AWS CloudHSM, AWS IAM, Amazon Cognito, and AWS Directory Services.

**Example Questions**

**Question:** The development team at your company have created a new mobile application that will be used by users to access confidential data. The developers have used Amazon Cognito for authentication, authorization, and user management. Due to the sensitivity of the data, there is a requirement to add another method of authentication in addition to a username and password.

You have been asked to recommend the best solution. What is your recommendation?

1. Integrate IAM with a user pool in Cognito
2. Enable multi-factor authentication (MFA) in IAM
3. Integrate a third-party identity provider (IdP)
4. Use multi-factor authentication (MFA) with a Cognito user pool

**Answer:** 4, You can use MFA with a Cognito user pool (not in IAM) and this satisfies the requirement. A user pool is a user directory in Amazon Cognito. With a user pool, your users can sign-in to your web or mobile app through Amazon Cognito. Your users can also sign-in through social identity providers like Facebook or Amazon, and through SAML identity providers.

**Question:** You have been asked to come up with a solution for providing single sign-on to existing staff in your company who manage on-premise web applications and now need access to the AWS management console to manage resources in the AWS cloud.

Which product combinations provide the best solution to achieve this requirement?

1. Use your on-premise LDAP directory with IAM
2. Use IAM and MFA
3. Use the AWS Secure Token Service (STS) and SAML
4. Use IAM and Amazon Cognito

**Answer:** 3, Single sign-on using federation allows users to log-in to the AWS console without assigning IAM credentials. The AWS Security Token Service (STS) is a web service that enables you to request temporary, limited-privilege credentials for IAM users or for users that you authenticate (such as federated users from an on-premise directory). Federation (typically Active Directory) uses SAML 2.0 for authentication and grants temporary access based on the users’ AD credentials. The user does not need to be a user in IAM.

**Test Domain 4: Design Cost-Optimized Architectures**

This domain makes up 18% of the exam and includes the following objectives:

4.1 Identify cost-effective storage solutions.

4.2 Identify cost-effective compute and database service.

4.3 Design cost-optimized network architectures.

**What you need to know**

A relatively small but still important area of the exam requires architects to consider cost- effectiveness when deploying application on AWS. You need to understand the various cost models of compute and storage services, what you pay for and what the best choices would be given a specific scenario.

**Example Questions**

**Question:** You need to run a production batch process quickly that will use several EC2 instances. The process cannot be interrupted and must be completed within a short time period.

What is likely to be the MOST cost-effective choice of EC2 instance type to use for this requirement?

1. Reserved instances
2. Spot instances
3. On-demand instances
4. Flexible instances

**Answer:** 3, the key requirements here are that you need to deploy several EC2 instances quickly to run the batch process and you must ensure that the job completes. The on-demand pricing model is the best for this ad-hoc requirement. Though spot pricing may be cheaper, you cannot afford to risk that the instances are terminated by AWS when the market price increases.

**Question:** An Architect is designing a serverless application that will accept images uploaded by users from around the world. The application will make API calls to back-end services and save the session state data of the user to a database.

Which combination of services would provide a solution that is cost-effective while delivering the least latency?

1. Amazon CloudFront, API Gateway, Amazon S3, AWS Lambda, DynamoDB
2. API Gateway, Amazon S3, AWS Lambda, DynamoDB
3. Amazon CloudFront, API Gateway, Amazon S3, AWS Lambda, Amazon RDS
4. Amazon S3, API Gateway, AWS Lambda, Amazon RDS

**Answer:** 1, Amazon CloudFront caches content closer to users at Edge locations around the world. This is the lowest latency option for uploading content. API Gateway and AWS Lambda are present in all options. DynamoDB can be used for storing session state data

## CONCLUSION

We trust that these training notes have helped you to gain a complete understanding of the facts you need to know to pass the AWS Certified Solutions Architect Associate exam first time.

The exam covers a broad set of technologies. It’s vital to ensure you are armed with the knowledge to answer whatever questions come up in your certification exam. We recommend reviewing these training notes until you’re confident in all areas.

### Before taking the AWS Exam

**Get Hands-On experience with AWS**

AWS certification exams such as the Solutions Architect Associate test your hands-on knowledge and experience with the AWS platform. It's therefore super important to have some practical experience before you sit the exam.

Our AWS Certified Solutions Architect Associate Hands-On Labs course provides a practical approach to learning. Through over 28 hours of on demand video training you will learn how to architect and build solutions on Amazon Web Services. By the end of the course, you will have developed a strong experience-based skillset. This is the best way to gain hands-on skills and will give you an edge on the day of your exam. To learn more, visit https://digitalcloud.training/aws-
certified-solutions-architect-associate-hands-on-course-saa-c02/.

**Assess your exam readiness with Practice Exams**

The Digital Cloud Training practice questions are the closest to the actual exam and the only exam- difficulty questions on the market. If you can pass these mock exams, you’re well set to ace the real thing. To learn more, visit https://digitalcloud.training/aws-certified-solutions-architect-associate-
practice-tests-saa-c02.

### Reach out and Connect

The AWS platform is evolving quickly, and the exam tracks these changes with a typical lag of around 6 months. We are therefore reliant on student feedback to keep track of what is appearing in the exam. If there are any topics in your exam that weren't covered in our training resources, please provide us with feedback using this form https://digitalcloud.training/student-feedback. We appreciate your feedback that will help us further improve our AWS training resources.

To discuss any exam-specific questions you may have, please join the discussion on Slack. Visit
[http://digitalcloud.training/slack](http://digitalcloud.training/slack) for instructions.

Also, remember to join our private Facebook group to ask questions and share your knowledge with the AWS community: https://www.facebook.com/groups/awscertificationqa

```
Best wishes for your AWS certification journey!
```

## OTHER BOOKS & COURSES BY NEAL DAVIS

All of our courses are available on digitalcloud.training/aws-training-courses

### Courses for the AWS Certified Cloud Practitioner

```
Course Description
```

```
AWS Certified
Cloud Practitioner
Instructor-led Video
Course
```

```
HIGHLY FLEXIBLE COURSE STRUCTURE: You can move quickly through the
course, focusing on the theory lectures.
GUIDED HANDS-ON EXERCISES: To gain more practical experience with
AWS services, you have the option to explore the guided hands-on
exercises.
EXAM-CRAM LECTURES : Get through the key exam facts in the shortest
time possible with the exam-cram lectures that you’ll find at the end of
each section.
HIGH-QUALITY VISUALS : We've spared no effort to create a highly visual
training course with lots of table and graphs.
```

```
AWS Certified
Cloud Practitioner
(online) Practice
Exams + Exam
Simulator
```

```
Get access to the Practice Exam course from Digital Cloud Training: 6 sets
of practice tests with 65 Questions each. All questions are unique, 100%
scenario-based and conform to the latest CLF-C01 exam blueprint. Our
AWS Practice Tests are delivered in 4 different modes:
```

- Exam Mode
- Training Mode
- Knowledge Reviews
- Final Exam Simulator (with 500 practice questions)

```
AWS Certified
Cloud Practitioner
(offline) Practice
Tests (ebook)
```

```
There are 6 practice exams with 65 questions each covering the five
domains of the AWS CLF-C01 exam blueprint. Each set of questions is
repeated once without answers and explanations, and once with answers
and explanations, so you get to choose from two methods of preparation:
1: To simulate the exam experience and assess your exam readiness, use
the “ PRACTICE QUESTIONS ONLY ” sets.
2: To use the practice questions as a learning tool, use the “ PRACTICE
QUESTIONS, ANSWERS & EXPLANATIONS ” sets to view the answers and
read the in-depth explanations as you move through the questions.
```

```
Training Notes for
the AWS Certified
```

```
This book is based on the CLF-C01 exam blueprint and provides a deep
dive into the subject matter in a concise and easy-to-read format so you
```

```
Cloud Practitioner
(ebook)
```

```
can fast-track your time to success. AWS Solutions Architect, Neal Davis,
has consolidated the information you need to be successful.
```

### Courses for the AWS Certified Solutions Architect Associate

```
Course Description
```

```
AWS Certified
Solutions Architect
Associate
Instructor-led Video
Course
```

```
This popular AWS Certified Solutions Architect Associate (SAA-C02) video
course is delivered through guided Hands-On Labs exercises
```

- 28 hours Video Lessons
- Exam Cram Lectures
- 90 Quiz Questions
- High-Quality Visuals
- Guided Hands-on Exercises
- Build Applications on AWS

```
AWS Certified
Solutions Architect
Associate (online)
Practice Tests
```

```
Get access to the Practice Exam course from Digital Cloud Training: 6 sets
of practice tests with 65 Questions each. All questions are unique, 100%
scenario-based and conform to the latest AWS SAA-C02 exam blueprint.
Our AWS Practice Tests are delivered in 4 different modes:
```

- Exam Mode
- Training Mode
- Knowledge Reviews
- Final Exam Simulator (with 500 practice questions)

```
AWS Certified
Solutions Architect
Associate (offline)
Practice Tests
(ebook)
```

```
There are 6 practice exams with 65 questions each covering the AWS
SAA-C02 exam blueprint. Each set of questions is repeated once without
answers and explanations, and once with answers and explanations.
1: To simulate the exam experience and assess your exam readiness, use
the “ PRACTICE QUESTIONS ONLY ” sets.
2: To use the practice questions as a learning tool, use the “ PRACTICE
QUESTIONS, ANSWERS & EXPLANATIONS ” sets to view the answers and
read the in-depth explanations as you move through the questions.
```

```
Training Notes for
the AWS Certified
Solutions Architect
Associate (ebook)
```

```
Deep dive into the SAA-C02 exam objectives with 300 pages of detailed
facts, tables and diagrams. Save valuable time by getting straight to the
facts you need to know to pass your AWS Certified Solutions Architect
Associate exam first time!
```

```
This book is based on the 2020 SAA-C02 exam blueprint and provides a
deep dive into the subject matter in a concise and easy-to-read format so
```

```
you can fast-track your time to success.
```

### Courses for the AWS Certified Developer Associate

```
Course Description
```

```
AWS
Certified
Developer
Associate
Instructor
led Video
Course
```

```
This popular AWS Certified Developer Associate Exam Training for the DVA-C01
certification exam is packed with over 28 hours of comprehensive video lessons,
hands-on labs, quizzes and exam-crams. With our mixture of in-depth theory,
architectural diagrams and hands-on training, you'll learn how to architect and
build applications on Amazon Web Services , fully preparing you for the AWS
Developer Certification exam. With this complete AWS Developer training
course, you have everything you need to comfortably pass the AWS Developer
Certification exam at the first attempt.
```

```
AWS
Certified
Developer
Associate
(online)
Practice
Tests
```

```
Get access to the Practice Exam Course from Digital Cloud Training with 390
Questions in 6 sets of practice tests. All questions are unique and conform to the
latest AWS DVA-C01 exam blueprint.
Our AWS Practice Tests are delivered in 4 different modes:
```

- Exam Mode
- Training Mode
- Knowledge Reviews
- Final Exam Simulator

```
AWS
Certified
Developer
Associate
(offline)
Practice
Tests
(ebook)
```

```
There are 6 practice exams with 65 questions each covering all topics for the AWS
DVA-C01 exam. Each set of questions is repeated once without answers and
explanations, and once with answers and explanations, so you get to choose from
two methods of preparation:
1: To simulate the exam experience and assess your exam readiness, use the
“ PRACTICE QUESTIONS ONLY ” sets.
2: To use the practice questions as a learning tool, use the “ PRACTICE QUESTIONS,
ANSWERS & EXPLANATIONS ” sets to view the answers and read the in-depth
explanations as you move through the questions.
```

```
Training
Notes for
the AWS
Certified
Developer
Associate
(ebook)
```

```
With these in-depth AWS Training Notes for the Developer Associate, you'll learn
everything you need to know to ace your exam! Fast-track your exam success with
over 340 pages of exam-specific facts, tables and diagrams.
```

```
AWS Solution Architect and founder of Digital Cloud Training, Neal Davis, has
consolidated ALL of the key information into this essential cheat sheet. Based on
the latest DVA-C01 certification exam, these Training Notes will shortcut your
study time and maximize your chance of passing your exam first time.
```

### Courses for the AWS Certified SysOps Administrator Associate

```
Course Description
```

```
AWS Certified SysOps
Administrator Associate
Instructor led Video
Course
```

```
This popular AWS Certified SysOps Administrator Exam Training for
the SOA-C01 certification exam is packed with 15 hours of
comprehensive video lessons, exam scenarios and practical
exercises. With our mixture of in-depth theory, logical diagrams and
hands-on training, you'll learn how deploy, manage, and operate
scalable, highly available, and fault tolerant systems on AWS, fully
preparing you for the AWS SysOps Certification exam. With this
complete AWS SysOps training course, you have everything you
need to comfortably pass the AWS SysOps Certification exam at the
first attempt.
```

```
AWS Certified SysOps
Administrator Associate
(online) Practice Tests
```

```
Get access to the Practice Exam Course from Digital Cloud Training
with 195 Questions in 3 sets of practice tests. All questions are
unique and conform to the latest AWS SOA-C01 exam blueprint.
Our AWS Practice Tests are delivered in 4 different modes:
```

- Exam Mode
- Training Mode
- Knowledge Reviews
- Final Exam Simulator

```
Training Notes for the
AWS Certified SysOps
Administrator Associate
(cheat sheets)
```

```
With these in-depth AWS Training Notes for the SysOps
Administrator, you'll learn everything you need to know to ace your
exam! Fast-track your exam success with exam-specific facts, tables
and diagrams.
Founder of Digital Cloud Training, Neal Davis, has consolidated ALL of
the key information into this essential cheat sheet. Based on the
latest SOA-C01 certification exam, these Training Notes will shortcut
your study time and maximize your chance of passing your exam first
time.
```

## ABOUT THE AUTHOR

**Neal Davis** is the founder of Digital Cloud Training, AWS Cloud Solutions Architect and successful IT
:qinstructor. With more than 20 years of experience in the tech industry, Neal is a true expert in virtualization and cloud computing. His passion is to help others achieve career success by offering in-depth AWS certification training resources.

Neal started **Digital Cloud Training** to provide a variety of training resources for Amazon Web Services (AWS) certifications that represent a higher standard of quality than is otherwise available in the market.

Digital Cloud Training provides **AWS Certification exam preparation resources** including instructor- led Video Courses, guided Hands-on Labs, in-depth Training Notes, Exam-Cram lessons for quick revision, Quizzes to test your knowledge and exam-difficulty Practice Exams to assess your exam readiness.

With Digital Cloud Training, you get access to highly experienced staff who support you on your AWS Certification journey and help you elevate your career through achieving highly valuable certifications. Join the AWS Community of over 2 50,000 happy students that are currently enrolled in Digital Cloud Training courses.

**CONNECT WITH NEAL ON SOCIAL MEDIA**

All Links available on https://digitalcloud.training/neal-davis

```
digitalcloud.training/neal-davis
```

```
https://www.youtube.com/c/digitalcloudtraining
```

```
facebook.com/digitalclou
dtraining
```

(^)
Twitter @nealkdavis linkedin.com/in/nealkdavi s Instagram @digitalcloudtraining
(^)