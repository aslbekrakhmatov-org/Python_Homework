def check(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Can't divide by zero"
    return wrapper

@check
def div(a, b):
    return a / b  

print(div(10, 2))
print(div(10, 0))
