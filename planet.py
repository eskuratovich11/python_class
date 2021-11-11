G=6.67*10**(-11)
class Planet:
    systemplanets = 0 

    def __init__(self, color, size, temperature):
      self.color = 'blue'
      self.size = 'big'
      self.temperature = temperature
      Planet.systemplanets = Planet.systemplanets + 1
    @classmethod
    def count_systemsplanets (cls):
      print(cls.systemplanets)

    @staticmethod
    def find_g(M, R):
      g=G*M/R**2
      print(g)

    @property
    def temperature(self):
       return self.temperature

    @temperature.setter
    def temperature (self, temperature):
      if temperature > -60 and temperature < 60:
        self._temperature=temperature/2
      elif temperature >= 60:
        self._temperature= temperature
      elif temperature <= -60:
        self._temperature= -100

    def temperature_on_planet (self): 
      print('На этой планете температура в среднем равна', self._temperature)
 
Planet.find_g(6*10**24, 64*10**5)
earth = Planet('blue','big', 30)
Planet.count_systemsplanets()
earth.temperature_on_planet()