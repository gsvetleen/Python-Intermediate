# Two ways to initialize
# example 1
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

# example 2
wild_animals = set(["lion", "tiger", "lion", "hare", "panther", "elephant"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

# adding to set

farm_animals.add("horse")
wild_animals.add("horse")

# NOTE: Can not use add to an empty set

# can convert any iterable object to a set
even = set(range(0, 40, 2))  # will be unordered
print(even)
squared_tuple = (4, 6, 9, 16, 25)
squares = set(squared_tuple)
print(squares)

# can use union to combine sets

print(even.union(squares))
print(len(even.union(squares)))
print("-" * 40)
# .intersection or & -> used to combine similar elements on both sets
print(even.intersection(squares))
print(even & squares)

# subtract similar elements from sets -> .difference() or -

print("Even minus squares")
print(sorted(even.difference(squares)))
print(even - squares)

print("Squares minus even")
print(squares.difference(even))
print(squares - even)


# .diiference_update() updates the set after removing the elements

even.difference_update(squares)
print(sorted(even))