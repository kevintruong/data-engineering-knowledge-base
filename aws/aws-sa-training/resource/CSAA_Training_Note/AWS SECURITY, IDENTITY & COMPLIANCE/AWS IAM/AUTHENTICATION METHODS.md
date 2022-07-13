#### AUTHENTICATION METHODS

**Console password:**

- A password that the user can enter to sign into interactive sessions such as
  the AWS Management Console.

- You can allow users to change their own passwords.

- You can allow selected IAM users to change their passwords by disabling the
  option for all

```

users and using an IAM policy to grant permissions for the selected users.

```

**Access Keys:**

- A combination of an access key ID and a secret access key.

- You can assign two active access keys to a user at a time.

- These can be used to make programmatic calls to AWS when using the **API** in
  program code or at a command prompt when

  using the **AWS CLI** or the **AWS PowerShell** tools.

- You can create, modify, view or rotate access keys.

- When created IAM returns the access key ID and secret access key.

- The secret access is returned only at creation time and if lost a new key must
  be created.

- Ensure access keys and secret access keys are stored securely.

- Users can be given access to change their own keys through IAM policy (not
  from the console).

- You can disable a user’s access key which prevents it from being used for API
  calls.

**Server certificates:**

- SSL/TLS certificates that you can use to authenticate with some AWS services.

- AWS recommends that you use the AWS Certificate Manager (ACM) to provision,
  manage and deploy your server

  certificates.

- Use IAM only when you must support HTTPS connections in a region that is not
  supported by ACM.

The following diagram shows the different methods of authentication available
with IAM:

