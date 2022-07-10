#### Question  21

**A web application runs in public and private subnets. The application architecture consists of a web tier and database

tier running on Amazon EC2 instances. Both tiers run in a single Availability Zone (AZ).**

**Which combination of steps should a solutions architect take to provide high availability for this architecture? (

Select TWO)**

- [ ] Create new public and private subnets in the same AZ for high availability

- [x] Create an Amazon EC2 Auto Scaling group and Application Load Balancer (ALB) spanning multiple AZs

- [ ] Add the existing web application instances to an Auto Scaling group behind an Application Load Balancer

(ALB)

- [ ] Create new public and private subnets in a new AZ. Create a database using Amazon EC2 in one AZ

- [x] Create new public and private subnets in the same VPC, each in a new AZ. Migrate the database to an Amazon RDS

multi-AZ deployment

- hasExplain:: [[explanation_Question  21.md]]

# high_availability #single_availability_zone #amazon_ec2_auto_scaling_group #multiple_azs #application_load_balancer
