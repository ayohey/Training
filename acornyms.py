acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
word = input('Enter your acronym here:\n')
if word in acronyms:
    print(word + ' is in the list.')
else:
    print(word + ' is not in the list.')
print('The current list contains')
for acronym in acronyms:
    print(acronym)   
