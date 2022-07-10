#### Question  14


**A web application in a three-tier architecture runs on a fleet of Amazon EC2 instances. Performance issues have been

reported and investigations point to insufficient swap space. The operations team requires monitoring to determine if

this is correct.**


**What should a solutions architect recommend?**


- [ ] Configure an Amazon CloudWatch SwapUsage metric dimension. Monitor the SwapUsage dimension in the EC2 metrics in

CloudWatch


- [ ] Use EC2 metadata to collect information, then publish it to Amazon CloudWatch custom metrics. Monitor SwapUsage

metrics in CloudWatch


- [x] Install an Amazon CloudWatch agent on the instances. Run an appropriate script on a set schedule. Monitor

SwapUtilization metrics in CloudWatch


- [ ] Enable detailed monitoring in the EC2 console. Create an Amazon CloudWatch SwapUtilization custom metric. Monitor

SwapUtilization metrics in CloudWatch



- hasExplain:: [[explanation_Question  14.md]]

#cloudwatch #monitoring #swapusage #swap #ec2 