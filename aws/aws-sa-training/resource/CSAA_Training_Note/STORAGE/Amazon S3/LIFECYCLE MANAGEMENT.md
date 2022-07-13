#### LIFECYCLE MANAGEMENT

Used to optimize storage costs, adhere to data retention policies and to keep S3
volumes well- maintained.

A _lifecycle configuration_ is a set of rules that define actions that Amazon S3
applies to a group of objects. There

are two types of actions:

- **Transition actions** —Define when objects transition to another storage
  class. For example, you might choose to

  transition objects to the STANDARD_IA storage class 30 days after you created
  them, or archive objects to the GLACIER

  storage class one year after creating them.

There are costs associated with the lifecycle transition requests. For pricing
information, see Amazon S3 Pricing.

- **Expiration actions** —Define when objects expire. Amazon S3 deletes expired
  objects on your behalf.

Lifecycle configuration is an XML file applied at the bucket level as a
subresource.

Can be used in conjunction with versioning or independently.

Can be applied to current and previous versions.

Can be applied to specific objects within a bucket: objects with a specific tag
or objects with a specific prefix.

**Supported Transitions and Related Constraints**

**Amazon S3 supports the following lifecycle transitions between storage classes
using a lifecycle configuration:**

- You can transition from the STANDARD storage class to any other storage class.

- You can transition from any storage class to the GLACIER or DEEP_ARCHIVE
  storage classes.

- You can transition from the STANDARD_IA storage class to the
  INTELLIGENT_TIERING or ONEZONE_IA storage classes.

- You can transition from the INTELLIGENT_TIERING storage class to the
  ONEZONE_IA storage class.

- You can transition from the GLACIER storage class to the DEEP_ARCHIVE storage
  class.

**The following lifecycle transitions are not supported:**

- You can't transition from any storage class to the STANDARD storage class.

- You can't transition from any storage class to the REDUCED_REDUNDANCY storage
  class.

- You can't transition from the INTELLIGENT_TIERING storage class to the
  STANDARD_IA storage class.

- You can't transition from the ONEZONE_IA storage class to the STANDARD_IA or
  INTELLIGENT_TIERING storage classes.

- You can transition from the GLACIER storage class to the DEEP_ARCHIVE storage
  class only.

- You can't transition from the DEEP_ARCHIVE storage class to any other storage
  class.

**The lifecycle storage class transitions have the following constraints:**

- From the STANDARD or STANDARD_IA storage class to INTELLIGENT_TIERING. The
  following constraints apply:

  o For larger objects, there is a cost benefit for transitioning to
  INTELLIGENT_TIERING. Amazon S3 does not transition

  objects that are smaller than 128 KB to the INTELLIGENT_TIERING storage class
  because it's not cost effective.

- From the STANDARD storage classes to STANDARD_IA or ONEZONE_IA. The following
  constraints apply:

  o For larger objects, there is a cost benefit for transitioning to STANDARD_IA
  or ONEZONE_IA. Amazon S3 does not

  transition objects that are smaller than 128 KB to the STANDARD_IA or
  ONEZONE_IA storage classes because it's not cost

  effective. o Objects must be stored at least 30 days in the current storage
  class before you can transition them to

  STANDARD_IA or ONEZONE_IA. For example, you cannot create a lifecycle rule to
  transition objects to the STANDARD_IA

  storage class one day after you create them. o Amazon S3 doesn't transition
  objects within the first 30 days because

  newer objects are

```

often accessed more frequently or deleted sooner than is suitable for STANDARD_IA or

ONEZONE_IA storage.

o If you are transitioning noncurrent objects (in versioned buckets), you can transition

only objects that are at least 30 days noncurrent to STANDARD_IA or ONEZONE_IA

storage.

```

- From the STANDARD_IA storage class to ONEZONE_IA. The following constraints
  apply:

  o Objects must be stored at least 30 days in the STANDARD_IA storage class
  before you can transition them to the

  ONEZONE_IA class.

