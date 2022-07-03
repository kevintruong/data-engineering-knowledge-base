---
up: [[EC2]] 
---

### **EC2 Metadata and User Data:**

<!-- #ec2_metadata #ec2_userdata -->
- User data is data that is supplied by the user at instance launch in the form of a script.
- Instance metadata is data about your instance that you can use to configure or manage the running instance.
- User data is limited to 16KB.
- User data and metadata are not encrypted.
- Instance metadata is available at [http://169.254.169.254/latest/meta-data/](http://169.254.169.254/latest/meta-data/) (the trailing “/” is required).
- Instance user data is available at: [http://169.254.169.254/latest/user-data.](http://169.254.169.254/latest/user-data.)
- The IP address 169.254.169.254 is a link-local address and is valid only from the instance.
- On Linux you can use the curl command to view metadata and userdata, e.g. “curl [http://169.254.169.254/latest/meta-data/”.](http://169.254.169.254/latest/meta-data/”.)
- The Instance Metadata Query tool allows you to query the instance metadata without having to type out the full URI or category names.