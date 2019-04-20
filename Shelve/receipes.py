import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # NOTE -> Once it runs you can comment out the rest of the original dictionary
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # NOTE modifying what is already shelved
    # ex1
    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list
    # ex2
    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list

    # NOTE -> Using writeback allows you to omit doing lines 19-25
    # but costs a huge amount of memory lost
    recipes["soup"].append("croutons")
    for snack in recipes:
        print(snack, recipes[snack])
