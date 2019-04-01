# similar to hashmaps
fruit = {"orange": "a sweet, orange. citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit["lemon"])

# Adding to a dictionary
# Note: Can overwrite a key with a new value
fruit["pear"] = "an odd shaped apple"
print(fruit)

# Removing a key
del fruit["lime"]
print(fruit)

# Clear Dictionaries
fruit.clear()

# Utilizing the .get Method
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)  # getMethod similar to hashmap
        print(description)
    else:
        print("We don't got that")

# Reformatted .get Method, Similar to getOrDefault in Java
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "Sorry we don't got that :(")  # getMethod similar to hashmap
    print(description)

# for loop for dictionaries
for snack in fruit:
    print(fruit[snack])



# Nicer way of iterating through the keys & .keys() method
ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + "-" + fruit[f])
# Same as above
for f in sorted(ordered_keys):
    print(f + "-" + fruit[f])




# .values() method
for val in fruit.values():
    print(val)


print(fruit.keys())
print(fruit.values())
