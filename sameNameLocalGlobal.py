def spam():
    global eggs
    eggs = 'spam'  # this is the global

def bacon():
    eggs = 'bacon'  # this is a locals

def ham():
    print(eggs) # this is the global

eggs = 42   # this is the globa;
spam()
print(eggs)
