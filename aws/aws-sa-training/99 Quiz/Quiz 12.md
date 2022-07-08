## Quiz 12: A solutions architect is creating a document submission application for a school. The application will use an Amazon S3 bucket for storage. The solution must prevent accidental deletion of the documents and ensure that all versions of the documents are available. Users must be able to upload and modify the documents.**

**Which combination of actions should be taken to meet these requirements? (Select TWO)**

- [ ] Set read-only permissions on the bucket
- [ ] Enable versioning on the bucket
- [ ] Attach an IAM policy to the bucket
- [ ] Enable MFA Delete on the bucket
- [ ] Encrypt the bucket using AWS SSE-S3

----
Answer: 2, 4
**Explanation:**
None of the options present a good solution for specifying permissions required to write and modify objects so that requirement needs to be taken care of separately. The other requirements are to prevent accidental deletion and the ensure that all versions of the document are available. The two solutions for these requirements are versioning and MFA delete. Versioning will retain a copy of each version of the document and multi-factor authentication delete (MFA delete) will prevent any accidental deletion as you need to supply a second factor when attempting a delete.

- ✅: "Enable versioning on the bucket" is a correct answer.
- ✅: "Enable MFA Delete on the bucket" is also a correct answer.
- ❌: "Set read-only permissions on the bucket" is incorrect as this will also prevent any writing to the bucket which is not desired.
- ❌: "Attach an IAM policy to the bucket" is incorrect as users need to modify documents which will also allow delete. Therefore, a method must be implemented to just control deletes.
- ❌: "Encrypt the bucket using AWS SSE-S3" is incorrect as encryption doesn’t stop you from deleting an object.
  **References:**
  https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html
  https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html
----
#quiz 
- relateTo:: [[Domain 3 Design Secure Applications and Architectures]]
