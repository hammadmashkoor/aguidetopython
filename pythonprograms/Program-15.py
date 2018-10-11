""" Program-15 : To demonstrate working of classes and objects """
class animal(object):
	#class for animals

	def __init__(self, name, animal, description, emotion): #representing the instance of the object
		self.name = name # specify the name of the animal
		self.animal = animal # specify the animal
		self.description = description # specify the description of the animal
		self.emotion = emotion #specify its emotion


	def whatisit(self): #a method for a brief desicption
		print( "{} the {}".format(self.name, self.animal)) #print the name and animal specified

	def describe(self):
		print(self.description)

	def feels(self):
		print("{} the {} {}".format(self.name,self.animal, self.emotion))

dog = animal("Spot","labrador", "Obedient and tame", "is very happy") #initializied the object dog 


dog.whatisit() #using the method whatisit
dog.describe() #using the method describe
dog.feels() #using the method feels