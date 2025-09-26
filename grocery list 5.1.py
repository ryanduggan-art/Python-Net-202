#Grocery List v. 5.1
#Global Variable
grocery_list = ['Eggs','Milk','Bread','Cheese','Bacon']
#Display current list
def display_list(grocery_list):
    print(f'Current List is: {grocery_list}')
#Add item
def add_item(grocery_list, item):
    grocery_list.append(item)
    print(f'Updated List: {grocery_list}')
#Remove item
def remove_item(grocery_list, item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f'{item} removed. Current list: {grocery_list}')
    else:
        print(f'{item} is not on the list')
#start main program
def main():
    global grocery_list
    display_list(grocery_list)
    new_item = input('Add ONE more Item: ')
    add_item(grocery_list, new_item)
    delete_item = input('Type an Item to Remove: ')
    remove_item(grocery_list, delete_item)
#end main program
main()

