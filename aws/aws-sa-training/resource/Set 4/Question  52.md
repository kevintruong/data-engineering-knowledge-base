#### Question  52


**A Solutions Architect is designing a new retail website for a high-profile company. The company has previously been

the victim of targeted distributed denial-of-service (DDoS) attacks and has requested that the design includes

mitigation techniques.**


**Which of the following are the BEST techniques to help ensure the availability of the services is not compromised in

an attack? (Select TWO)**


1: Configure Auto Scaling with a high maximum number of instances to ensure it can scale accordingly


2: Use CloudFront for distributing both static and dynamic content


3: Use Spot instances to reduce the cost impact in case of attack


4: Use encryption on your EBS volumes


5: Use Placement Groups to ensure high bandwidth and low latency


**Answer: 1,2**


**Explanation:**


CloudFront distributes traffic across multiple edge locations and filters requests to ensure that only valid HTTP(S)

requests will be forwarded to backend hosts. CloudFront also supports geoblocking, which you can use to prevent requests

from particular geographic locations from being served.


Auto Scaling helps to maintain a desired count of EC2 instances running at all times and setting a high maximum number

of instances allows your fleet to grow and absorb some of the impact of the attack.


- CORRECT "Configure Auto Scaling with a high maximum number of instances to ensure it can scale accordingly" is a

  correct answer.


- CORRECT "Use CloudFront for distributing both static and dynamic content" is also a correct answer.


- INCORRECT "Use Spot instances to reduce the cost impact in case of attack" is incorrect. Spot instances may reduce the

  cost (depending on the current Spot price) however the questions asks us to focus on availability not cost.


- INCORRECT "Use encryption on your EBS volumes" is incorrect. Encrypting EBS volumes does not help in a DDoS attack as

  the attack is targeted at reducing availability rather than compromising data.


- INCORRECT "Use Placement Groups to ensure high bandwidth and low latency" is incorrect as this will not assist with

  mitigation of DDoS attacks.


**References:**


https://aws.amazon.com/answers/networking/aws-ddos-attack-mitigation/


https://docs.aws.amazon.com/waf/latest/developerguide/tutorials-ddos-cross-service.html


https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-

delivery/amazon-cloudfront/

