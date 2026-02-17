# Serverless File Processing System



## Overview



This project implements a serverless file processing workflow using AWS. When a file is uploaded to an Amazon S3 bucket, an AWS Lambda function is triggered automatically. The function reads file metadata and stores processing logs in Amazon CloudWatch.



## Architecture



User Upload → Amazon S3 → Lambda Trigger → CloudWatch Logs



## AWS Services Used



* Amazon S3

* AWS Lambda

* AWS IAM

* Amazon CloudWatch



## Prerequisites



* AWS account

* Basic knowledge of AWS Console

* Python runtime selected in Lambda



## Setup Steps



### Step 1: Create S3 Bucket



1. Open AWS Console

2. Go to Amazon S3

3. Click Create bucket

4. Enter a unique bucket name

5. Keep default settings and create the bucket



### Step 2: Create IAM Role for Lambda



1. Open IAM

2. Go to Roles and click Create role

3. Select AWS service and choose Lambda

4. Attach policy: AWSLambdaBasicExecutionRole

5. Name the role: Lambda-S3-Execution-Role

6. Create the role



### Step 3: Create Lambda Function



1. Open AWS Lambda

2. Click Create function

3. Select Author from scratch

4. Function name: S3FileProcessor

5. Runtime: Python 3.x

6. Choose existing role and select Lambda-S3-Execution-Role

7. Create the function



### Step 4: Add Lambda Code



Replace the default code with:



```

import urllib.parse



def lambda_handler(event, context):

&nbsp;   for record in event['Records']:

&nbsp;       bucket = record['s3']['bucket']['name']

&nbsp;       key = urllib.parse.unquote_plus(record['s3']['object']['key'])

&nbsp;       size = record['s3']['object']['size']



&nbsp;       print("Bucket:", bucket)

&nbsp;       print("File:", key)

&nbsp;       print("Size:", size, "bytes")



&nbsp;   return "Success"

```



Deploy the function.



### Step 5: Add S3 Trigger



1. Open the Lambda function

2. Click Add trigger

3. Select S3

4. Choose your bucket

5. Event type: All object create events

6. Add the trigger



### Step 6: Test the Project



1. Open your S3 bucket

2. Upload any file

3. The Lambda function will run automatically



### Step 7: Verify Logs



1. Open Amazon CloudWatch

2. Go to Log groups

3. Open the log group for the Lambda function

4. View file details in the logs



## Workflow



1. User uploads a file to S3

2. S3 event triggers Lambda

3. Lambda reads file details

4. Processing logs are stored in CloudWatch



## Optional Enhancements



* Validate file type before processing

* Rename files after upload

* Send SNS notification after processing

* Move processed files to a different folder



## Benefits



* No server management required

* Automatic scaling based on events

* Centralized logging for monitoring

* Cost efficient pay per use architecture



