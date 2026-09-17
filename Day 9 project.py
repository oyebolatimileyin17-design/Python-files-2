def find_average(*numbers):
   total = sum(numbers)
   count = len(numbers)
   average = total / count
   return average
result = find_average(900 ,-4, 14)
print(result)

if result < 0:
   print("No fool")
elif result > 0:
     print("Yes boy")
else:
    print("You are not serious")
    