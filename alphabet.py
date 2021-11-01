class Alphabet:

    def __init__(self, language):
        self.language = language
        self.letters  = ['a','b']

    def printer (self) :
      
      print (self.letters)


    def letters_num (self) :
      
      print(len(self.letters))  

 
alphabet1 = Alphabet('apricot')

print(alphabet1.language)

alphabet1.letters = ['w','m','l','a']

alphabet1.printer()
alphabet1.letters_num()

alphabet2 = Alphabet('tomta')

print(alphabet2.language)

alphabet2.letters = ['t','m','y','a','o','@']

alphabet2.printer()
alphabet2.letters_num()
