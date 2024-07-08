# Solution Architecting: National Day Parade 2023 Web Application

## Introduction

As part of the  National Day Parade 2023 project, I was tasked with designing an AWS architecture to host their web application, which consists of a React frontend, a NodeJS backend, and a Postgres database. Below, I will detail the architecture I designed and how it aligns with the six pillars of the AWS Well-Architected Framework.

## Architecture Overview

* **Frontend:** React, hosted by an S3 bucket
* **Backend:** NodeJS, handled by EC2 instances in the app tier
* **Database:** Postgres, managed by RDS

Users across the internet access the web application by typing the domain name into their browsers. The DNS request is handled by AWS Route 53, which resolves the domain name to the correct IP address. Route 53 then directs the traffic to CloudFront, which serves cached content from the nearest edge location to ensure quick load times. If the requested content is not cached, CloudFront retrieves it from the S3 bucket, which hosts the static website files (HTML, CSS, JavaScript). 

For dynamic content or API requests, CloudFront forwards the requests to an Elastic Load Balancer (ELB), which distributes the traffic to EC2 instances in the web tier managed by an Auto Scaling Group. This group ensures that enough instances are running to handle the traffic, automatically adjusting the number of instances based on demand. Requests needing backend processing are further routed by another ELB in the application tier to EC2 instances that handle business logic and database interactions. These instances communicate with a PostgreSQL database hosted on Amazon RDS, ensuring secure and reliable data storage and retrieval.

## Well-Architected Framework

### 1. Operational Excellence

To achieve operational excellence, I implemented:
* **Automated Deployments:** Leveraging Terraform for Infrastructure as Code (IaC) ensures consistent, repeatable deployments. This approach allows for rapid iteration and deployment of updates without manual intervention, thus minimizing errors and speeding up the deployment process.
* **Monitoring and Logging:** Comprehensive logging and monitoring are provided by AWS CloudWatch and CloudTrail. This setup is particularly vital for the web application, allowing the development team to quickly identify and address issues, ensuring smooth operation during high-traffic events like the National Day Parade.

### 2. Security

To ensure best security practices:
* **AWS WAF and AWS Shield:** These services protect against web application attacks and DDoS attacks, respectively. For an event as significant as the National Day Parade, ensuring the application is shielded from potential threats is critical to maintaining user trust and service availability.
* **Security Groups and IAM Roles:** Fine-grained access control ensures that only authorized users and services can access resources. This approach minimizes the risk of unauthorized access and data breaches, which is essential for protecting sensitive user information.
* **Data Encryption:** Encryption at rest is handled using AWS KMS, and in-transit data is secured with SSL/TLS. User information transmitted within the application is securely stored and transmitted, maintaining data integrity and privacy.
* **Route 53 and CloudFront:** Secure content distribution using HTTPS ensures that all user interactions with the web application are secure and trustworthy.

### 3. Reliability

To ensure high reliability and availability:
* **Multi-AZ Deployment:** Resources like RDS and EC2 instances are deployed across multiple Availability Zones to ensure high availability and fault tolerance. This design ensures that the application can withstand failures in one zone without affecting user access.
* **Auto Scaling Groups:** Automatically adjust the number of EC2 instances based on traffic, ensuring the application can handle increases in load. This setup allows the application to scale out to keep up with heavier traffic during peak hours such as during the parade itself.
* **Elastic Load Balancers:** Distribute incoming application traffic across multiple targets, increasing the fault tolerance of the application. This setup ensures that no single server is overwhelmed by traffic, maintaining the application's responsiveness and availability.

### 4. Performance Efficiency

For performance efficiency:
* **Auto Scaling:** Dynamically adjusts resources based on demand, ensuring optimal performance at all times. This means that the application can handle varying levels of traffic without over-provisioning resources, which is cost-effective and efficient.
* **CloudFront:** Provides low-latency content delivery through a global network of edge locations. Singaporeans from all over the world can minimize latency, allowing for a more seamless experience using the web application.
* **RDS Read Replicas:** Improve read performance by distributing read traffic among multiple database replicas. This ensures that the application can handle a high number of read requests, which is critical during the high-traffic event of the National Day Parade.

### 5. Cost Optimization

Reducing operational costs can be done in a few ways:
* **S3 for Static Content:** Using S3 for static website hosting is cost-effective compared to running a web server. This reduces costs while providing high durability and availability for the static assets of the web application.
* **Auto Scaling:** Ensures only the necessary resources are used, reducing unnecessary costs. This design ensures that we only pays for what they use, avoiding over-provisioning and optimizing resource usage.
* **Reserved Instances:** If we are able to estimate or predict the traffic flow to the web server, we will be able to be cost efficient in our spending on compute costs.

### 6. Sustainability

Sustainability of resources such as energy or costs:
* **Efficient Resource Utilization:** Auto scaling and right-sizing of resources ensure that only necessary resources are utilized, reducing waste.
* **Managed Services:** Using managed services like RDS and CloudFront helps reduce the operational burden and energy consumption associated with managing these services in-house.

---

This architecture ensures that the National Day Parade web application is secure, highly available, and efficient, aligning with the AWS Well-Architected Framework.

**Note**
-  Another consideration for the architecture would be to make the back end serverless. This could be done with an API gateway attatched to cloudfront instead of an autoscaling group, which then points to Lamda service which points to the Aurora database for postgre. This provides a serverless architecture which would ensure high availability and tolerance. Lamda functions and the Aurora database would be able to scale in and out automatically according to traffic, negating the need for us to manually scale the auto scaling groups in the previous architecture.
