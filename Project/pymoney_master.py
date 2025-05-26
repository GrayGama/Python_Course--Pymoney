# # ************    Week 4:    ****************# 
# wallet = int(input('How much money do you have? '))
# record = input('Add an expense or income record with description and amount:\n').split()
# value = int(record[1])
# print(f'Now you have {wallet + value} dollars.')  
# #*************************************************************#


# # ************    Week 5:    ****************#  
# wallet = int(input('How much money do you have? '))
# record = input('Add an expense or income record with description and amount:\n').split(', ')
# print('desc1 amt1, desc2 amt2, desc3 amt3, ...')
# TtoLst = []
# for elem in record: 
#     spltrec = []
#     Ltotp = ()
#     num = 0
    
#     spltrec = elem.split()
#     num = int(spltrec[1])
#     spltrec.pop(); spltrec.append(num)     # replacing the str type value to int
    
#     Ltotp = tuple(spltrec)
    
#     TtoLst.append(Ltotp)                     # required step 3
# valueL = []                                  # storing only the values to add the with sum() 
# for tp in TtoLst: 
#     valueL.append(tp[1])
# totalSum = sum(valueL)      
                 
# print('Here\'s your expenses and income records: ')
# for elem in  record: 
#     print(elem)
# print(f'Now you have {wallet + totalSum} dollars.')  
# #*************************************************************#


# # ************    Week 6:    ****************#  
# wallet = int(input('How much money do you have? '))

# recordLst = []
# indx = 0
# InEx = 0 

# while True: 
#     option = input('What do you want to do (add / view / delete / exit)? ')
    
#     if(option == 'add'):                
#         record = input('Add an expense or income record with description and amount:\n').split()
    
#         num = int(record[1])
#         record.pop(); record.append(num)     # replacing the str type value to int
        
#         Ltotp = tuple(record)
#         recordLst.append(Ltotp)             # adding the records as (description, value)
#         indx += 1
        
#         tp = recordLst[indx-1]              # getting the tuple from the list  
#         InEx += tp[1]                      
                         
            
#     elif(option == 'view'):
#         print('Here\'s your expenses and income records: ')
#         print('{:<20s} {}'.format('Description', 'Amount'))
#         print('='*20, end=''); print(' ', end=''); print('='*6)
#         for elem in recordLst:
#             print('{:<20} {}'.format(elem[0], elem[1])) 
#         print('='*20, end=''); print(' ', end=''); print('='*6)
#         print(f'Now you have {wallet + InEx} dollars.')
        
#     elif(option == 'delete'):
#         # For my delete design I will print the record of the Income/Expenses with 
#         # their respective index and let the user decide which one it prefer to delete
#         count = 1           # For printing purposes 
        
#         print('Please select the record to delete: ')
#         print('='*20, end=''); print(' ', end=''); print('='*6)
#         for elem in recordLst:
#             print('{:<20} {:<7} [{}]'.format(elem[0], elem[1], count))
#             count += 1 
#         print('='*20, end=''); print(' ', end=''); print('='*6)
        
#         indx = int(input())
        
#         tp = recordLst[indx-1]
#         InEx -= tp[1]
#         del(recordLst[indx-1])
        
#     else:
#         break
# #*************************************************************#
   
# # ************    Week 7:    ****************#  
# import sys 

# try: 
#     fh = open('records.txt', 'r')
# except FileNotFoundError:       #(7) File does not exist. 
    
#     try:     #(1) The user want to input a not convertible string
#         wallet = int(input('How much money do you have? ')); print('\n')    
#         recordLst = []
#     except ValueError:
#         sys.stdout.write('\nInvalid: Setting wallet to 0 by default\n')
#         wallet = 0
# else: 
#     print('Welcome back!\n')
    
#     try:    #(8) No line to read from the file. 
#         walletstr = fh.readline()
#         assert walletstr != '', 'The file is empty!'
#     except AssertionError as err:      #(8) File is empty, by a possible undesired modification. 
#         sys.stdout.write('\nError: %s\n' %err)
#         sys.exit(1)
        
#     try:    #(9) the first line cannot be interpreted as initial amount of money.
#        wallet = int(walletstr)
#     except ValueError as err:
#         sys.stdout.write('\nError: %s\nFail to read the first line of the file\n\n' %err)
#         sys.exit(1)
      
#     recordLst = fh.readlines()
#     for line in recordLst: 
#         try: #(10) Fail to read any of lines. 
#             bufferRecord = line.split()
#             assert len(bufferRecord) == 2
#         except AssertionError: 
#             sys.stdout.write('\nError reading one of the lines of the file\n\n')
#             sys.exit(1)
            
# indxL = 0 
# for elem in recordLst:
#     recordLst[indxL] = elem.strip('\n')       # removing the '\n' from readlines().
#     indxL += 1

# indxL = 0     
# for elem in recordLst:               # making my data structure -> (description, value).
#     spltrec = elem.split()
#     num = int(spltrec[1])
#     spltrec.pop(); spltrec.append(num)     
    
