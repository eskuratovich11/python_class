class Tomato:

  global states, n
  states=['none', 'flower', 'green','red']
  

  def __init__(self, i):
      self.i= i 
      self.x  = 0
      self.state = states[self.x]
      print(self.state)

  def grow(self):
      self.x  += 1
      self.state = states[self.x]
      print(self.state)

  def is_ripe(self):

    if self.x == 3 :
      self.ripe= True
      print(self.ripe)
    else:
      self.ripe=False
      print(self.ripe)

class TomatoBush:

  def __init__(self,n):

     self.tomatoes = [Tomato(i) for i in range(0, n)]

     print(self.tomatoes)

  def grow_all(self):
    for tomato in self.tomatoes:
      tomato.grow()

#  def all_are_ripe(self):
#     self.ripe_all= [tomato.is_ripe() for i in range (self.tomatoes)]
#      print(self.ripe_all)

  def give_away_all(self):
        self.tomatoes = []

class Gardener :

  def __init__(self, name, plant):
        self.name= name
        self.plant = plant 

  def work (self):
     self.plant.grow_all()

  def knowledge_base(self):
       self.knowledge_base= 'справка по садоводству'
       print (self.knowledge_base)

tomato1=Tomato(1)
plant1=TomatoBush(2)
gardener1= Gardener ('Ivan', plant1 )
gardener1.work()
gardener1.work()
tomato1.is_ripe()
