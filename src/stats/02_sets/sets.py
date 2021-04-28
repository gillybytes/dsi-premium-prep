# list/set trick for deduping

lst = ['kayaking', 'tennis', 'rolf ball', 'swimming', 'tennis', 'kayaking']


# print(list(set(lst))) # --> ['swimming', 'tennis', 'kayaking', 'rolf ball']


def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)
    
    return deduped

# print(dedupe_in_order(lst))



# STAR ARGS:  *args

def prod_nums(*nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod

print(prod_nums(5,3,5,7,6,9,5,8,1,3,5,7))
print(prod_nums(5,3,5,))








anim_1 = ['jellyfish', 'lion', 'tiger', 'cricket', 'squid', 'cat'] 
anim_2 = ['tiger', 'cat', 'eagle', 'shark', 'manta ray']
anim_3 = ['lion', 'meerkat', 'dog', 'shark', 'eagle', 'prairie dog']

def union(lst1, lst2):
    set_union = lst1.copy()

    for item in lst2:
        if item not in set_union:
            set_union.append(item)
    
    return set_union

# print(union(anim_1, anim_2)) # ['jellyfish', 'lion', 'tiger', 'cricket', 'squid', 'cat', 'eagle', 'shark', 'manta ray']