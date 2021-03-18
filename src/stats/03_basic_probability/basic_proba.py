
pets = ['cat', 'dog', 'ferret', 'goldfish']

'''
Exhaustive set of possibilities for drawing 3 pets WITH REPLACEMENT
'''

pet_outcomes = []

for pet1 in pets:
    for pet2 in pets:
        for pet3 in pets:
            for pet4 in pets:
                pet_outcomes.append([pet1, pet2, pet3, pet4])

# for pet_outcome in pet_outcomes:
#     print(pet_outcome)

two_or_more_cats = []

for pet_outcome in pet_outcomes:
    if pet_outcome.count('cat') >= 2:
        two_or_more_cats.append(pet_outcome)



for item in two_or_more_cats:
    print(item)
print(len(two_or_more_cats) / len(pet_outcomes))