#     Ltotp = tuple(spltrec)
    
#     recordLst[indxL] = Ltotp
#     indxL += 1 

# qt = len(recordLst)            # variable to tell the total numbers of elements in recordLst.

# while True: 
#     try:    #(2) the user input an invalid option.
#         option = input('What do you want to do (add / view / delete / exit)? ')
#         assert (option == 'add' or option == 'view' or option == 'delete' or option == 'exit') 
#     except AssertionError:
#         sys.stdout.write(f'\nError: Invalid intput \"{option}\", please select a valid option.\n\n')  
#         continue    # asking the user to try again
         
#     if(option == 'add'):                
#         try:    #(3) User add a not separable string in the form -> 'description' value 
#             record = input('Add an expense or income record with description and amount:\n').split()
#             assert len(record) == 2, '\nError: Invalid record given, please add a valid Income/Expense record.'
#         except AssertionError as err: 
#             sys.stdout.write('%s\n' %err)
#             continue
        
#         try:     #(4) the string is not convertible to integer. 
#             num = int(record[1])
#         except ValueError as err: 
#             sys.stdout.write('\nError: %s\n' %err)
#             print('Invalid: Please enter a valid Income/Expense value\n')
#         record.pop(); record.append(num)  # replacing the str type value to int
        
#         Ltotp = tuple(record)
#         recordLst.append(Ltotp)     # adding the records as (InEx, value)
        
#         tp = recordLst[qt]     # getting the tuple from the list  
#         qt += 1
        
#         wallet += tp[1]        
            
#     elif(option == 'view'):
#         print('Here\'s your expenses and incomes records: ')
#         print('{:<20s} {}'.format('Description', 'Amount'))
#         print('='*20, end=''); print(' ', end=''); print('='*6)
#         for elem in recordLst:
#             print('{:<20} {}'.format(elem[0], elem[1])) 
#         print('='*20, end=''); print(' ', end=''); print('='*6)
#         print(f'Now you have {wallet} dollars.\n')
        
#     elif(option == 'delete'):
#         # For my delete design I will print the record of the Income/Expenses with 
#         # their respective index and let the user decide which one it prefer to delete
#         count = 1   # For printing purposes 
        
#         print('Please select the record to delete: ')
#         print('='*20, end=''); print(' ', end=''); print('='*6)
#         for elem in recordLst:
#             print('{:<20} {:<7} [{}]'.format(elem[0], elem[1], count))
#             count += 1 
#         print('='*20, end=''); print(' ', end=''); print('='*6)
        
#         try: #(5) user doesn't follow design instructions. 
#             indxD = int(input())
#         except ValueError as err:
#             sys.stdout.write('\nError: %s\n' %err)
#             print('Invalid: Please choose an available record\n')
            
#         try: #(6) the user enter a index out of range of the record shown in screen. 
#             tp = recordLst[indxD-1]
#         except IndexError: 
#             sys.stdout.write(f'\nInvalid index: {indxD}, please enter the number of the record to delete\n\n.')
#         else:
#             wallet -= tp[1]
#             recordLst.pop(indxD-1); qt -= 1      # decrease the record qt by 1
        
#     else: #"exit" option
#         break
    
# recordstr = []
# for elem in recordLst:                  # Converting my data structure into list of strings 
#     int2str = str(elem[1])
#     recordstr.append(elem[0] + ' ' + int2str)


# with open('records.txt', 'w') as fh: 
#     fh.write('%s\n' %str(wallet))
#     fh.writelines('%s\n' % line for line in recordstr)
    
# #*************************************************************#

# # # ************    Week 8:    ****************#  
# import sys

# def initialize():
#     try: 
#         fh = open('records.txt', 'r')
#     except FileNotFoundError:       #(7) File does not exist. 
        
#         try:     #(1) The user want to input a not convertible string
#             wallet = int(input('How much money do you have? '))  
#             recordLst = []
#         except ValueError:
#             sys.stdout.write('\nInvalid: Setting wallet to 0 by default\n')
#             wallet = 0
            
#     else: 
#         print('Welcome back!')
        
#         try:    #(8) No line to read from the file. 
#             walletstr = fh.readline()
#             assert walletstr != '', 'The file is empty!'
#         except AssertionError as err:      #(8) File is empty, by a possible undesired modification. 
#             sys.stdout.write('\nError: %s\n' %err)
#             sys.exit(1)

#         try:    #(9) the first line cannot be interpreted as initial amount of money.
#             wallet = int(walletstr)
#         except ValueError as err:
#             sys.stdout.write('\nError: %s\nFail to read the first line of the file\n\n' %err)
#             sys.exit(1)
        
#         recordLst = fh.readlines()
#         for line in recordLst: 
#             try: #(10) Fail to read any of lines. 
#                 bufferRecord = line.split()
#                 assert len(bufferRecord) == 2
#             except AssertionError: 
#                 sys.stdout.write('\nError reading one of the lines of the file\n\n')
#                 sys.exit(1)
        
