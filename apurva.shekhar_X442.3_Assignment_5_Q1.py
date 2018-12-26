fruits = {}
fruits['apple'] = 2
fruits['banana'] = 3
fruits['grapes'] = 4
fruits['pineapple'] = 5
fruits_names = []
for fruit_name in fruits.keys():
    fruits_names.append(fruit_name)
fruits_names.sort()
for fruit_name in fruits_names:
    print(fruit_name,fruits[fruit_name])
