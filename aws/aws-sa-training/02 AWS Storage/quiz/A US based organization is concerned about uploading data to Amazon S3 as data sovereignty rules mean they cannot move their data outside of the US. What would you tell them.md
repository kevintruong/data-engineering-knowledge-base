### **A US based organization is concerned about uploading data to Amazon S3 as data sovereignty rules mean they cannot move their data outside of the US. What would you tell them?**

- [ ] Data never leaves a region unless specifically configured to do so.
- [ ] Data will be replicated globally so they cannot use Amazon S3.

---- 

**Answer: 1**

Data never leaves a region unless specifically configured to do so.

**Explanation:**

- Data never leaves a region unless specifically configured to do so is correct. S3 is a global service but buckets are created within a region. Data is never replicated outside of that region unless you configure it (e.g. through CRR).
- Data will be replicated globally so they cannot use Amazon S3 is incorrect. Data is not replicated globally with Amazon S3.

---- 
#quiz 