#         indxL = 0 
#         for elem in recordLst:
#             recordLst[indxL] = elem.strip('\n')  # removing the '\n' from readlines().
#             indxL += 1

#         indxL = 0     
#         for elem in recordLst:               # making my data structure -> (description, value).
#             spltrec = elem.split()
#             num = int(spltrec[1])
#             spltrec.pop(); spltrec.append(num)     
            
#             Ltotp = tuple(spltrec)
            
#             recordLst[indxL] = Ltotp
#             indxL += 1 
            
#     return wallet, recordLst       
# def add(recordList):
#     try:    # User add a not separable string in the form -> 'description' value 
#         record = input('Add an expense or income record with description and amount:\n').split()
#         assert len(record) == 2, '\nError: Invalid record given, please add a valid Income/Expense record.'
#     except AssertionError as err: 
#         sys.stdout.write('%s\n' %err)
    
#     try:     # The string is not convertible to integer. 
#         num = int(record[1])
#     except ValueError as err: 
#         sys.stdout.write('\nError: %s\n' %err)
#         print('Invalid: Please enter a valid Income/Expense value\n')
        
#     record.pop(); record.append(num)  # replacing the str type value to int
    
#     Ltotp = tuple(record)
#     recordList.append(Ltotp)     # adding the records as (InEx, value)
    
#     return recordList
# def view(wallet, recordList):
#     print('Here\'s your expenses and incomes records: ')
#     print('{:<20s} {}'.format('Description', 'Amount'))
#     print('='*20, end=''); print(' ', end=''); print('='*6)
#     for elem in recordList:
#         print('{:<20} {}'.format(elem[0], elem[1])) 
#         wallet += elem[1]
#     print('='*20, end=''); print(' ', end=''); print('='*6)
#     print(f'Now you have {wallet} dollars.')
# def delete(recordList): 
#     # For my delete design I will print the record of the Income/Expenses with 
#     # their respective index and let the user decide which one it prefer to delete
#     count = 1   # For printing purposes 
    
#     print('Please select the record to delete: ')
#     print('='*20, end=''); print(' ', end=''); print('='*6)
#     for elem in recordList:
#         print('{:<20} {:<7} [{}]'.format(elem[0], elem[1], count))
#         count += 1 
#     print('='*20, end=''); print(' ', end=''); print('='*6)
    
#     try: # User doesn't follow design instructions. 
#         indxD = int(input())
#     except ValueError as err:
#         print('Invalid: Please choose an available record number')
#         sys.stdout.write('Error: %s\n\n' %err)
#     else: 
#         try: 
#             recordList.pop(indxD-1);    # decrease the record qt by 1
#         except IndexError: 
#             sys.stdout.write(f'There is no \"{indxD}\" index, please choose a valid index.')
    
#     return recordList
# def save(wallet, recordList):
#     recordstr = []
#     for elem in recordList:                  # Converting my data structure into list of strings 
#         int2str = str(elem[1])
#         recordstr.append(elem[0] + ' ' + int2str)

#     with open('records.txt', 'w') as fh: 
#         fh.write('%s\n' %str(wallet))
#         fh.writelines('%s\n' % line for line in recordstr)
# # Variables:
# initial_money, records = initialize()
# #print('records: ', records)

# # The 5 function calls here
# while True:
#     try:    #User input an invalid command.
#         command = input('\nWhat do you want to do (add / view / delete / exit)? ')
#         assert (command == 'add' or command == 'view' or command == 'delete' or command == 'exit') 
#     except AssertionError:
#         sys.stdout.write(f'\nError: Invalid intput \"{command}\", please select a valid option.\n\n')  
#         continue    # asking the user to try again
    
#     if command == 'add':
#         records = add(records)
#     elif command == 'view':
#         view(initial_money, records)
#     elif command == 'delete':
#         records = delete(records)
#     else:
#         save(initial_money, records)
#         break
# #*************************************************************#

# # ************    Week 9:    ****************#  
# import sys

# #Functions to initilize our variables
# def initialize():
#     """This function will initialize or initial variables values, 
#     by reading from the records.txt file.
#     """
#     try: 
#         fh = open('records.txt', 'r')
#     except FileNotFoundError:       #(7) File does not exist. 
        
#         try:     #(1) The user want to input a not convertible string
#             wallet = int(input('How much money do you have? '))  
#             recordLst = []
#         except ValueError:
#             sys.stdout.write('\nInvalid: Setting wallet to 0 by default\n')
#             wallet = 0
            
#     else: 
#         print('Welcome back!')
        
#         try:    #(8) No line to read from the file. 
#             walletstr = fh.readline()
#             assert walletstr != '', 'The file is empty!'
#         except AssertionError as err:      #(8) File is empty, by a possible undesired modification. 
#             sys.stdout.write('\nError: %s\n' %err)
#             sys.exit(1)

