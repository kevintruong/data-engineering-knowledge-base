### AWS Systems Manager

AWS Systems Manager allows you to centralize operational data from multiple AWS
services and automate tasks across your

AWS resources.

You can create logical groups of resources such as applications, different
layers of an application stack, or production

versus development environments.

With Systems Manager, you can select a resource group and view its recent API
activity, resource configuration changes,

related notifications, operational alerts, software inventory, and patch
compliance status.

You can also take action on each resource group depending on your operational
needs.

Systems Manager provides a central place to view and manage your AWS resources,
so you can have complete visibility and

control over your operations.

Centralized console and toolset for a wide variety of system management tasks.

Designed for managing a large fleet of systems – tens or hundreds.

SSM Agent enables System Manager features and supports all OSs supported by OS
as well as back to Windows Server 2003

and Raspbian.

SSM Agent installed by default on recent AWS-provided base AMIs for Linux and
Windows.

Manages AWS-based and on-premises based systems via the agent.

The AWS Systems Manager console integrates with AWS Resource Groups, and it
offers grouping capabilities in addition to

other native integrations.

**Systems Manager Inventory:**

- AWS Systems Manager collects information about your instances and the software
  installed on them, helping you to

  understand your system configurations and installed applications.

- You can collect data about applications, files, network configurations,
  Windows services, registries, server roles,

  updates, and any other system properties.

- The gathered data enables you to manage application assets, track licenses,
  monitor file integrity, discover

  applications not installed by a traditional installer, and more.

**Configuration Compliance:**

- AWS Systems Manager lets you scan your managed instances for patch compliance
  and configuration inconsistencies.

- You can collect and aggregate data from multiple AWS accounts and Regions, and
  then drill down into specific resources

  that aren’t compliant.

- By default, AWS Systems Manager displays data about patching and associations.
  You can also customize the service and

  create your own compliance types based on your requirements.

**Automation:**

- AWS Systems Manager allows you to safely automate common and repetitive IT
  operations and management tasks across AWS

  resources.

- With Systems Manager, you can create JSON documents that specify a specific
  list of tasks or use community published

  documents.

- These documents can be executed directly through the AWS Management Console,
  CLIs, and SDKs, scheduled in a

  maintenance window, or triggered based on changes to AWS resources through
  Amazon CloudWatch Events.

- You can track the execution of each step in the documents as well as require
  approvals for each step.

- You can also incrementally roll out changes and automatically halt when errors
  occur.

**Run Command:**

- Use Systems Manager Run Command to remotely and securely manage the
  configuration of your managed instances at scale.

  Use Run Command to perform on-demand changes like updating applications or
  running Linux shell scripts and Windows

  PowerShell commands on a target set of dozens or hundreds of instances.

**Session Manager:**

- AWS Systems Manager provides you safe, secure remote management of your
  instances at scale without logging into your

  servers, replacing the need for bastion hosts, SSH, or remote

```

PowerShell.

```

- It provides a simple way of automating common administrative tasks across
  groups of instances such as registry edits,

  user management, and software and patch installations.

- Through integration with AWS Identity and Access Management (IAM), you can
  apply granular permissions to control the

  actions users can perform on instances.

- All actions taken with Systems Manager are recorded by AWS CloudTrail,
  allowing you to audit changes throughout your

  environment.

**Patch Manager:**

- AWS Systems Manager helps you select and deploy operating system and software
  patches automatically across large

  groups of Amazon EC2 or on-premises instances.

- Through patch baselines, you can set rules to auto-approve select categories
  of patches to be installed, such as

  operating system or high severity patches, and you can specify a list of
  patches that override these rules and are

  automatically approved or rejected.

- You can also schedule maintenance windows for your patches so that they are
  only applied during preset times.

- Systems Manager helps ensure that your software is up-to-date and meets your
  compliance policies.

**Maintenance Windows:**

- AWS Systems Manager lets you schedule windows of time to run administrative
  and maintenance tasks across your

  instances.

- This ensures that you can select a convenient and safe time to install patches
  and updates or make other configuration

  changes, improving the availability and reliability of your services and
  applications.

**Distributor:**

- Distributor is an AWS Systems Manager feature that enables you to securely
  store and distribute software packages in

  your organization.

- You can use Distributor with existing Systems Manager features like Run
  Command and State Manager to control the

  lifecycle of the packages running on your instances.

**State Manager:**

- AWS Systems Manager provides configuration management, which helps you
  maintain consistent configuration of your

  Amazon EC2 or on-premises instances.

- With Systems Manager, you can control configuration details such as server
  configurations, anti-virus definitions,

  firewall settings, and more.

- You can define configuration policies for your servers through the AWS
  Management Console or use existing scripts,

  PowerShell modules, or Ansible playbooks directly from GitHub or Amazon S3
  buckets.

- Systems Manager automatically applies your configurations across your
  instances at a time and frequency that you

  define.

- You can query Systems Manager at any time to view the status of your instance
  configurations, giving you on-demand

  visibility into your compliance status.

**Parameter Store:**

- AWS Systems Manager provides a centralized store to manage your configuration
  data, whether plain-text data such as

  database strings or secrets such as passwords.

- This allows you to separate your secrets and configuration data from your
  code. Parameters can be tagged and organized

  into hierarchies, helping you manage parameters more easily.

- For example, you can use the same parameter name, “db-string”, with a
  different hierarchical path, “dev/db-string” or

  “prod/db-string”, to store different values.

- Systems Manager is integrated with AWS Key Management Service (KMS), allowing
  you to automatically encrypt the data

  you store.

- You can also control user and resource access to parameters using AWS Identity
  and Access Management (IAM). Parameters

  can be referenced through other AWS services, such as Amazon Elastic Container
  Service, AWS Lambda, and AWS

  CloudFormation.

