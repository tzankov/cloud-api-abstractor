from abstractions import IResource

class AzureResource(IResource):
	def __init__(self):
		self.name = "Azure Resource"
	
	def create(self):
		print("azure create")

	def update():
		print("azure update")

	def secure(self):
	    print("azure nsg")