#         try:    #(9) the first line cannot be interpreted as initial amount of money.
#             wallet = int(walletstr)
#         except ValueError as err:
#             sys.stdout.write('\nError: %s\nFail to read the first line of the file\n\n' %err)
#             sys.exit(1)
        
#         recordLst = fh.readlines()
#         for line in recordLst: 
#             try: #(10) Fail to read any of lines. 
#                 bufferRecord = line.split()
#                 assert len(bufferRecord) == 3
#             except AssertionError: 
#                 sys.stdout.write('\nError reading one of the lines of the file\n\n')
#                 sys.exit(1)
        
#         indxL = 0 
#         for elem in recordLst:
#             recordLst[indxL] = elem.strip('\n')  # removing the '\n' from readlines().
#             indxL += 1

#         indxL = 0     
#         for elem in recordLst:               # making my data structure -> (description, value).
#             spltrec = elem.split()
#             num = int(spltrec[2])
#             spltrec.pop(); spltrec.append(num)     
            
#             Ltotp = tuple(spltrec)
            
#             recordLst[indxL] = Ltotp
#             indxL += 1 
            
#     return wallet, recordLst   
    
# def initialize_categories():
#     """Just returns a default list of categories"""
#     return ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', \
#     ['bus', 'railway']], 'income', ['salary', 'bonus']]

# #Functions for the differents commands: 
# def add(recordList):
#     """add function will return the added records to the list in 
#     the form of (category, description, amount)
#     """
#     try:    # User add a not separable string in the form -> 'description' value 
#         record = input('Add an expense or income record with category, description, and amount:\n').split()
#         assert len(record) == 3, '\nError: Invalid record given, please add a valid Income/Expense record.'
        
#         # Check if the first parameter is a valid category
#         if is_category_valid(record[0], categories) != True:
#             raise ValueError
        
#     except AssertionError as err: 
#         sys.stdout.write('%s\n' %err)
#     except ValueError: 
#         sys.stdout.write('''Error: The specified category is not in the category list.
#         \rYou can check the category list by the command "view categories".
#         \r--Failed to add a new record.--\n''')
        
#     else:
        
#         try:     # The string is not convertible to integer. 
#             num = int(record[2])
#         except ValueError as err: 
#             sys.stdout.write('\nError: %s\n' %err)
#             print('Invalid: Please enter a valid Income/Expense value\n')
            
#         record.pop(); record.append(num)  # replacing the str type value to int
        
#         Ltotp = tuple(record)
#         recordList.append(Ltotp)     # adding the records as (InEx, value)
        
#         return recordList
    
# def view(recordList, wallet=0, flag=False):
#     """Show all the records made by the user updated.
#     flag         -- to identify if the function was called
#                     by the user or by the funtion find().
#     """
#     print('Here\'s your expenses and incomes records:')
#     print('{:<15s} {:<20s} {}'.format('Category', 'Description', 'Amount'))
#     print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#     for elem in recordList:
#         print('{:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2])) 
#         wallet += elem[2]
#     print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#     if flag == False: 
#         print(f'Now you have {wallet} dollars.')
#     else:
#         #view function was called from find()
#         print(f'Total from the records above: {wallet}.')

# def delete(recordList): 
#     """Deletes the selected record from the list of records.
#     """
#     # For my delete design I will print the record of the Income/Expenses with 
#     # their respective index and let the user decide which one it prefer to delete
#     count = 1   # For printing purposes 
    
#     print('Please select the record to delete: ')
#     print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#     for elem in recordList:
#         print('{:<15s} {:<20} {:<7} [{}]'.format(elem[0], elem[1], elem[2], count))
#         count += 1 
#     print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
    
#     try: # User doesn't follow design instructions. 
#         indxD = int(input())
#     except ValueError as err:
#         print('Invalid: Please choose an available record number')
#         sys.stdout.write('Error: %s\n\n' %err)
#     else: 
#         try: 
#             recordList.pop(indxD-1);    # decrease the record qt by 1
#         except ValueError: 
#             sys.stdout.write(f'There is no \"{indxD}\" index, please choose a valid index.')
    
#     return recordList

# def view_categories(catgList, prefix=()):
#     """Display the available categories"""
#     #From the source code of the Outline numbering. 
#     if type(catgList) in {list, tuple}:
#         i = 0
#         for v in catgList: 
#             if type(v) not in {list, tuple}:
#                 i += 1
#             view_categories(v, prefix+(i,))
#     else: 
#         s = ' '*4*(len(prefix) - 1)
#         s += '- ' + catgList
#         print(s)  

# def find(records):
#     """Finds the category and sub-related categories asked by the user.
#     """
#     category = input('Which category do you want to find? ') 
#     catgList = find_subcategories(category, categories)
    
#     catgRecords = list(filter(lambda x: x[0] in catgList, records))
#     view(catgRecords, flag=True)    # send a flag to the view function, to let it now
#                                     # that it has to print according to find requirements 
                         
