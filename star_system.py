class StarSystem:
    def __init__(self, name, planets):
        self.planets = planets
        self.name = name
        
    def info(self):
          print( self.name, self.planets)

    def __sub__(self, other):
        self.planets.remove(other)
        return StarSystem( self.name, self.planets)    


    def __rsub__(self, other):
        self.planets= list( set(other)- set(self.planets))
        return StarSystem(self.name, self.planets)

    
    def __isub__(self, other):
        self.planets.remove(other)
        return self

system_1 = StarSystem('System_1', ['planet_1', 'planet_2', 'planet_3', 'planet_4'])


system_1 -= 'planet_2'
system_1.info()

system_1= system_1- 'planet_1'
system_1.info()

new_system_1 = ['planet_3', 'planet_4', 'planet_5']
system_1 = new_system_1 - system_1
system_1.info()
