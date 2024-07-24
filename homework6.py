my_dict = {'Daniil': 1999, 'Anton': 2003,'Sergey': 1985}
print("Dict:",my_dict)
print("Existing value:",my_dict['Daniil'])
print("No existing value:",my_dict.get('Sasha'))

my_dict.update({'Masha': 2005, 'Alex': 1995})
a = my_dict.pop('Masha')
print("Deleted value:",a)
print(my_dict.items())

my_set = {1, 2, 2, 3, 3, 'One', 'One', (3, 4, 5)}
print("Set:",my_set)
my_set.add('new')
my_set.add(10.1)
my_set.remove('One')
print("Modified set:",my_set)


