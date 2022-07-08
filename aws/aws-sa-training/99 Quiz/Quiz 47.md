## Quiz 47: A recent security audit uncovered some poor deployment and configuration practices within your VPC. You need to ensure that applications are deployed in secure configurations.**

**How can this be achieved in the most operationally efficient manner?**

- [ ] Remove the ability for staff to deploy applications

- [x] Use CloudFormation with securely configured templates

- [ ] Manually check all application configurations before deployment

- [ ] Use AWS Inspector to apply secure configurations

----
Answer: 2
**Explanation:**
CloudFormation helps users to deploy resources in a consistent and orderly way. By ensuring the CloudFormation templates are created and administered with the right security configurations for your resources, you can then repeatedly deploy resources with secure settings and reduce the risk of human error.

- ✅: "Use CloudFormation with securely configured templates" is the correct answer.

- ❌: "Remove the ability for staff to deploy applications" is incorrect. Removing the ability of staff to deploy resources does not help you to deploy applications securely as it does not solve the problem of how to do this in an operationally efficient manner.

- ❌: "Manually check all application configurations before deployment" is incorrect. Manual checking of all application configurations before deployment is not operationally efficient.

- ❌: "Use AWS Inspector to apply secure configurations" is incorrect. Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications **_deployed_** on AWS. It is not used to secure the actual deployment of resources, only to assess the deployed state of the resources.
  **References:**
  https://aws.amazon.com/cloudformation/resources/templates/
