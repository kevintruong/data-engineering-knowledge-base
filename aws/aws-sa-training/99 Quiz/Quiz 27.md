## Quiz 27: Amazon EC2 instances in a development environment run between 9am and 5pm Monday-Friday. Production instances run 24/7. Which pricing models should be used? (Select TWO)**

- [ ] Use Spot instances for the development environment

- [ ] Use Reserved instances for the development environment

- [x] Use scheduled reserved instances for the development environment

- [x] Use Reserved instances for the production environment

- [ ] Use On-Demand instances for the production environment

----
Answer: 3,4

- [x] Use scheduled reserved instances for the development environment

- [x] Use Reserved instances for the production environment
  **Explanation:**
  Scheduled Instances are a good choice for workloads that do not run continuously but do run on a regular schedule. This is ideal for the development environment. Reserved instances are a good choice for workloads that run continuously. This is a good option for the production environment**.**
- ✅: "Use scheduled reserved instances for the development environment" is a correct answer.

- ✅: "Use Reserved instances for the production environment" is also a correct answer.

- ❌: "Use Spot instances for the development environment" is incorrect. Spot Instances are a cost- effective choice if you can be flexible about when your applications run and if your applications can be interrupted. Spot instances are not suitable for the development environment as important work may be interrupted.

- ❌: "Use Reserved instances for the development environment" is incorrect as they should be used for the production environment.

- ❌: "Use On-Demand instances for the production environment" is incorrect. There is no long-term commitment required when you purchase On-Demand Instances. However, you do not get any discount and therefore this is the most expensive option.
  **References:**
  https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-purchasing-options.html



----
#quiz 
- relateTo:: [[Domain 4 Design Cost-Optimized Architectures]]