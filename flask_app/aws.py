from abstractions import IResource

class AwsResource(IResource):
	def __init__(self):
		self.name = "AWS Resource"
		print(self.name)

	def create(self):
		print("aws create")

	def update():
		print("aws update")

	def secure(self):
	    print("aws sg")
