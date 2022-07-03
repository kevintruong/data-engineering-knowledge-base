### **What type of consistency model is provided in Amazon S3 when you upload a new version of an object?**

- [ ] Read after write consistency
- [x] Eventual consistency

----

**Answer:**

Eventual consistency

**Explanation:**

- Read after write consistency is incorrect. You do not get read after write consistency for overwrite PUT and DELETES.
- Eventual consistency is correct. In Amazon S3 you get eventual consistency for overwrite PUTS and DELETES.

---- 
#quiz 