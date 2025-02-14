def convert_cel_to_far(cel):
  return (cel * 9/5) + 32
def convert_far_to_cel(far):
  return (far - 32) * 5/9

print("Enter a temperature in celcius.")
celcius = float(input())
print(f"{round(convert_cel_to_far(celcius), 2)} farenheit")
print("Enter a temperature in farenheit.")
farenheit = float(input())
print(f"{round(convert_far_to_cel(farenheit), 2)} celsius")