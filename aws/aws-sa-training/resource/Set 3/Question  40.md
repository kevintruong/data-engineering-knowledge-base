#### Question  40


**An EC2 status check on an EBS volume is showing as** **_insufficient-data_****. What is the most likely explanation?**


1: The checks have failed on the volume


2: The checks may still be in progress on the volume


3: The volume does not have enough data on it to check properly


4: The checks require more information to be manually entered


Answer: 2


**Explanation:**


The possible values are ok, impaired, warning, or insufficient-data. If all checks pass, the overall status of the

volume is ok. If the check fails, the overall status is impaired. If the status is insufficient-data, then the checks

may still be taking place on your volume at the time.


- CORRECT "The checks may still be in progress on the volume" is the correct answer.


- INCORRECT "The checks have failed on the volume" is incorrect. The checks have not failed or the status would be

  impaired.


- INCORRECT "The volume does not have enough data on it to check properly" is incorrect. The volume does not need a

  certain amount of data on it to be checked properly.


- INCORRECT "The checks require more information to be manually entered" is incorrect. The checks do not require manual

  input.


**References:**


https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumeStatus.html


**Save time with our exam-specific cheat sheets:**


https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

