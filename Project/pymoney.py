# ************    Week 12:    ****************# 
import sys

class Record:
    """Represent a record."""
    def __init__(self, date, category, description, amount):
        self._date = date
        self._category = category
        self._descrpt = description
        self._amount = int(amount)
    @property
    def date(self):
        return self._date
    @property
    def category(self):
        return self._category
    @property
    def description(self):
        return self._descrpt
    @property
    def amount(self):
        return self._amount
    
class Records:
#member data of Records:
#wallet, self.record_lst, filtered_records
    def __init__(self):
        """Initialize variables values, or 
        read them from the records.txt file.
        """
        try: 
            fh = open('records.txt', 'r')
        except FileNotFoundError:       #(7) File does not exist. 
            
            try:     #(1) The user want to input a not convertible string
                self._wallet = int(input('How much money do you have? '))  
                self._record_lst = []
            except ValueError:
                sys.stdout.write('\nInvalid: Setting wallet to 0 by default\n')
                self._wallet = 0
                
        else: 
            print('Welcome back!')
            
            try:    #(8) No line to read from the file. 
                walletstr = fh.readline()
                assert walletstr != '', 'The file is empty!'
            except AssertionError as err:      #(8) File is empty, by a possible undesired modification. 
                sys.stdout.write('\nError: %s\n' %err)
                sys.exit(1)

            try:    #(9) the first line cannot be interpreted as initial amount of money.
                self._wallet = int(walletstr)
            except ValueError as err:
                sys.stdout.write('\nError: %s\nFail to read the first line of the file\n\n' %err)
                sys.exit(1)
            
            self._record_lst = fh.readlines()
            for line in self._record_lst: 
                try: #(10) Fail to read any of lines. 
                    bufferRecord = line.split()
                    assert len(bufferRecord) == 3
                except AssertionError: 
                    sys.stdout.write('\nError reading one of the lines of the file!\n\n')
                    sys.exit(1)
            
            indxL = 0 
            for elem in self._record_lst:
                self._record_lst[indxL] = elem.strip('\n')  # removing the '\n' from readlines().
                indxL += 1

            indxL = 0     
            for elem in self._record_lst:               # making my data structure -> (description, value).
                spltrec = elem.split()
                num = int(spltrec[2])
                spltrec.pop(); spltrec.append(num)     
                
                Ltotp = tuple(spltrec)
                
                self._record_lst[indxL] = Ltotp
                indxL += 1 
    
    def add(self, rec_toadd, catg_obj):
        """Method to add a new record in the form 
        of (date, category, description, amount) and add it
        to self._record_lst
        """
        try:
            assert len(rec_toadd) == 3, '\nError: Invalid record given, please add a valid Income/Expense record.'
            if catg_obj.is_category_valid(rec_toadd[0], catg_obj._catg_lst) != True:
                raise ValueError
        except AssertionError as err: 
            sys.stdout.write('%s\n' %err)
            return
        except ValueError: 
            sys.stdout.write('''Error: The specified category is not in the category list.
            \rYou can check the category list by the command "view categories".
            \r--Failed to add a new record.--\n''')
            return
            
        try:
            num = int(rec_toadd[2])
        except ValueError as err: 
            sys.stdout.write('\nError: %s\n' %err)
            print('Invalid: Please enter a valid Income/Expense value\n')
            return
        except UnboundLocalError:
            return
        
        rec_toadd.pop(); rec_toadd.append(num)  # replacing the str type value to int
         
        Ltotp = tuple(rec_toadd)
        self._record_lst.append(Ltotp)     # adding the records as (InEx, value)
    
    def view(self, flag=False):
        """Show all the records updated, made by the user.
        flag         -- to identify if the function was called
                        from the funtion find().
        """
        total_sum = 0
        print('Here\'s your expenses and incomes records:')
        print('{:<15s} {:<20s} {}'.format('Category', 'Description', 'Amount'))
        print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
        if flag == False: 
            for elem in self._record_lst:
                print('{:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2])) 
                total_sum += elem[2]
            print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
            print(f'Now you have {self._wallet+total_sum} dollars.')
        else:
            #view function was called from find()
            for elem in self.filtered_records:
                print('{:<15s} {:<20} {}'.format(elem[0], elem[1], elem[2])) 
                total_sum += elem[2]
            print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
            print(f'Total from the records above: {total_sum}.')
    
    def delete(self):
        """Deletes the selected record from the list of records.
        """
        try: # User doesn't follow design instructions. 
            indxD = int(input())
            if indxD == 0:
                raise ValueError
        except ValueError: #as err:
            print('Invalid index: Please choose an available record number')
            #sys.stdout.write('Error: %s\n' %err)
        else: 
            try: 
                self._record_lst.pop(indxD-1);    # decrease the record qt by 1
            except IndexError: 
                sys.stdout.write(f'There is no \"{indxD}\" index, please choose a valid index.')
        
        return self._record_lst
  
    def find(self, target_catg):
        """Finds the category and sub-related categories asked by the user.
        """
        self.filtered_records = list(filter(lambda x: x[0] in target_catg, self._record_lst))
        self.view(flag=True)
        
    def save(self):
        """Saves the records made from the user into records.txt.
        """
        recordstr = []
        for elem in self._record_lst:       
            # Converting my data structure into list of strings           
            int2str = str(elem[2])      # integer to string
            recordstr.append(elem[0] + ' ' + elem[1] + ' ' + int2str)

        with open('records.txt', 'w') as fh: 
            fh.write('%s\n' %str(self.wallet))
            fh.writelines('%s\n' % line for line in recordstr)  

class Categories():
    def __init__(self):
        self._catg_lst = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', \
        ['bus', 'railway']], 'income', ['salary', 'bonus']]
    
    def is_category_valid(self, category, categors):
        #recursive function to look if an inputed category is valid
        #print(type(categories))
        if type(categors) is list:
            for v in categors: 
                p = self.is_category_valid(category, v)
                if p == True:
                    return p 
        return categors == category
    
    def view(self, categories, prefix=()):
        """Display the available categories."""
        #From the source code of the Outline numbering. 
        if type(categories) is list:
            i = 0
            for v in categories: 
                if type(v) is not list:
                    i += 1
                self.view(v, prefix+(i,))
        else: 
            s = ' '*4*(len(prefix) - 1)
            s += '- ' + categories
            print(s)  
    
    def find_subcategories(self, category):
        """Utility function used by the find function. It will return a flatten list
        of category and subcategories.
        """
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index+1], True)
            else:
                if categories == category or found == True:
                    yield categories
      
        targetcat_lst = [i for i in find_subcategories_gen(category, self._catg_lst)]
        return targetcat_lst
    
categories = Categories()
records = Records()
commandList = ['add', 'view', 'delete', 'view categories', 'find', 'exit']   #List with the possible commmands.

# Pymoney main: 
while True:
    try:    #User input an invalid command.
        command = input('\nWhat do you want to do (add / view / delete / view categories / exit)? ')
        commandList.index(command) 
    except ValueError:
        sys.stdout.write(f'\nError: Invalid intput \"{command}\", please select a valid action.\n')  
        continue    # asking the user to try again
    
    if command == 'add':
        add_record = input('Add an expense or income record with category, description, and amount:\n').split()
        records.add(add_record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        count = 1
        print('Please select the record to delete: ')
        print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
        for elem in records._record_lst:
            print('{:<15s} {:<20} {:<7} [{}]'.format(elem[0], elem[1], elem[2], count))
            count += 1 
        print('='*15, end=''); print(' ', end=''); print('='*20, end=''); print(' ', end=''); print('='*6)
        
        records.delete()     
        
    elif command == 'view categories':
        categories.view(categories._catg_lst)
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)
    else:
        records.save()
        break
#*************************************************************#