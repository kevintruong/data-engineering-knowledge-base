#### IAM USERS

An IAM user is an entity that represents a person or service.

**Can be assigned:**

- An access key ID and secret access key for programmatic access to the AWS API,
  CLI, SDK, and other development tools.

- A password for access to the management console.

By default, users cannot access anything in your account.

The account root user credentials are the email address used to create the
account and a password.

The root account has full administrative permissions, and these cannot be
restricted.

**Best practice for root accounts:**

- Don’t use the root user credentials.

- Don’t share the root user credentials.

- Create an IAM user and assign administrative permissions as required.

- Enable MFA.

IAM users can be created to represent applications and these are known as
“service accounts”.

You can have up to 5000 users per AWS account.

Each user account has a friendly name and an ARN which uniquely identifies the
user across AWS.

A unique ID is also created which is returned only when you create the user
using the API, Tools for Windows PowerShell

or the AWS CLI.

You should create individual IAM accounts for users (best practice not to share
accounts).

The Access Key ID and Secret Access Key are not the same as a password and
cannot be used to login to the AWS console.

The Access Key ID and Secret Access Key can only be generated once and must be
regenerated if lost.

A password policy can be defined for enforcing password length, complexity
etc. (applies to all users).

You can allow or disallow the ability to change passwords using an IAM policy.

Access keys and passwords should be changed regularly.

