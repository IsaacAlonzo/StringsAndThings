# Strings
#   data that falls within " " marks

# Concatenation
# Put 2 or more strings together

firstname = "Billy"
lastname =  "Bobby"

fullName = firstname + lastname

print(fullName)

# Repetition
#   repetition operator; *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = 'John W. Cena'
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
#   slicing operator:  :
#   slicing lets us make substrings

print(name[0:3])
print(name[:7])
print(name[4:8])
print(name[4:])

for i in range(1, len(name)+1):
    print(name[0:i])

# Searching inside of strings

print("Cena" in name)
print("W." not in name)

if "h" in name:
    print("The letter h is in name")
else:
    print("The letter h is not in name")


# String Methods to investigate:
# Method        Use Example         Explanation
# center        aStr.center(w)      it centers the string out how many vales you want it
print(name.center(15))
# ljust         aStr.ljust(w)
x = name.ljust(21)
print(x , "is awesome")
# rjust         aStr.rjust(w)
# upper         aStr.upper()
# lower         aStr.lower()
# index         aStr.index(item)
# rindex        aStr.rindex(item)
# find          aStr.find(item)
# rfind         aStr.rfind(item)
# replace       aStr.replace(old, new)

# Be sure to include multiple examples of all of them in use