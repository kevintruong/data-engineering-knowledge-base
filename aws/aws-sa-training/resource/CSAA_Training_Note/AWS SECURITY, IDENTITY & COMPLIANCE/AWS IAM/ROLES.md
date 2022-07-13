#### ROLES


Roles are created and then “assumed” by trusted entities and define a set of permissions for making AWS service

requests.


With IAM Roles you can delegate permissions to resources for users and services without using permanent credentials (

e.g. user name and password).


IAM users or AWS services can assume a role to obtain temporary security credentials that can be used to make AWS API

calls.


You can delegate using roles.


There are no credentials associated with a role (password or access keys).


IAM users can temporarily assume a role to take on permissions for a specific task.


A role can be assigned to a federated user who signs in using an external identity provider.


Temporary credentials are primarily used with IAM roles and automatically expire.


Roles can be assumed temporarily through the console or programmatically with the **AWS CLI** ,

**Tools for Windows PowerShell** or **API.**


**IAM roles with EC2 instances:**


- IAM roles can be used for granting applications running on EC2 instances permissions to AWS API requests using

  instance profiles.

- Only one role can be assigned to an EC2 instance at a time.

- A role can be assigned at the **EC2 instance creation time or at any time afterwards**.

- When using the AWS CLI or API instance profiles must be created manually (it’s automatic and transparent through the

  console).

- Applications retrieve temporary security credentials from the instance metadata.


**Role Delegation:**


- Create an IAM role with two policies:

  o Permissions policy – grants the user of the role the required permissions on a resource. o Trust policy – specifies

  the trusted accounts that are allowed to assume the role.

- Wildcards (*) cannot be specified as a principal.

- A permissions policy must also be attached to the user in the trusted account.