# def save(wallet, recordList):
#     """Saves the records made from the user into records.txt.
#     """
#     recordstr = []
#     for elem in recordList:       
#         # Converting my data structure into list of strings           
#         int2str = str(elem[2])      # integer to string
#         recordstr.append(elem[0] + ' ' + elem[1] + ' ' + int2str)

#     with open('records.txt', 'w') as fh: 
#         fh.write('%s\n' %str(wallet))
#         fh.writelines('%s\n' % line for line in recordstr)
    
# #Tool Functions: 
# def is_category_valid(category, categories):
#     """This utility function returns True if it finds the category asked
#     from the user in the default categories.
#     """
#     #recursive function to look if an inputed category is valid
#     if type(categories) is list:
#         for v in categories: 
#             p = is_category_valid(category, v)
#             if p == True:
#                 return p 
#     return categories == category
# def find_subcategories(category, categories):
#     """Utility function used by the find function. It will return a flatten list
#     of category and subcategories.
#     """
#     if type(categories) == list:
#         for v in categories:
#             p = find_subcategories(category, v)
#             if p == True:
#                 index = categories.index(v)
#                 if index + 1 < len(categories) and \
#                         type(categories[index + 1]) == list:
#                     return flatten(categories[index:index + 2])
#                 else:
#                     # return only itself if no subcategories
#                     return [v]
#             if p != []:
#                 return p
#     return True if categories == category else [] # return [] instead of False if not found
# def flatten(L):
#     if type(L) == list:
#         result = []
#         for child in L:
#             result.extend(flatten(child))
#         return result
#     else:
#         return [L]
 
# # Variables to initialize:
# initial_money, records = initialize()
# categories = initialize_categories()
# commandList = ['add', 'view', 'delete', 'view categories', 'find', 'exit']   #List with the possible commmands.

# #print('records: ', records)
# # print('categories: ', categories)

# # Pymoney main: 
# while True:
#     try:    #User input an invalid command.
#         command = input('\nWhat do you want to do (add / view / delete / view categories / exit)? ')
#         commandList.index(command) 
#     except ValueError:
#         sys.stdout.write(f'\nError: Invalid intput \"{command}\", please select a valid action.\n')  
#         continue    # asking the user to try again
    
#     if command == 'add':
#         records = add(records)
#     elif command == 'view':
#         view(records, initial_money)
#     elif command == 'delete':
#         records = delete(records)
#     elif command == 'view categories':
#         view_categories(categories)
#     elif command == 'find':
#         find(records)
#     else:
#         save(initial_money, records)
#         break
# #*************************************************************#

# ************    Week 11:    ****************#  
# # Variables to initialize:
# import sys

# class Records:
# #member data of Records:
# #wallet, self.record_lst, filtered_records
#     def __init__(self):
#         try: 
#             fh = open('records.txt', 'r')
#         except FileNotFoundError:       #(7) File does not exist. 
            
#             try:     #(1) The user want to input a not convertible string
#                 self._wallet = int(input('How much money do you have? '))  
#                 self._record_lst = []
#             except ValueError:
#                 sys.stdout.write('\nInvalid: Setting wallet to 0 by default\n')
#                 self.wallet = 0
                
#         else: 
#             print('Welcome back!')
            
#             try:    #(8) No line to read from the file. 
#                 walletstr = fh.readline()
#                 assert walletstr != '', 'The file is empty!'
#             except AssertionError as err:      #(8) File is empty, by a possible undesired modification. 
#                 sys.stdout.write('\nError: %s\n' %err)
#                 sys.exit(1)

#             try:    #(9) the first line cannot be interpreted as initial amount of money.
#                 self.wallet = int(walletstr)
#             except ValueError as err:
#                 sys.stdout.write('\nError: %s\nFail to read the first line of the file\n\n' %err)
#                 sys.exit(1)
            
#             self.record_lst = fh.readlines()
#             for line in self.record_lst: 
#                 try: #(10) Fail to read any of lines. 
#                     bufferRecord = line.split()
#                     assert len(bufferRecord) == 3
#                 except AssertionError: 
#                     sys.stdout.write('\nError reading one of the lines of the file!\n\n')
#                     sys.exit(1)
            
#             indxL = 0 
#             for elem in self.record_lst:
#                 self.record_lst[indxL] = elem.strip('\n')  # removing the '\n' from readlines().
#                 indxL += 1

#             indxL = 0     
#             for elem in self.record_lst:               # making my data structure -> (description, value).
#                 spltrec = elem.split()
#                 num = int(spltrec[2])
#                 spltrec.pop(); spltrec.append(num)     
                
#                 Ltotp = tuple(spltrec)
                
#                 self.record_lst[indxL] = Ltotp
#                 indxL += 1 
    
