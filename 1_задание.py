def read_cookbook(file_name):
    cookbook = {}
    
    with open(file_name, encoding= 'utf-8') as f:
        for line in f:
            line = line.strip()
            dish_name = line
            ingredients_count = int(f.readline().strip())
            ingridients = []
            for i in range(ingredients_count):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                ingridients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
                
                cookbook[dish_name] = ingridients
    
    return cookbook
            
file_path = "C:/Users/Роман Никитенко/Downloads/recipes.txt"
cookbookk = read_cookbook(file_path)
print(cookbookk)


# {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'}, {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'}, {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}]}
# PS C:\Users\Роман Никитенко\Desktop\boje> 


