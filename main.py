import boto3
import json

# JSON-based secrets module. This is where it looks for the secret key file and reads it.
with open('security/secrets.json') as f:
	secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
	# Get the secret variable or return explicit exception.
	try:
		return secrets[setting]
	except KeyError:
		error_msg = 'Set the {0} environment variable'.format(setting)
		print(error_msg)


s3 = boto3.resource('s3')

aws_bucket_name = get_secret('AWS_STORAGE_BUCKET_NAME')


client = boto3.client(
	's3',
	aws_secret_access_key=get_secret('AWS_SECRET_ACCESS_KEY'),
	aws_access_key_id=get_secret('AWS_ACCESS_KEY_ID')
)


for bucket in client.buckets.all():
	print(bucket.name)
