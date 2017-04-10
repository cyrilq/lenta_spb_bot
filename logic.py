import random

list_of_guys = [
    'umerenkov',
    'kiseliov'
]
list_of_girls = [
    'romanova',
    'anikina'
]

list_of_complete_couples = [()]


def get_the_name(gotten_name: object) -> object:
    if gotten_name in list_of_guys:
        random_girls_name = random.choice(list_of_girls)
        list_of_complete_couples.append((gotten_name, random_girls_name))
        list_of_guys.remove(gotten_name)
        list_of_girls.remove(random_girls_name)
        
    return list_of_complete_couples[-1]

print(get_the_name('umerenkov'))