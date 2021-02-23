from abc import ABCMeta, abstractstaticmethod

class IResource(metaclass=ABCMeta):
	@abstractstaticmethod
	def create():
		""" Interface create method """	

	@abstractstaticmethod
	def peer():
		""" Interface peer method """		
	    

class AWSResource(IResource):
	def __init__(self):
		self.name = "AWS Resource"
		print(self.name)

	def create(self):
		print("aws create")

	def peer(self):
	    print("aws peer")


class AzureResource(IResource):
	def __init__(self):
		self.name = "Azure Resource"
	
	def create(self):
		print("azure create")

	def peer(self):
	    print("azure peer")


class ResourceFactory:
	@staticmethod
	def build_resource(action, resource_type):
		if resource_type == "VPC":
			aws = AWSResource()
			if action == "create":
				return aws.create()
			elif action == "peer":
				return aws.peer()
		if resource_type == "VNET":
			return AzureResource(action)
		print("Invalid type")
		return 1



# import sys
# import inspect

# function_list = [o[0] for o in inspect.getmembers(sys.modules[__name__], inspect.isfunction)]

# actions = {}
# for func in function_list:
#	actions[func] = str(func)