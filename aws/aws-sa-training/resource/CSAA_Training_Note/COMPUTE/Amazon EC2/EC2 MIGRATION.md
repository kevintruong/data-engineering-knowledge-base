#### EC2 MIGRATION


VM Import/Export is a tool for migrating VMware, Microsoft, XEN VMs to the Cloud.


Can also be used to convert EC2 instances to VMware, Microsoft or XEN VMs.


**Supported for:**


- Windows and Linux.

- VMware ESX VMDKs and (OVA images for export only).

- Citrix XEN VHD.

- Microsoft Hyper-V VHD.


Can only be used via the API or CLI (not the console).


Stop the VM before generating VMDK or VHD images.


**AWS has a VM connector plugin for vCenter:**


- Allows migration of VMs to S3.

- Then converts into a EC2 AMI.

- Progress can be tracked in vCenter.

