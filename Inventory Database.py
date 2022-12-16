# Created June 10, 2021

def outputmenu():
    print('='*12+'Inventory Database'+'='*12)
    print('\nPlease choose one of the following options.\n')
    print('Option A - Enter New Products')
    print('Option B - Change Existing Products')
    print('Option C - Delete Products')
    print('Option D - Print Inventory List')
    print('\n*Press Q to quit\n')
    print('='*38)



def optionA():
    print("\nYou chose: 'Option A - Enter New Products'.")
    print('\nOBJECTIVE:')
    print('Create a data input form to enter new inventory items.')
    
    keepgoing = 'YES'
    
    while keepgoing.upper() in ['YES','Y']:
        
        #Question 1: Product ID
        ID = input("\nEnter product ID: ")
        print('Add to thing')

        #Question 2: Description
        description = input("Enter Product Description: ")

        #Question 3: List Price
        listprice = -1
            
        while listprice < 0:
            user_input = input("Enter List Price: $")
            try:
                listprice = float(user_input)

            except ValueError:
                 print(f"'{user_input}' is not a valid list price. Please enter a valid number.")

        print(f'{listprice} done with listprice')   
    

        #Question 4: Wholesale Price

        wholesale = -1
            
        while wholesale < 0:
            user_answer = input("Enter Wholesale Price: $")
            try:
                wholesale = float(user_answer)

            except ValueError:
                 print(f"'{wholesale}' is not a valid wholesale price. Please enter a valid number.")

        print(f'{wholesale} done with wholesale price')

        #Question 5: Quantity in Stock

        
        quantity = -1
            
        while quantity < 0:
            user_response = input("Enter Quantity in Stock: ")
            try:
                quantity = int(user_response)

            except ValueError:
                 print(f"'{quantity}' is not a valid quantity amount. Please enter a valid number.")

        print(f'{quantity} done with quantity\n')
        
        keepgoing = input('Do you want to enter more products? [Y/N]: ')

        while keepgoing.upper() not in ['YES','Y','NO','N']:
            print(f"'{keepgoing}' is not a valid response. Please enter a valid response.\n")
            keepgoing = input('Do you want to enter more products? [Y/N]: ')
            
    print()
# end of OptionA


def optionB():
    print("\nYou chose: 'Option B - Change Existing Products'.")
    print('\nOBJECTIVE:')
    print('Change inventory.\n')

def optionC():
    print("\nYou chose: 'Option C - Delete Products'.")
    print('\nOBJECTIVE:')
    print('Delete inventory.\n')

def optionD():
    print("\nYou chose: 'Option D - Print Inventory List'.")
    print('\nOBJECTIVE:')
    print('Print inventory list.\n')

    
print()
choice = 'thing'

while choice.upper() not in 'Q':
    outputmenu()
    choice = input('Please choose an option: ')
    
    if choice.upper() not in ['A','OPTION A','B','OPTION B','C','OPTION C','D','OPTION D','Q']:
        print(f"'{choice}' is not a valid option. Please enter a valid option.")
        print("Valid options include: 'A', 'Option A', 'B', 'Option B', 'C', 'Option C', 'D', 'Option D', and 'Q'.\n\n\n\n\n")

    if choice.upper() in ['A','OPTION A']:
        optionA()

    if choice.upper() in ['B','OPTION B']:
        optionB()

    if choice.upper() in ['C','OPTION C']:
        optionC()

    if choice.upper() in ['D','OPTION D']:
        optionD()



