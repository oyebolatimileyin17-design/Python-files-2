#Tuples are quick ways of storing multiple values that can't be changed
my_tuple = (1, 2, 3, 4,)
#my_tuple [0] = 20 # This prints an error message cause tuples can't be changed
  
  #Sets don't allow duplicates i.e it auto removes them
  #Sets items are'nt stored in a fixed position and It doesn't allow for indexing
my_set = {1, 2, 3, 3, 4, 5, 6,  }
print(my_set)

fruits = {"Mango", "Watermelon"}
fruits.add ("Cucumber")
fruits.remove("Mango")
print(len(fruits))

#People generally use set cause it removes duplicates
numbers = [1, 2, 3, 4, 7, 1, 9, ]
unique_numbers = set(numbers)
print(unique_numbers)

list_numbers = [1, 2, 3, 3, 1, 9, 29, 40, ]
numbers = set(list_numbers)
print(numbers)
