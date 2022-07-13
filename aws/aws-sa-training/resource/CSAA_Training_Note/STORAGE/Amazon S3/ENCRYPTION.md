#### ENCRYPTION


You can securely upload/download your data to Amazon S 3 via SSL endpoints using the HTTPS protocol (In Transit –

SSL/TLS).


**Encryption options:**


**Server side encryption options:**


- **SSE-S3 – Server Side Encryption with S3 managed keys**

  o Each object is encrypted with a unique key. o Encryption key is encrypted with a master key. o AWS regularly rotate

  the master key. o Uses AES 256.

- **SSE-KMS – Server Side Encryption with AWS KMS keys**

  o KMS uses Customer Master Keys (CMKs) to encrypt. o Can use the automatically created CMK key. o OR you can select

  your own key (gives you control for management of keys). o An envelope key protects your keys. o Chargeable.

- **SSE-C – Server Side Encryption with client provided keys**

  o Client manages the keys, S3 manages encryption. o AWS does not store the encryption keys. o If keys are lost data

  cannot be decrypted.


The following diagram depicts the options for enabling encryption and shows you where the encryption is applied and

where the keys are managed:

