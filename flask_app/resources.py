from az import AzureResource
from aws import AwsResource

class ResourceFactory:
	@staticmethod
	def build_resource(action, resource_type):
		if resource_type == "ec2":
			aws = AwsResource()
			if action == "create":
				return aws.create()
			elif action == "update":
				return aws.update()
			elif action == "secure":
				return aws.secure()
		if resource_type == "vm":
			az = AzureResource()
			if action == "create":
				return az.create()
			elif action == "update":
				return az.update()
			elif action == "secure":
				return az.secure()
		print("Invalid type")
		return 1