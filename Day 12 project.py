word = "Education"
print(word[0])      # P
print(word[-1])      # n
print(word[0:3])    # Pyt
print(word[3:])     # hon
print(word[0:7:2])

sentence = "I love learning coding"
words = sentence.split()
print(words)

data = "apple.pawpaw.orange"
items = data.split(".")
print(items)

words = ['I', 'Love', 'Python']
list = " ".join(words)
print(list)

text = "  hello  "
print(text.strip())

text = "I love cats"
new_text = text.replace("cats", "dogs")
print(new_text)

text = "python"
print(text.lower())
print(text.upper())

text = "I love cats"
new_text = text.replace("cats", "dogs")
print(new_text)   # "I love dogs"

goals = "be_rich be_happy stay_up"
mission = goals.split()
print(mission)
print(len(mission))
wordnumber = goals.count("be_rich")
print(wordnumber)

Members = ("Gideon,Semilore,Timileyin")
people = Members.split(",")
print(people)
print(len(people)
      )
wordnumber = Members.count("")
print(wordnumber)