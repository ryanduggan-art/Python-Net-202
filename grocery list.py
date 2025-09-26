#Grocery List Script

grocery_list = ['Eggs', 'Bread', 'Bacon', 'Milk', 'Cheese']

#Display List
def display_list(grocery_list):
    print(f'Current items on list: {grocery_list}')
#Add Item
def add_item(grocery_list, item):
    grocery_list.append(item)
    print(f'Updated List: {grocery_list}')
#Remove Item
def remove_item(grocery_list, item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f'{item} removed.\nUpdated List: {grocery_list}')
    else:
        print(f'{item} not on list.')
    #Main Program Start
def main():
    display_list(grocery_list)
    new_item = input('Add one new item: ')
    add_item(grocery_list, new_item)
    item_to_remove = input('Type an item to remove: ')
    remove_item(grocery_list, item_to_remove)
main()




