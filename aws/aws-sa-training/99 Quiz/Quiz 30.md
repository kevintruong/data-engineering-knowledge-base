## Quiz 30: A company wishes to restrict access to their Amazon DynamoDB table to specific, private source IP addresses from their VPC. What should be done to secure access to the table?**

- [ ] Create an interface VPC endpoint in the VPC with an Elastic Network Interface (ENI)
- [x] Create a gateway VPC endpoint and add an entry to the route table
- [ ] Create the Amazon DynamoDB table in the VPC
- [ ] Create an AWS VPN connection to the Amazon DynamoDB endpoint

----
Answer:

- [x] Create a gateway VPC endpoint and add an entry to the route table
  **Explanation:**
  There are two different types of VPC endpoint: interface endpoint, and gateway endpoint. With an interface endpoint you use an ENI in the VPC. With a gateway endpoint you configure your route table to point to the endpoint. Amazon S3 and DynamoDB use gateway endpoints. This solution means that all traffic will go through the VPC endpoint straight to DynamoDB using private IP addresses.
  ![](aws-solution-architecture-practice-quiz-1641093034952.png)
- ✅: "Create a gateway VPC endpoint and add an entry to the route table" is the correct answer.

- ❌: "Create an interface VPC endpoint in the VPC with an Elastic Network Interface (ENI)" is incorrect. As mentioned above, an interface endpoint is not used for DynamoDB, you must use a gateway endpoint.

- ❌: "Create the Amazon DynamoDB table in the VPC" is incorrect. You cannot create a DynamoDB table in a VPC, to connect securely using private addresses you should use a gateway endpoint instead.

- ❌: "Create an AWS VPN connection to the Amazon DynamoDB endpoint" is incorrect. You cannot create an AWS VPN connection to the Amazon DynamoDB endpoint.
  **References:**
  https://docs.amazonaws.cn/en_us/vpc/latest/userguide/vpc-endpoints-ddb.html
  https://aws.amazon.com/premiumsupport/knowledge-center/iam-restrict-calls-ip-addresses/
  https://aws.amazon.com/blogs/aws/new-vpc-endpoints-for-dynamodb/

----
#quiz 
- relateTo:: [[Domain 1 Design Resilient Architectures]]