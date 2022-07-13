#### AMIS


An Amazon Machine Image (AMI) is a special type of virtual appliance that is used to create a virtual machine within the

Amazon Elastic Compute Cloud (“EC2”).


**An AMI includes the following:**


- A template for the root volume for the instance (for example, an operating system, an application server, and

  applications).

- Launch permissions that control which AWS accounts can use the AMI to launch instances.

- A block device mapping that specifies the volumes to attach to the instance when it’s launched.


AMIs are either instance store-backed or EBS-backed.


**Instance store-backed:**


- Launch an EC2 instance from an AWS instance store-backed AMI.

- Update the root volume as required.

- Create the AMI which will upload to a user-specified S3 bucket (user bucket).

- Register the AMI with EC2 (creates another EC2 controlled S3 image).

- To make changes update the source then deregister and reregister.

- Upon launch the image is copied to the EC2 host.

- Deregister an image when the AMI is not needed anymore (does not affect existing


```

instances created from the AMI).

```


- Instance store-backed volumes can only be created at launch time.


**EBS-backed:**


- Must stop the instance to create a consistent image and then create the AMI.

- AWS registers the AMIs manually.

- During creation AWS creates snapshots of all attached volumes – there is no need to specify a bucket but you will be

  charged for storage on S3.

- You cannot delete the snapshot of the root volume as long as the AMI is registered

  (deregister and delete).

- You can now create AMIs with encrypted root/boot volumes as well as data volumes (can also use separate CMKs per

  volume).


**Copying AMIs:**


- You can copy an Amazon Machine Image (AMI) within or across an AWS region using the AWS Management Console, the AWS

  AWS Command Line Interface or SDKs, or the Amazon EC2 API, all of which support theCopyImage action.

- You can copy both Amazon EBS-backed AMIs and instance store-backed AMIs.

- You can copy encrypted AMIs and AMIs with encrypted snapshots.

