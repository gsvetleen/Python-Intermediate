myList = ["a","b","c","d"]

newString = ''

# Not efficient strings are immutable, therefore it will continuously
# recreate the string - memory cost
for c in myList:
    newString += c + ","


# More efficient and preferred
newString = ",".join(myList) #a,b,c,d
print(newString)

#ex 2

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

newString = "mississippi ".join(numbers)
print(newString)