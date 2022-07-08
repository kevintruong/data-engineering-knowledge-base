---
date created: 2022-07-05 23:15
---

## Quiz 4: A company stores important data in an Amazon S3 bucket. A solutions architect needs to ensure that data can be recovered in case of accidental deletion.**

**Which action will accomplish this?**

- [ ] Enable Amazon S3 versioning
- [ ] Enable Amazon S3 Intelligent-Tiering
- [ ] Enable an Amazon S3 lifecycle policy
- [ ] Enable Amazon S3 cross-Region replication

---

Answer: 1
**Explanation:**
Object versioning is a means of keeping multiple variants of an object in the same Amazon S3 bucket. Versioning provides the ability to recover from both unintended user actions and application failures. You can use versioning to preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket.

- ✅: "Enable Amazon S3 versioning" is the correct answer.
- ❌: "Enable Amazon S3 Intelligent-Tiering" is incorrect. This is a storage class that automatically moves data between frequent access and infrequent access classes based on usage patterns.
- ❌: "Enable an Amazon S3 lifecycle policy" is incorrect. An S3 lifecycle policy is a set of rules that define actions that apply to groups of S3 objects such as transitioning objects to another storage class.
- ❌: "Enable Amazon S3 cross-Region replication" is incorrect as this is used to copy objects to different regions. CRR relies on versioning which is the feature that is required for protecting against accidental deletion.
  **References:**
  <https://d0.awsstatic.com/whitepapers/protecting-s3-against-object-deletion.pdf>


---- 
#quiz 
- relateTo:: [[Domain 1 Design Resilient Architectures]]