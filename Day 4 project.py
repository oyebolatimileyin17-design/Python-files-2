try:
 
  number_input = int(input("Enter a number:"))
  if number_input < 0:
    print("That's a negative number.")
  elif number_input > 0:
    print("That's a positive number.")
  else:
    print("That's zero.")
  if number_input % 2 == 0:
    print("That's an even number")
  else:
    print("That's an Odd number")
    
except ValueError:
    print("That's not a real number.")



