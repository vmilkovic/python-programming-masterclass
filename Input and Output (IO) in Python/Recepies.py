import shelve

# blt = ['bacon', 'lettuce', 'tomato', 'bread']
# beansOnToast = ['beans', 'bread']
# scrambledEggs = ['eggs', 'butter', 'milk']
soup = ['tin of soup']
# pasta = ['pasta', 'cheese']

with shelve.open('recipes') as recipes:
    # recipes['blt'] = blt
    # recipes['beans on toast'] = beansOnToast
    # recipes['scrambled eggs'] = scrambledEggs
    # recipes['pasta'] = pasta
    # recipes['soup'] = soup

    # Updating the shelve recipes file

    # tempList = recipes['blt']
    # tempList.append('butter')
    # recipes['blt'] = tempList

    # tempList = recipes['pasta']
    # tempList.append('tomato')
    # recipes['pasta'] = tempList

    for snack in recipes:
        print(snack, recipes[snack])

# Writeback update shelve recipes file
with shelve.open('recipes', writeback=True) as recipes:
    # recipes['soup'].append('croutons')

    recipes['soup'] = soup
    recipes.sync()
    soup.append('cream')

    for snack in recipes:
        print(snack, recipes[snack])