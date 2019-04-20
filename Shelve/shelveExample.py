# shelve provides a shelf similar to a dictionary put is stored in a file rather
# than memory, Assistant dictionary

# Don't use for untrusted data
# Good for persistent data without the overkill of relational databases
import shelve

# Note: shelves are read/write in nature
# Note: cannot initialze a shelf using a literal

# example 1
with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"]) # will work shelf is open
    print(fruit["grape"]) # will work shelf is open

print(fruit["lemon"]) # ERROR -> will not work shelf is closed
print(fruit["grape"]) # ERROR -> will not work shelf is closed

print(fruit) # will provide memory location of the shelf


# Example 2
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"
print(fruit["lemon"]) # will work shelf is open
print(fruit["grape"]) # will work shelf is open

# can update values
fruit["lime"] = "great with tequila"

for snack in fruit:
    print(snack+": "+fruit[snack])

fruit.close()