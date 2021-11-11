def summator(arg1):
  
  def decorator(func):

    def wrapper(arg2):

      print(arg1+arg2)

    return wrapper

  return decorator

@summator(6)
def f(arg2):
 return arg2

f(7)