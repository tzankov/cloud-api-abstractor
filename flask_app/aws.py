from abstractions import IResource

class AwsResource(IResource):
	def __init__(self):
		self.name = "AWS Resource"

	def create(self):
		print("aws create")

	def update(self):
		print("aws update")

	def secure(self):
	    print("aws sg")
