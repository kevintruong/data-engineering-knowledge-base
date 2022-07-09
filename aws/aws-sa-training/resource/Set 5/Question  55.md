#### Question  55


**A Solutions Architect is creating a multi-tier application that includes loosely-coupled, distributed application

components and needs to determine a method of sending notifications instantaneously. Using Amazon SNS which transport

protocols are supported? (Select TWO)**


1: Amazon SWF


2: FTP


3: HTTPS


4: AWS Lambda


5: Email-JSON


**Answer: 3,5**


**Explanation:**


Note that the questions asks you which transport protocols are supported, NOT which subscribers – therefore AWS Lambda

is not supported.


Amazon SNS supports notifications over multiple transport protocols:


- HTTP/HTTPS – subscribers specify a URL as part of the subscription registration.

- Email/Email-JSON – messages are sent to registered addresses as email (text-based or JSON-object).

- SQS – users can specify an SQS standard queue as the endpoint.

- SMS – messages are sent to registered phone numbers as SMS text messages.


- CORRECT "HTTPS" is the correct answer.


- CORRECT "Email-JSON" is the correct answer.


- INCORRECT "Amazon SWF" is incorrect as this is not a supported transport protocol.


- INCORRECT "FTP" is incorrect as this is not a supported transport protocol.


- INCORRECT "AWS Lambda" is incorrect as this is not a supported transport protocol.


**References:**


https://aws.amazon.com/sns/faqs/


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-

integration/amazon-sns/

