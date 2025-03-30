def read_cookbook(file_name):
    cookbook = {}
    
    with open(file_name, encoding= 'utf-8') as f:
            dish_name = f.readline().strip()
            ingredients_count = int(f.readline().strip())
            ingredients = []  
            for i in range(ingredients_count):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure})
                
            cookbook[dish_name] = ingredients  

    return cookbook

file_path = "C:/Users/Роман Никитенко/Downloads/recipes.txt"
cookbookk = read_cookbook(file_path)

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}  
    for dish_name in dishes:
        if dish_name in cookbookk:
            ingredients = cookbookk[dish_name]  
            for ingredient in ingredients:  
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name in shopping_list:
                    shopping_list[ingredient_name]['quantity'] += quantity  
                else:
                    shopping_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
    return shopping_list

shopping_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shopping_list)
