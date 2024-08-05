my_dict = {'Valeria': 2001, 'Mary': 2007, 'Alex': 1997, 'Denis': 1999}
print('Dict:', my_dict)
print('Existing value: ', my_dict['Valeria'])
print('Not existing value: ', my_dict.get('Helen'))
my_dict.update({'Max': 2000, 'Oleg': 1996})
print('Deleted value: ', my_dict.pop('Mary'))
print('Modified dictionary: :', my_dict)

my_set = {8,7,6,8,7,6, 'Valeria', True, 'Valeria', True}
print('Set: ', my_set)
my_set.update([5, False])
my_set.discard('Valeria')
print('Modified set: ', my_set)