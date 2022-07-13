#### PRE-DEFINED GROUPS


**Authenticated Users group:**


- This group represents all AWS accounts.

- Access permission to this group allows any AWS account access to the resource.

- All requests must be signed (authenticated).

- Any authenticated user can access the resource.


**All Users group:**


- Access permission to this group allows anyone in the world access to the resource.

- The requests can be signed (authenticated) or unsigned (anonymous).

- Unsigned requests omit the authentication header in the request.

- AWS recommends that you never grant the All Users group WRITE, WRITE_ACP, or FULL_CONTROL permissions.


**Log Delivery group:**


- Providing WRITE permission to this group on a bucket enables S3 to write server access logs.

- Not applicable to objects.


**The following table lists the set of permissions that Amazon S3 supports in an ACL:**


- The set of ACL permissions is the same for an object ACL and a bucket ACL.



- Depending on the context (bucket ACL or object ACL), these ACL permissions grant permissions for specific buckets or

  object operations.

- The table lists the permissions and describes what they mean in the context of objects and buckets.


**Note the following:**


- Permissions are assigned at the account level for authenticated users.

- You cannot assign permissions to individual IAM users.

- When Read is granted on a bucket it only provides the ability to list the objects in the bucket.

- When Read is granted on an object the data can be read.

- ACP means access control permissions and READ_ACP/WRITE_ACP control who can read/write the ACLs themselves.

- WRITE is only applicable to the bucket level (except for ACP).


Bucket policies are limited to 20 KB in size.


Object ACLs are limited to 100 granted permissions per ACL.


The only recommended use case for the bucket ACL is to grant write permissions to the S3 Log Delivery group.


**There are limits to managing permissions using ACLs:**


- You cannot grant permissions to individual users.

- You cannot grant conditional permissions.

- You cannot explicitly deny access.


When granting other AWS accounts the permissions to upload objects, permissions to these objects can only be managed by

the object owner using object ACLs.


**You can use bucket policies for:**


- Granting users permissions to a bucket owned by your account.

- Managing object permissions (where the object owner is the same account as the bucket owner).

- Managing cross-account permissions for all Amazon S3 permissions.


**You can use user policies for:**


- Granting permissions for all Amazon S3 operations.

- Managing permissions for users in your account.

- Granting object permissions to users within the account.


**For an IAM user to access resources in another account the following must be provided:**


- Permission from the parent account through a user policy.

- Permission from the resource owner to the IAM user through a bucket policy, or the parent account through a bucket

  policy, bucket ACL or object ACL.


If an AWS account owns a resource it can grant permissions to another account, that account can then delegate those

permissions or a subset of them to uses in the account (permissions delegation).


An account that receives permissions from another account cannot delegate permissions cross- account to a third AWS

account.

