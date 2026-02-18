# Serverless File Processing System







## Overview







Built a serverless file processing pipeline using AWS services. The system triggers an AWS Lambda function when a file is uploaded to an Amazon S3 bucket. The function reads file metadata and stores logs in Amazon CloudWatch.







## Architecture







User Upload → Amazon S3 → Lambda Trigger → CloudWatch Logs







## AWS Services Used







* Amazon S3



* AWS Lambda



* AWS IAM



* Amazon CloudWatch







## Features







* Automatic Lambda trigger on file upload



* Extracts bucket name and file information



* Logs file details to CloudWatch



* Fully serverless architecture with no server maintenance







## Workflow







1\. Upload a file to the S3 bucket



2\. S3 event triggers the Lambda function



3\. Lambda reads event metadata such as bucket name and file key



4\. Processing details are stored in CloudWatch logs







## Benefits







* No infrastructure management required



* Automatic scaling based on events



* Centralized logging for monitoring and troubleshooting



* Cost efficient pay per use architecture







## Outcome







Successfully built a serverless file processing system where file uploads to Amazon S3 automatically trigger an AWS Lambda function to process file metadata and store logs in Amazon CloudWatch, enabling a scalable, secure, and fully automated event driven workflow.

