**Explanation:**

RedShift is a columnar data warehouse DB that is ideal for running long complex queries. RedShift can also improve

performance for repeat queries by caching the result and returning the cached result when queries are re-run. Dashboard,

visualization, and business intelligence (BI) tools that execute repeat queries see a significant boost in performance

due to result caching.

- ✅ :  "RedShift for both use cases" is the correct answer.

- ❌ :  "RDS for both use cases" is incorrect. RDS may be a good fit for the fast queries (not for the complex

  queries) but you now have multiple DBs to manage and multiple sets of data which is not going to be cost-effective.

- ❌ :  "RedShift for the analytics use case and ElastiCache in front of RedShift for the customer support

  dashboard" is incorrect. You could put ElastiCache in front of the RedShift DB and this would provide good performance

  for the fast, repeat queries. However, it is not essential and would add cost to the solution so is not the most

  cost-effective option available.

- ❌ :  "RedShift for the analytics use case and RDS for the customer support dashboard" is incorrect as RedShift is

  a better fit for both use cases.

**References:**

<https://aws.amazon.com/about-aws/whats-new/2017/11/amazon-redshift-introduces-result-caching-for-sub>-

second-response-for-repeat-queries/

**Save time with our exam-specific cheat sheets:**

<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>- redshift/

----

- #redshift_db #<https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon>-_redshift/> #columnar_data_warehouse_db #<https://aws.amazon.com/about-aws/whats-new/2017/11/amazon-redshift-introduces-result-caching-for-sub>>- #fast_queries
