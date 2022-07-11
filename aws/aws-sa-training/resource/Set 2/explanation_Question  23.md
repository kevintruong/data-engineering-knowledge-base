**Explanation:**

In this scenario we need to keep the objects in the STANDARD storage class for 30 days as the objects are being

frequently accessed. We can configure a lifecycle action that then transitions the objects to INTELLIGENT_TIERING,

STANDARD_IA, or ONEZONE_IA. After that we don’t need the objects so they can be expired.

All other options do not meet the stated requirements or are not supported lifecycle transitions. For example:

- You cannot transition to REDUCED_REDUNDANCY from any storage class.

- Transitioning from STANDARD_IA to ONEZONE_IA is possible but we do not want to keep the objects so it incurs

  unnecessary costs.

- Transitioning to GLACIER is possible but again incurs unnecessary costs.

- ✅ :  "Transition to ONEZONE_IA after 30 days. After 90 days expire the objects " is the correct answer.

- ❌ :  "Transition to STANDARD_IA after 30 days. After 90 days transition to GLACIER" is incorrect.

- ❌ :  "Transition to STANDARD_IA after 30 days. After 90 days transition to ONEZONE_IA" is incorrect.

- ❌ :  "Transition to REDUCED_REDUNDANCY after 30 days. After 90 days expire the objects " is incorrect.

**References:**

<https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html>

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/>

----

- #lifecycle_transitions #<https://docs.aws.amazon.com/amazons3/latest/dev/lifecycle-transition-general-considerations.html> #lifecycle_action #days_transition #transitioning
