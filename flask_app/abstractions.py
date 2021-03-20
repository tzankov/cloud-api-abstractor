from abc import ABCMeta, abstractstaticmethod

class IResource(metaclass=ABCMeta):
	@abstractstaticmethod
	def create():
		""" Interface create method """	

	@abstractstaticmethod
	def update():
		""" Interface update method """	

	@abstractstaticmethod
	def secure():
		""" Interface secure method """