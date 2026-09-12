
def create_name(first, last):

    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("oyebola", "timileyin")
print(full_name)


# function = A block of reusable code #   Place () after the function name to invoke it 
def happy_birthday (name, age, gender):
    print(f"Happy birthday to you, {name}!")
    print(f"You are {age} years old")
    print(f"You are a {gender}")
    print(f"Wishing you long life and prosperity, good {gender}!")

happy_birthday("Bob", 30, "boy") 
happy_birthday("Alice", 17, "girl")
happy_birthday("Faith", 16, "girl")
happy_birthday("Samuel", 17, "boy")