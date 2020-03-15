import boto3

s3_client = boto3.client('s3')
response = s3_client.list_buckets()

print('List of S3 buckets and their region:')
print("{:15} {:8}".format('Bucket', 'Region'))

for item in response['Buckets']:
    b_name = item['Name']
    response = s3_client.get_bucket_location(Bucket=b_name)
    b_region = response['LocationConstraint']
    print("{:15} {:8}".format(b_name, b_region))
