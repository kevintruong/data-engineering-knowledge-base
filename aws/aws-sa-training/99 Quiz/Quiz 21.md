## Quiz 21: A web application runs in public and private subnets. The application architecture consists of a web tier and database tier running on Amazon EC2 instances. Both tiers run in a single Availability Zone (AZ).**

**Which combination of steps should a solutions architect take to provide high availability for this architecture? (

**Select TWO)**

- [ ] Create new public and private subnets in the same AZ for high availability
- [ ] Create an Amazon EC2 Auto Scaling group and Application Load Balancer (ALB) spanning multiple AZs
- [ ] Add the existing web application instances to an Auto Scaling group behind an Application Load Balancer

  (ALB)
- [ ] Create new public and private subnets in a new AZ. Create a database using Amazon EC2 in one AZ
- [ ] Create new public and private subnets in the same VPC, each in a new AZ. Migrate the database to an Amazon RDS multi-AZ deployment

----
Answer: 2, 5
**Explanation:**
To add high availability to this architecture both the web tier and database tier require changes. For the web tier an Auto Scaling group across multiple AZs with an ALB will ensure there are always instances running and traffic is being distributed to them. The database tier should be migrated from the EC2 instances to Amazon RDS to take advantage of a managed database with Multi-AZ functionality. This will ensure that if there is an issue preventing access to the primary database a secondary database can take over.

- ✅: "Create an Amazon EC2 Auto Scaling group and Application Load Balancer (ALB) spanning multiple AZs" is the correct answer.
- ✅: "Create new public and private subnets in the same VPC, each in a new AZ. Migrate the database to an Amazon RDS multi-AZ deployment" is the correct answer.
- ❌: "Create new public and private subnets in the same AZ for high availability" is incorrect as this would not add high availability.
- ❌: "Add the existing web application instances to an Auto Scaling group behind an Application Load Balancer (ALB)" is incorrect because the existing servers are in a single subnet. For HA we need to instances in multiple subnets.
- ❌: "Create new public and private subnets in a new AZ. Create a database using Amazon EC2 in one AZ" is incorrect because we also need HA for the database layer.
  **References:**
  https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html
  https://aws.amazon.com/rds/features/multi-az/

----
#quiz 
- relateTo:: [[Domain 1 Design Resilient Architectures]]