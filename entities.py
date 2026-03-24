class Bird:
	def __init__(self,species,gender,cost):
		self.species=species
		self.gender=gender
		self.cost=cost
		self.age=0
		self.isAlive=True
		self.isHungry=False
	def __str__(self):
		status="alive" if self.isAlive else "dead"
		hungry="hungry" if self.isHungry else "full"
		return f"{self.gender}, {self.species}, age:{self.age} {status} {hungry}"
	def age_up(self):
		if self.isAlive:
			self.age+=1
			self.isHungry=True
class Chicken(Bird):
	def __init__(self, gender ):
		super().__init__("chicken",gender,100)

class Duck (Bird):
	def __init__ (self,gender):
		super().__init__("duck",gender,150)
class Turkey(Bird):
	def __init__(selff,gender):
		super().__init__("turkey",gender,300)
c1=Chicken("male")
c2=Chicken("female")
d1=Duck("male")
d2=Duck("female")
t1=Turkey("male")
t2=Turkey("female")
for bird in [c1,c2,t1,t2,d1,d2]:
	print(bird)