#     def add(self, rec_toadd, catg_obj):
#         try:
#             assert len(rec_toadd) == 3, '\nError: Invalid record given, please add a valid Income/Expense record.'
#             if catg_obj.is_category_valid(rec_toadd[0], catg_obj.catg_lst) != True:
#                 raise ValueError
#         except AssertionError as err: 
#             sys.stdout.write('%s\n' %err)
#             return
#         except ValueError: 
#             sys.stdout.write('''Error: The specified category is not in the category list.
#             \rYou can check the category list by the command "view categories".
#             \r--Failed to add a new record.--\n''')
#             return
            
#         try:
#             num = int(rec_toadd[2])
#         except ValueError as err: 
#             sys.stdout.write('\nError: %s\n' %err)
#             print('Invalid: Please enter a valid Income/Expense value\n')
#             return
#         except UnboundLocalError:
#             return
        
#         rec_toadd.pop(); rec_toadd.append(num)  # replacing the str type value to int
         
#         Ltotp = tuple(rec_toadd)
#         self.record_lst.append(Ltotp)     # adding the records as (InEx, value)
    
#     def view(self, flag=False):
#         print('Here\'s your expenses and incomes records:')
#         print('{:<15s} {:<20s} {}'.format('Category', 'Description', 'Amount'))
#         print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#         if flag == False: 
#             for elem in self.record_lst:
#                 print('{:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2])) 
#                 self.wallet += elem[2]
#             print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#             print(f'Now you have {self.wallet} dollars.')
#         else:
#             #view function was called from find()
#             for elem in self.filtered_records:
#                 print('{:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2])) 
#                 self.wallet += elem[2]
#             print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#             print(f'Total from the records above: {self.wallet}.')
    
#     def delete(self):
#         try: # User doesn't follow design instructions. 
#             indxD = int(input())
#         except ValueError as err:
#             print('Invalid index: Please choose an available record number')
#             sys.stdout.write('Error: %s\n\n' %err)
#         else: 
#             try: 
#                 self.record_lst.pop(indxD-1);    # decrease the record qt by 1
#             except IndexError: 
#                 sys.stdout.write(f'There is no \"{indxD}\" index, please choose a valid index.')
        
#         return self.record_lst
  
#     def find(self, target_catg):
#         self.filtered_records = list(filter(lambda x: x[0] in target_catg, self.record_lst))
#         self.view(flag=True)
        
#     def save(self):
#         """Saves the records made from the user into records.txt.
#         """
#         recordstr = []
#         for elem in self.record_lst:       
#             # Converting my data structure into list of strings           
#             int2str = str(elem[2])      # integer to string
#             recordstr.append(elem[0] + ' ' + elem[1] + ' ' + int2str)

#         with open('records.txt', 'w') as fh: 
#             fh.write('%s\n' %str(self.wallet))
#             fh.writelines('%s\n' % line for line in recordstr)  

# class Categories():
#     def __init__(self):
#         self.catg_lst = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', \
#         ['bus', 'railway']], 'income', ['salary', 'bonus']]
    
#     def is_category_valid(self, category, categors):
#         #recursive function to look if an inputed category is valid
#         #print(type(categories))
#         if type(categors) is list:
#             for v in categors: 
#                 p = self.is_category_valid(category, v)
#                 if p == True:
#                     return p 
#         return categors == category
#     #Reference: https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
#     def view(self, categories, prefix=()):
#         """Display the available categories."""
#         #From the source code of the Outline numbering. 
#         if type(categories) is list:
#             i = 0
#             for v in categories: 
#                 if type(v) is not list:
#                     i += 1
#                 self.view(v, prefix+(i,))
#         else: 
#             s = ' '*4*(len(prefix) - 1)
#             s += '- ' + categories
#             print(s)  
    
#     def find_subcategories(self, category, categories):
#         """Utility function used by the find function. It will return a flatten list
#         of category and subcategories.
#         """
#         if type(categories) == list:
#             for v in categories:
#                 p = self.find_subcategories(category, v)
#                 if p == True:
#                     index = categories.index(v)
#                     if index + 1 < len(categories) and \
#                             type(categories[index + 1]) == list:
#                         return self._flatten(categories[index:index + 2])
#                     else:
#                         # return only itself if no subcategories
#                         return [v]
#                 if p != []:
#                     return p
#         return True if categories == category else [] # return [] instead of False if not found
    
#     def _flatten(self, L):
#         if type(L) == list:
#             result = []
#             for child in L:
#                 result.extend(self._flatten(child))
#             return result
#         else:
#             return [L]
            
# categories = Categories()
# records = Records()
# commandList = ['add', 'view', 'delete', 'view categories', 'find', 'exit']   #List with the possible commmands.

# # Pymoney main: 
# while True:
#     try:    #User input an invalid command.
#         command = input('\nWhat do you want to do (add / view / delete / view categories / exit)? ')
#         commandList.index(command) 
#     except ValueError:
#         sys.stdout.write(f'\nError: Invalid intput \"{command}\", please select a valid action.\n')  
#         continue    # asking the user to try again
    
