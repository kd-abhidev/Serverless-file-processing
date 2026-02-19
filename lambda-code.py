import json

def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']
        file_size = record['s3']['object'].get('size', 0)

        print("New file uploaded")
        print(f"Bucket: {bucket_name}")
        print(f"File: {file_name}")
        print(f"Size: {file_size} bytes")

    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully')
    }
