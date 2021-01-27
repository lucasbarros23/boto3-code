import boto3



 # Provisionar EC2
ec2 = boto3.resource ( 'ec2' )
ec2.create_instances ( ImageId = 'ami-0885b1f6bd170450c' , MinCount = 1, MaxCount = 2, InstanceType = 't2.micro')


#Provisionar S3
s3 = boto3.client('s3')
s3.create_bucket(Bucket='NOME-DO-SEU-BUCKETT')





#describe
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)




#describe
s3 = boto3.client('s3')
response = s3.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')














