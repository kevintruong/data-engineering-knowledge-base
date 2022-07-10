#### Question  18

**A solutions architect is designing a two-tier web application. The application consists of a public-facing web tier

hosted on Amazon EC2 in public subnets. The database tier consists of Microsoft SQL Server running on Amazon EC2 in a

private subnet. Security is a high priority for the company.**

**How should security groups be configured in this situation? (Select TWO)**

- [x] :  Configure the security group for the web tier to allow inbound traffic on port 443 from 0.0.0.0/0

- [ ] :  Configure the security group for the web tier to allow outbound traffic on port 443 from 0.0.0.0/0

- [x] :  Configure the security group for the database tier to allow inbound traffic on port 1433 from the security group for

the web tier

- [ ] :  Configure the security group for the database tier to allow outbound traffic on ports 443 and 1433 to the security

group for the web tier

- [ ] :  Configure the security group for the database tier to allow inbound traffic on ports 443 and 1433 from the security

group for the web tier

----

- #security_groups #security_group #web_tier #tier_web_application #database_tier
- hasExplain:: [[explanation_Question  18.md]]
