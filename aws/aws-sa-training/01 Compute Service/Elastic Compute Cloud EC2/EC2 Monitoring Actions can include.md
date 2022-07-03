### **EC2 Monitoring Actions can include:**
- Recover the instance (only supported on specific instance types and can be used only with StatusCheckFailed_System).
- Stop the instance (only applicable to EBS-backed volumes).
- Terminate the instance (cannot terminate if termination protection is enabled).
- Reboot the instance.
  
  It is a best practice to use EC2 to reboot instance rather than the OS (create a CloudWatch record).
  
  **CloudWatch Monitoring frequency:**
- Standard monitoring = 5 mins
- Detailed monitoring = 1 min (chargeable)

----
- up:: [[EC2 MONITORING]]