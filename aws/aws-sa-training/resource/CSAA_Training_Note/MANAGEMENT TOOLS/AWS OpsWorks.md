### AWS OpsWorks


AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet two very popular

automation platforms.


Automates how applications are configured, deployed and managed.


Provide configuration management to deploy code, automate tasks, configure instances, perform upgrades etc.


OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon

EC2 instances or on-premises compute environments.


OpsWorks is an automation platform that transforms infrastructure into code.


**OpsWorks consists of Stacks and Layers:**


- Stack are collections of resources needed to support a service or application.

- Stacks are containers of resources (EC2, RDS etc.) that you want to manage collectively.

- Every Stack contains one or more Layers and Layers automate the deployment of packages.

- Stacks can be cloned – but only within the same region.

- Layers represent different components of the application delivery hierarchy.

- EC2 instances, RDS instances, and ELBS are examples of Layers.


OpsWorks is a global service. But when you create a stack, you must specify a region and that stack can only control

resources in that region.


There are three offerings: OpsWorks for Chef Automate, OpsWorks for Puppet Enterprise, and OpsWorks Stacks.


**AWS OpsWorks for Chef Automate**


- A fully-managed configuration management service that hosts Chef Automate, a suite of automation tools from Chef for

  configuration management, compliance and security, and continuous deployment.

- Completely compatible with tooling and cookbooks from the Chef community and automatically registers new nodes with

  your Chef server.

- Chef server stores recipes and configuration data.

- Chef client (node) is installed on each server.


**AWS OpsWorks for Puppet Enterprise**


- A fully-managed configuration management service that hosts Puppet Enterprise, a set of automation tools from Puppet

  for infrastructure and application management.


**AWS OpsWorks Stacks**


- An application and server management service that allows you to model your application as a stack containing different

  layers, such as load balancing, database, and application server.

- OpsWorks Stacks is an AWS creation and uses and embedded Chef Solo client installed on EC2 instances to run Chef

  recipes.


OpsWorks Stacks supports EC2 instances and on-premise servers as well as an agent.

