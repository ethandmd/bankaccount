#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


class Account:
    
    #Instantiations 
    def __init__ (self, owner, psk, balance):
        self.owner = owner
        self.psk = psk
        self.balance = balance
        
    #Methods
    def __str__(self):
        return f"Account owner is: {self.owner} \nAccount balance is: ${self.balance}"
    
    def deposit(self, dep):
        '''Add specified deposit amount to existing balance'''
        self.balance += dep
        #return f'Your new account balance is {self.balance}'
        
        
    def withdraw(self, wit):
        '''Subtract specified withdrawal amount as long as it is <= acct balance'''
        if wit <= self.balance:
            self.balance -= wit
        else:
            print('Withdrawal amount exceeds balance amount, transaction cancelled')


# In[3]:


def menu_choice_input():
    '''Take in a number option, run it through a conditions check, and return the choice'''
    
    in_range = False
    menu_options = range(0,4)
    menu_choice = 'wrong'
   
    while menu_choice.isdigit() == False or in_range == False:
        
        menu_choice =(input('Enter a number option corresponding to the service you wish to request.'))
        
        if menu_choice.isdigit() == False:
            print('Please enter a number (integer) option')
            
        if menu_choice.isdigit() == True:
            if int(menu_choice) in menu_options:
                in_range = True
            
            else:
                print('Sorry, that option is not currently mapped')
                in_range = False
                
    return int(menu_choice) 


# In[4]:


def menu_choice_exe(menu_choice):
    '''Take in user menu_choice and execute requested service'''
    #Menu Choices
    if menu_choice == 1:
        print(acct1)
    elif menu_choice == 2:
        acct1.deposit(dep=int(input('Enter deposit amount: ')))
        print(f'Your new account balance is ${acct1.balance}')
    elif menu_choice == 3:
        acct1.withdraw(wit=int(input('Enter withdrawal amount: ')))
        print(f'Your new account balance is ${acct1.balance}')
    else:
        pass


# In[5]:


print('Welcome to Ethan Fiduciary Services LLC \nWe start all customers with $100')

username = input('Please enter a username: ')
password = input('Please enter a password, only letters A-Z, sorry: ')

acct1 = Account(username, password, 100)
clear_output()
print('\nHere are your menu options\n"1" for Account info\n"2" for Deposit Money\n"3" for Withdraw Money')

main_menu = input("Would you like to access the main menu? Y or N: ").upper()

if main_menu == "N":
    interact = False
elif main_menu == "Y":
    print("Please enter password:")
    enter_psk = input('Password: ')
    if enter_psk == acct1.psk:
        interact = True
    else:
        pass
else:
    pass

while interact:
    menu_choice =int(input('Enter a number option corresponding to the service you wish to request.'))
    #menu_choice_input()
    menu_choice_exe(int(menu_choice))
    
    main_menu = input("Would you like to access the main menu? Y or N: ").upper()
    if main_menu == "N":
        clear_output()
        print('Bye.')
        interact = False
    elif main_menu == "Y":
        interact = True
    else:
        pass


# In[ ]:




