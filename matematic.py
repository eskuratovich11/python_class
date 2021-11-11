def matematic(func):

    def wrapper(n1,n2, znak):

      if znak == '+':

        print(n1+n2)

      elif znak == '*':

        print(n1+n2)

      elif znak == '/':

        print(n1/n2)

      elif znak == '-':
        
        print(n1-n2)

    return wrapper


@matematic
def two_variables(n1,n2, znak):
 return n1,n2, znak
 
two_variables(6,5,'+')