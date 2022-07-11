*

**Explanation:**

AWS best practice is to deploy databases into private subnets wherever possible. You can then deploy your web front-ends

into public subnets and configure these, or an additional application tier to write data to the database.

* ✅ :  "The private subnet" is the correct answer.

* ❌ :  "It doesn’t matter" is incorrect as the best practice does recommend using a private subnet.

* ❌ :  "The public subnet" is incorrect. Public subnets are typically used for web front-ends as they are directly

  accessible from the Internet. It is preferable to launch your database in a private subnet.

* ❌ :  "The subnet that is mapped to the primary AZ in the region" is incorrect. There is no such thing as a

  “primary” Availability Zone (AZ). All AZs are essentially created equal and your subnets map 1:1 to a single AZ.

**References:**

<https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>-

delivery/amazon-vpc/

----
* #aws #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content>>- #availability_zone #private_subnet #private_subnets
