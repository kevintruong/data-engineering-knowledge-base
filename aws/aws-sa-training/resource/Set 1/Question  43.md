#### Question  43


**A Solutions Architect needs to improve performance for a web application running on EC2 instances launched by an Auto

Scaling group. The instances run behind an ELB Application Load Balancer. During heavy use periods the ASG doubles in

size and analysis has shown that static content stored on the EC2 instances is being requested by users in a specific

geographic location.**


**How can the Solutions Architect reduce the need to scale and improve the application performance?**


- [ ] Store the contents on Amazon EFS instead of the EC2 root volume


- [ ] Implement Amazon Redshift to create a repository of the content closer to the users


- [x] Create an Amazon CloudFront distribution for the site and redirect user traffic to the distribution


- [ ] Re-deploy the application in a new VPC that is closer to the users making the requests



- hasExplain:: [[explanation_Question  43.md]]

#cloudfront #ec2 #scaling #elb #efs 