#     if command == 'add':
#         add_record = input('Add an expense or income record with category, description, and amount:\n').split()
#         records.add(add_record, categories)
#     elif command == 'view':
#         records.view()
#     elif command == 'delete':
#         count = 1
#         print('Please select the record to delete: ')
#         print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#         for elem in records.record_lst:
#             print('{:<15s} {:<20} {:<7} [{}]'.format(elem[0], elem[1], elem[2], count))
#             count += 1 
#         print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
        
#         records.delete()     
        
#     elif command == 'view categories':
#         categories.view(categories.catg_lst)
#     elif command == 'find':
#         category = input('Which category do you want to find? ')
#         target_categories = categories.find_subcategories(category, categories.catg_lst)
#         records.find(target_categories)
#     else:
#         records.save()
#         break
# #*************************************************************#
# # ************    Week 12:    ****************# 
# import sys

# class Records:
# #member data of Records:
# #wallet, self.record_lst, filtered_records
#     def __init__(self):
#         try: 
#             fh = open('records.txt', 'r')
#         except FileNotFoundError:       #(7) File does not exist. 
            
#             try:     #(1) The user want to input a not convertible string
#                 self._wallet = int(input('How much money do you have? '))  
#                 self._record_lst = []
#             except ValueError:
#                 sys.stdout.write('\nInvalid: Setting wallet to 0 by default\n')
#                 self.wallet = 0
                
#         else: 
#             print('Welcome back!')
            
#             try:    #(8) No line to read from the file. 
#                 walletstr = fh.readline()
#                 assert walletstr != '', 'The file is empty!'
#             except AssertionError as err:      #(8) File is empty, by a possible undesired modification. 
#                 sys.stdout.write('\nError: %s\n' %err)
#                 sys.exit(1)

#             try:    #(9) the first line cannot be interpreted as initial amount of money.
#                 self.wallet = int(walletstr)
#             except ValueError as err:
#                 sys.stdout.write('\nError: %s\nFail to read the first line of the file\n\n' %err)
#                 sys.exit(1)
            
#             self.record_lst = fh.readlines()
#             for line in self.record_lst: 
#                 try: #(10) Fail to read any of lines. 
#                     bufferRecord = line.split()
#                     assert len(bufferRecord) == 3
#                 except AssertionError: 
#                     sys.stdout.write('\nError reading one of the lines of the file!\n\n')
#                     sys.exit(1)
            
#             indxL = 0 
#             for elem in self.record_lst:
#                 self.record_lst[indxL] = elem.strip('\n')  # removing the '\n' from readlines().
#                 indxL += 1

#             indxL = 0     
#             for elem in self.record_lst:               # making my data structure -> (description, value).
#                 spltrec = elem.split()
#                 num = int(spltrec[2])
#                 spltrec.pop(); spltrec.append(num)     
                
#                 Ltotp = tuple(spltrec)
                
#                 self.record_lst[indxL] = Ltotp
#                 indxL += 1 
    
#     def add(self, rec_toadd, catg_obj):
#         try:
#             assert len(rec_toadd) == 3, '\nError: Invalid record given, please add a valid Income/Expense record.'
#             if catg_obj.is_category_valid(rec_toadd[0], catg_obj.catg_lst) != True:
#                 raise ValueError
#         except AssertionError as err: 
#             sys.stdout.write('%s\n' %err)
#             return
#         except ValueError: 
#             sys.stdout.write('''Error: The specified category is not in the category list.
#             \rYou can check the category list by the command "view categories".
#             \r--Failed to add a new record.--\n''')
#             return
            
#         try:
#             num = int(rec_toadd[2])
#         except ValueError as err: 
#             sys.stdout.write('\nError: %s\n' %err)
#             print('Invalid: Please enter a valid Income/Expense value\n')
#             return
#         except UnboundLocalError:
#             return
        
#         rec_toadd.pop(); rec_toadd.append(num)  # replacing the str type value to int
         
#         Ltotp = tuple(rec_toadd)
#         self.record_lst.append(Ltotp)     # adding the records as (InEx, value)
    
#     def view(self, flag=False):
#         print('Here\'s your expenses and incomes records:')
#         print('{:<15s} {:<20s} {}'.format('Category', 'Description', 'Amount'))
#         print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#         if flag == False: 
#             for elem in self.record_lst:
#                 print('{:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2])) 
#                 self.wallet += elem[2]
#             print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#             print(f'Now you have {self.wallet} dollars.')
#         else:
#             #view function was called from find()
#             for elem in self.filtered_records:
#                 print('{:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2])) 
#                 self.wallet += elem[2]
#             print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#             print(f'Total from the records above: {self.wallet}.')
    
#     def delete(self):
#         try: # User doesn't follow design instructions. 
#             indxD = int(input())
#         except ValueError as err:
#             print('Invalid index: Please choose an available record number')
#             sys.stdout.write('Error: %s\n\n' %err)
#         else: 
#             try: 
#                 self.record_lst.pop(indxD-1);    # decrease the record qt by 1
#             except IndexError: 
#                 sys.stdout.write(f'There is no \"{indxD}\" index, please choose a valid index.')
        
