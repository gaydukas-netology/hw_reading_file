import os

## Task 2

cook_book = {}

with open('recipes.txt') as file:
  for line in file:
    dish_name = line.strip()
    #print(dish_name)
    ingredient_count = file.readline()
    ing_list = []
    for i in range(int(ingredient_count)):
      ing = file.readline()
      ingredient_name, quantity, measure = ing.strip().split(' | ')
      ing_list.append({
        'ingredient_name': ingredient_name,
        'quantity': quantity,
        'measure': measure
      })
      dict_ = {dish_name: ing_list}
      #print(ing_list)
    #print(dict_)
    empty_line = file.readline()
    cook_book.update(dict_)

print(cook_book)
print()

## Task 2

def get_shop_list_by_dishes(dishes,person_count): 
  new_cook = {} 
  #cook_book = my_cook_book() 
  for dish in dishes: 
    if dish in cook_book: 
      for ingredient in cook_book[dish]: 
        ingredient['quantity'] *= person_count
        new_cook.setdefault(ingredient['ingredient_name'], ingredient)
    else:
      print(f'No recipe for {dish}')
  print(new_cook)
  print()

dishes = ['Запеченный картофель', 'Омлет', 'Заливная рыба']
person_count = 1

get_shop_list_by_dishes(dishes,person_count)

## Task 3

with open('1.txt', encoding='utf8') as file_1, open ('2.txt', encoding='utf8') as file_2, open ('3.txt', encoding='utf8') as file_3:
  
  line_count = len(file_1.readlines()), len(file_2.readlines()), len(file_3.readlines())
  
  file_1.seek(0), file_2.seek(0), file_3.seek(0)
  
  file_text = file_1.readlines(), file_2.readlines(), file_3.readlines()
  file_1.close(), file_2.close(), file_3.close()

title_file1 = ['\nThe file 1.txt has ', str(line_count[0]), ' strings.\n']
title_file2 = ['\nThe file 2.txt has ', str(line_count[1]), ' strings.\n']
title_file3 = ['\nThe file 3.txt has ', str(line_count[2]), ' strings.\n']

file_dict = {line_count[0]: ''.join(title_file1), line_count[1]: ''.join(title_file2), line_count[2]: ''.join(title_file3)}

file_dict[line_count[0]] = file_dict.get(line_count[0], '') + ''.join(file_text[0])
file_dict[line_count[1]] = file_dict.get(line_count[1], '') + ''.join(file_text[1])
file_dict[line_count[2]] = file_dict.get(line_count[2], '') + ''.join(file_text[2])

# file_dict = {line_count[0]: file_text[0], line_count[1]: file_text[1], line_count[2]: file_text[2]}
sorted_dict = dict(sorted(file_dict.items()))

with open('result.txt', 'a') as result_file:
  for val in list(sorted_dict.values()):
    for item in val:
        result_file.write(str(item))
    
print(sorted_dict)
