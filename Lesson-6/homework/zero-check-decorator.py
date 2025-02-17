def check(func):
  def wrapper(a, b):
    try:
      return func(a, b) 
    except ZeroDivisionError:
      return "Can't divided by zero"
  return wrapper
# div = check(div)
@check
def div(a, b):
  return a/b

result = div(2, 0)
print(result)

