#### Question  13

**A company has launched a multi-tier application architecture. The web tier and database tier run on Amazon EC2

instances in private subnets within the same Availability Zone.**

**Which combination of steps should a Solutions Architect take to add high availability to this architecture?

(Select TWO)**

- [ ] Create new public subnets in the same AZ for high availability and move the web tier to the public subnets

- [x] Create an Amazon EC2 Auto Scaling group and Application Load Balancer (ALB) spanning multiple AZs

- [ ] Add the existing web application instances to an Auto Scaling group behind an Application Load Balancer

(ALB)

- [ ] Create new private subnets in the same VPC but in a different AZ. Create a database using Amazon EC2 in one AZ

- [x] Create new private subnets in the same VPC but in a different AZ. Migrate the database to an Amazon RDS multi-AZ

deployment

- hasExplain:: [[explanation_Question  13.md]]
