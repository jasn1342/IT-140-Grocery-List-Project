#empty data structure
grocery_item = {}

#empty list
grocery_history = [] 

#Variable used to check if the while loop condition is met
stop = 'go'

while stop != "q": 

    #User inputs item name
    item_name = input('Item Name:\n') 
    #User inputs quantity purchased
    quantity = input ('Quantity purchased:\n') 
    #User inputs price of item
    cost = input('Price per item:\n')
   
    grocery_item['name'] = item_name
    grocery_item['number'] = int(quantity)
    grocery_item['price'] = float(cost) #float allows decimal
    
    grocery_history.append(grocery_item.copy())
    #User is prompted to add another item or calculate total
    stop = input("Would you like to enter another item? \nType 'c' for continue or 'q' to quit:\n")

# Define variable to hold grand total called 'grand_total'
grand_total = 0
  

for index, item in enumerate(grocery_history):
  
  #Calculate the total cost for the grocery_item.
  item_total = item['number']* item['price']
  #Add the item_total to the grand_total
  grand_total = grand_total + item_total
  #Output the information for the grocery item.
  print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
  
  

  item_total = 0

print("Grand total: $%.2f" % grand_total)