#         return self.record_lst
  
#     def find(self, target_catg):
#         self.filtered_records = list(filter(lambda x: x[0] in target_catg, self.record_lst))
#         self.view(flag=True)
        
#     def save(self):
#         """Saves the records made from the user into records.txt.
#         """
#         recordstr = []
#         for elem in self.record_lst:       
#             # Converting my data structure into list of strings           
#             int2str = str(elem[2])      # integer to string
#             recordstr.append(elem[0] + ' ' + elem[1] + ' ' + int2str)

#         with open('records.txt', 'w') as fh: 
#             fh.write('%s\n' %str(self.wallet))
#             fh.writelines('%s\n' % line for line in recordstr)  

# class Categories():
#     def __init__(self):
#         self.catg_lst = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', \
#         ['bus', 'railway']], 'income', ['salary', 'bonus']]
    
#     def is_category_valid(self, category, categors):
#         #recursive function to look if an inputed category is valid
#         #print(type(categories))
#         if type(categors) is list:
#             for v in categors: 
#                 p = self.is_category_valid(category, v)
#                 if p == True:
#                     return p 
#         return categors == category
    
#     def view(self, categories, prefix=()):
#         """Display the available categories."""
#         #From the source code of the Outline numbering. 
#         if type(categories) is list:
#             i = 0
#             for v in categories: 
#                 if type(v) is not list:
#                     i += 1
#                 self.view(v, prefix+(i,))
#         else: 
#             s = ' '*4*(len(prefix) - 1)
#             s += '- ' + categories
#             print(s)  
    
#     def find_subcategories(self, category):
#         """Utility function used by the find function. It will return a flatten list
#         of category and subcategories.
#         """
#         def find_subcategories_gen(category, categories, found=False):
#             if type(categories) == list:
#                 #print('categories: ', categories)
#                 for index, child in enumerate(categories):
#                     yield from find_subcategories_gen(category, child, found)
#                     if child == category and index + 1 < len(categories) \
#                         and type(categories[index + 1]) == list:
#                         # When the target category is found,
#                         # recursively call this generator on the subcategories
#                         # with the flag set as True.
#                         yield from find_subcategories_gen(category, categories[index+1], True)
#             else:
#                 if categories == category or found == True:
#                     yield categories
      
#         targetcat_lst = [i for i in find_subcategories_gen(category, self.catg_lst)]
#         return targetcat_lst
#     #Reference: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

# categories = Categories()
# records = Records()
# commandList = ['add', 'view', 'delete', 'view categories', 'find', 'exit']   #List with the possible commmands.

# # Pymoney main: 
# while True:
#     try:    #User input an invalid command.
#         command = input('\nWhat do you want to do (add / view / delete / view categories / exit)? ')
#         commandList.index(command) 
#     except ValueError:
#         sys.stdout.write(f'\nError: Invalid intput \"{command}\", please select a valid action.\n')  
#         continue    # asking the user to try again
    
#     if command == 'add':
#         add_record = input('Add an expense or income record with category, description, and amount:\n').split()
#         records.add(add_record, categories)
#     elif command == 'view':
#         records.view()
#     elif command == 'delete':
#         count = 1
#         print('Please select the record to delete: ')
#         print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
#         for elem in records.record_lst:
#             print('{:<15s} {:<20} {:<7} [{}]'.format(elem[0], elem[1], elem[2], count))
#             count += 1 
#         print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
        
#         records.delete()     
        
#     elif command == 'view categories':
#         categories.view(categories.catg_lst)
#     elif command == 'find':
#         category = input('Which category do you want to find? ')
#         target_categories = categories.find_subcategories(category)
#         records.find(target_categories)
#     else:
#         records.save()
#         break

# #*************************************************************#
# ************    Week 13:    ****************# 
import sys
from pyrecord import *
from pycategory import *    

categories = Categories()
records = Records()
commandList = ['add', 'view', 'delete', 'view categories', 'find', 'exit']   #List with the possible commmands.
print(records._record_lst)

# Pymoney main: 
while True:
    try:    #User input an invalid command.
        command = input('\nWhat do you want to do (add | view | delete | view categories | find | exit)? ')
        commandList.index(command) 
    except ValueError:
        sys.stdout.write(f'\nError: Invalid intput \"{command}\", please select a valid option.\n')  
        continue    # asking the user to try again
    
    if command == 'add':
        add_record = input('Add an expense or income record with category, description, and amount:\n').split()
        records.add(add_record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        count = 1
        #Interface of my 'delete' function:
        print('Please select the record to delete: ')
        print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
        for elem in records._record_lst:
            print('{:<15s} {:<20} {:<10} [{}]'.format(elem[0], elem[1], elem[2], count))
            count += 1 
        print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
        #calling the method:
        records.delete()     
    elif command == 'view categories':
        categories.view(categories.catg_lst)
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)
    else:
        records.save()
        break
# #*************************************************************#
# ************    Week 14:    ****************# 
