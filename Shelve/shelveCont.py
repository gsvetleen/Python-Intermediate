import shelve
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"
print(fruit["lemon"]) # will work shelf is open
print(fruit["grape"]) # will work shelf is open

while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key == "quit":
        break
    description = fruit.get(shelf_key, "We don't have a "+shelf_key)
    print(description)

# sort keys in shelf

ordered_keys = list(fruit.keys())
sorted(ordered_keys)

for f in ordered_keys:
    print(f + "-"+fruit[f] )