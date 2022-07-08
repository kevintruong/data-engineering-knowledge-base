## Quiz 33: An Amazon RDS Read Replica is being deployed in a separate region. The master database is not encrypted but all data in the new region must be encrypted. How can this be achieved?**

- [ ] Enable encryption using Key Management Service (KMS) when creating the cross-region Read Replica
- [ ] Encrypt a snapshot from the master DB instance, create an encrypted cross-region Read Replica from the snapshot
- [ ] Enabled encryption on the master DB instance, then create an encrypted cross-region Read Replica
- [x] Encrypt a snapshot from the master DB instance, create a new encrypted master DB instance, and then create an encrypted cross-region Read Replica

----
Answer:

- [x] Encrypt a snapshot from the master DB instance, create a new encrypted master DB instance, and then create an encrypted cross-region Read Replica
  **Explanation:**
  You cannot create an encrypted Read Replica from an unencrypted master DB instance. You also cannot enable encryption after launch time for the master DB instance. Therefore, you must create a new master DB by taking a snapshot of the existing DB, encrypting it, and then creating the new DB from the snapshot. You can then create the encrypted cross-region Read Replica of the master DB.
- ✅: "Encrypt a snapshot from the master DB instance, create a new encrypted master DB instance, and then create an encrypted cross-region Read Replica" is the correct answer.

- ❌: "Enable encryption using Key Management Service (KMS) when creating the cross-region Read Replica" is incorrect. All other options will not work due to the limitations explained above.

- ❌: "Encrypt a snapshot from the master DB instance, create an encrypted cross-region Read Replica from the snapshot" is incorrect. All other options will not work due to the limitations explained above.

- ❌: "Enabled encryption on the master DB instance, then create an encrypted cross-region Read Replica" is incorrect. All other options will not work due to the limitations explained above.
  **References:**
  https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html
  https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html


----
#quiz 
- relateTo:: [[Domain 3 Design Secure Applications and Architectures]]